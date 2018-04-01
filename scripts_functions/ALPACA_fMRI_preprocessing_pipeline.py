# ALPACA_fMRI_preprocessing_pipeline.py
# This script performs a base and MVPA preprocessing pipeline on fMRI data, as well as creates different masks to use
# during 1st level statistics. It includes unzipping of .gz functionals, realignment (AFNI), artifact detection, coregistration (FreeSurfer), smoothing (FSL),
# tsnr, demean, standard deviation & z-standard. It furthermore aggregates all volumes/sessions into one, samples volume
# data to the surface reconstruction from FreeSurfer and also aggregates the resulting surface files into one (per hemisphere).
# Subsequently, you can do some 1st level analysis for example using nipy, fsl or SPM.
# -*- coding: utf-8 -*-

# Ver. 1 - 04/2017 - Peer Herholz (herholz dot peer at gmail dot com)


##### Import important modules #####

from os.path import join as opj
from nipype.interface.afni import Despike
from nipype.interfaces.freesurfer import BBRegister, ApplyVolTransform, Binarize, Concatenate, MRIConvert, FSCommand
from nipype.interfaces.fsl import BET, BinaryMaths, ImageMaths, ImageStats, MCFLIRT, PlotMotionParams, SUSAN
from nipype.interfaces.utility import Function, IdentityInterface
from nipype.interfaces.io import SelectFiles, DataSink
from nipype.algorithms.rapidart import ArtifactDetect
from nipype.algorithms.misc import Gunzip
from nipype.algorithms.confounds import TSNR
from nipype.pipeline.engine import Workflow, Node, MapNode

##### Specify interface behaviors #####

# FreeSurfer - Specify the location of the freesurfer folder
fs_dir = '../resources/example_data/derivatives/mindboggle/freesurfer_subjects'
FSCommand.set_default_subjects_dir(fs_dir)

##### Specify important variables #####

experiment_dir = '../resources/example_data/' # location of experiment folder
subject_list = ['sub-01'] # create the subject_list variable

output_dir = 'output_prepro_ALPACA' # name of output folder
working_dir = 'workingdir_prepro_ALPACA' # name of working directory

fwhm_size=6

##### Create & specify nodes to be used and connected during the preprocessing pipeline #####

### base preprocessing pipeline

# Realign - correct for motion
realign = Node(MCFLIRT(mean_vol=True, save_mats=True, save_plots=True, save_rms=True, outputtype='NIFTI'),
               name="realign")

# Plot the rotations, translations, and displacement parameters from MCFLIRT
plotrot = MapNode(PlotMotionParams(in_source="fsl",
                                          plot_type="rotations"),
                         name="plotrotation",
                         iterfield=["in_file"])

plottrans = MapNode(PlotMotionParams(in_source="fsl",
                                                plot_type="translations"),
                           name="plottranslation",
                           iterfield=["in_file"])

plotdisp = MapNode(PlotMotionParams(in_source="fsl",
                                               plot_type="displacement"),
                          name="plotdisplacement",
                          iterfield=["in_file"])

# BBRegister - coregister a volume to the Freesurfer anatomical
bbregister = Node(BBRegister(init='spm',
                             contrast_type='t2',
                             out_fsl_file=True),
                  name='bbregister')

# Artifact Detection - determine which of the images in the functional series
# are outliers. This is based on deviation in intensity or movement.
art = Node(ArtifactDetect(norm_threshold=1,
                          zintensity_threshold=3,
                          mask_type='file',
                          parameter_source='FSL',
                          use_differences=[True, False]),
           name="art")

# Gunzip - unzip functional
gunzip = MapNode(Gunzip(), name="gunzip", iterfield=['in_file'])

# Smooth - to smooth the images with a given kernel
smooth = Node(SUSAN(fwhm=fwhm_size, brightness_threshold=2000.0),
              name="smooth")

# Create the base preprocessing workflow
preproc_ALPACA_base = Workflow(name='preproc_ALPACA_base')
preproc_ALPACA_base.base_dir = opj(experiment_dir, working_dir)

# Connect the base preprocessing nodes to a pipeline
preproc_ALPACA_base.connect([(gunzip, realign, [('out_file', 'in_file')]),
                 (realign, plotrot, [('par_file', 'in_file')]),
                 (realign, plottrans, [('par_file', 'in_file')]),
                 (realign, plotdisp,  [('rms_files', 'in_file')]),
                 (realign, bbregister, [('mean_img', 'source_file')]),
                 (realign, art, [('par_file', 'realignment_parameters'),
                                ('mean_img', 'mask_file')]),
                 (realign, art, [('out_file', 'realigned_files')]),
                 (realign, smooth, [('out_file', 'in_file')]),
                 ])

### MVPA preprocessing pipeline

# Transform node - apply volume transformation
applyVolReg = Node(ApplyVolTransform(fs_target = True, no_resample=True),
                   name='applyVolReg')

# Despike node - despike data
despike = Node(Despike(outputtype='NIFTI'),
               name='despike')

# TSNR node - remove polynomials 2nd order
tsnr = Node(TSNR(regress_poly=2),
            name='tsnr')

# Demean node - demean data
demean = Node(BinaryMaths(operation='sub'),
              name='demean')

# Standard deviation node - calculate standard deviation
standev = Node(ImageStats(op_string='-S'), name='standev')

# Z-standardize node - z-standardize data
zstandardize = Node(BinaryMaths(operation = 'div'), name='zstandardize')

# Create the MVPA preprocessing workflow
preproc_ALPACA_MVPA = Workflow(name='preproc_ALPACA_MVPA')
preproc_ALPACA_MVPA.base_dir = opj(experiment_dir, working_dir)

# Connect the MVPA preprocessing nodes to a pipeline
preproc_ALPACA_MVPA.connect([(despike, applyVolReg,[('out_file', 'source_file')]),
                 (applyVolReg, tsnr, [('transformed_file', 'in_file')]),
                 (tsnr, demean, [('detrended_file', 'in_file')]),
                 (tsnr, demean, [('mean_file', 'operand_file')]),
                 (demean, standev, [('out_file', 'in_file')]),
                 (demean, zstandardize, [('out_file', 'in_file')]),
                 (standev, zstandardize, [('out_stat', 'operand_value')]),
                 ])

### MVPA volume and surface pipeline

# Concatenate Volume node - concatenates all session files into one file
concatVol = Node(Concatenate(), name='concatVol')

# Create volume pipeline
volume_flow = Workflow(name='volume_flow')

## create the surface workflow ##

# Copy the concatenate node from the volume pipeline
concatSurfLH = concatVol.clone('concatSurfLH')
concatSurfRH = concatVol.clone('concatSurfRH')

# Convert NIfTI into mgz
mriconvertSurfLH = Node(MRIConvert(out_type = 'mgz'),name='mriconvertSurfLH')
mriconvertSurfRH = Node(MRIConvert(out_type = 'mgz'),name='mriconvertSurfRH')

# Sample Left node - samples the volume data onto the surface representation
samplerLH = Node(SampleToSurface(hemi='lh',
                                    interp_method = 'trilinear',
                                    sampling_method = 'average',
                                    sampling_range = (0.1, 0.9, 0.1),
                                    sampling_units = 'frac'),
                 name='samplerLH')

# Sample Right node - does the same as the node above,
#                     but on the right hemisphere
samplerRH = samplerLH.clone('samplerRH')
samplerRH.inputs.hemi = 'rh'

# Create surface pipeline
surface_flow = Workflow(name='surface_flow')

# Connect the surface nodes to a pipeline
surface_flow.connect([(samplerLH, concatSurfLH, [('out_file', 'in_files')]),
                  (samplerRH, concatSurfRH,  [('out_file', 'in_files')]),
                  (concatSurfLH, mriconvertSurfLH, [('concatenated_file', 'in_file')]),
                  (concatSurfRH, mriconvertSurfRH, [('concatenated_file', 'in_file')]),
                  ])

### mask preprocessing pipeline

# meanfuncmask - create a whole brain mask from the mean functional based on FSL's robust BET
meanfuncmask = Node(BET(mask=True,
                        no_output=False,
                        frac=0.55,
                        robust=True,
                        output_type='NIFTI',
                        out_file='meanfunc'),
                       name='meanfuncmask')

# Binarize Cortex node - creates a binary map of cortical voxel
binarizeCortical = Node(Binarize(out_type='nii.gz',
                                    match = [3,42],
                                    binary_file='binarized_cortical.nii.gz'),
                        name='binarizeCortical')

# Binarize Subcortex node - creates a binary map of subcortical voxel
binarizeSubcortical = Node(Binarize(out_type='nii.gz',
                                       match = [8,47,   # Cerebellum
                                                10,49,  # Thalamus
                                                11,50,  # Caudate
                                                12,51,  # Putamen
                                                13,52,  # Pallidum
                                                17,53,  # Hippocampus
                                                18,54,  # Amygdala
                                                26,58,  # AccumbensArea
                                                251,252,253,254,255,  # Corpus Callosum
                                                85,     # Optic Chiasm
                                                16      # Brain-Stem
                                                ],
                                    binary_file='binarized_subcortical.nii.gz'),
                       name='binarizeSubcortical')

# Brainmask node - combines cortical and subcortical binary maps
wholebrainmask = Node(BinaryMaths(operation='add',
                                 args='-bin'),
                 name='wholebrainmask')

# Volume Transformation - transform the brainmask into functional space
applyVolTrans_complete_mask = Node(ApplyVolTransform(),
                     name='applyVolTrans_complete_mask')

# Binarize -  binarize brainmask.mgz an image to create a brainmask
binarizebrainmask = Node(Binarize(min=0.5,
                         out_type='nii'),
                name='binarizebrainmask')

# Dilate node - dilates the binary brain mask
dilate_brain_mask = Node(Binarize(dilate=1,
                          min=0.5),
              name='dilate_brain_mask')

# Dilate node - dilates the binary brain mask
dilate_cortical_mask = Node(Binarize(dilate=1,
                          min=0.5),
              name='dilate_cortical_mask')

# Dilate node - dilates the binary brain mask
dilate_complete_mask = Node(Binarize(dilate=1,
                          min=0.5),
              name='dilate_complete_mask')

# MRIConvert - to unzip output files
mriconvert_cortical_mask = Node(MRIConvert(out_type='nii'),
                     name='mriconvert_cortical_mask')

# MRIConvert - to unzip output files
mriconvert_brain_mask = Node(MRIConvert(out_type='nii'),
                     name='mriconvert_brain_mask')

# MRIConvert - to unzip output files
mriconvert_complete_mask = Node(MRIConvert(out_type='nii'),
                     name='mriconvert_complete_mask')

# Binarize Dialte node - binarizes dilated mask again after transformation
binarizeDilatedCorticalMask = Node(Binarize(min=0.1, binary_file='dilated_cortical_mask.nii'),
                           name='binarizeDilatedCorticalMask')

# Binarize Dialte node - binarizes dilated mask again after transformation
binarizeDilatedBrainMask = Node(Binarize(min=0.1, binary_file='dilated_brain_mask.nii'),
                           name='binarizeDilatedBrainMask')

# Binarize Dialte node - binarizes dilated mask again after transformation
binarizeDilatedCompleteMask = Node(Binarize(min=0.1, binary_file='dilated_complete_mask.nii'),
                           name='binarizeDilatedCompleteMask')

applyVolTrans_cortical_mask = Node(ApplyVolTransform(reg_header=True,
                                  interp='nearest'),
                name='applyVolTrans_cortical_mask')

applyVolTrans_brain_mask = Node(ApplyVolTransform(reg_header=True,
                                  interp='nearest'),
                name='applyVolTrans_brain_mask')

applyVolTrans_complete_mask = Node(ApplyVolTransform(reg_header=True,
                                  interp='nearest'),
                name='applyVolTrans_complete_mask')

aparc_robust_BET_mask = MapNode(interface=ImageMaths(suffix='_ribbon_robust_BET',
                                               op_string='-mas', output_type='NIFTI', out_file='aparc_robust_BET.nii'),
                      iterfield=['in_file'],
                      name='aparc_robust_BET_mask')

# Create the mask pipeline
preproc_ALPACA_maskflow = Workflow(name='prepro_ALPACA_maskflow')

# Connect all components of the preprocessing workflow - aparc / ribbon mask 
preproc_ALPACA_maskflow.connect([(realign, meanfuncmask, [('mean_image', 'in_file')]), # create a skull stripped mask image from the mean functional
                 (binarizebrainmask, mriconvert_brain_mask, [('binary_file', 'in_file')]), # convert brainmask to nifti
                 (mriconvert_brain_mask, applyVolTrans_brain_mask, [('out_file', 'source_file')]), # transform brainmask to functional space
                 (realign, applyVolTrans_brain_mask, [('mean_image', 'target_file')]),
                 (applyVolTrans_brain_mask, dilate_brain_mask, [('transformed_file', 'in_file')]), # dilate transformed brainmask
                 (dilate_brain_mask, binarizeDilatedBrainMask, [('binary_file', 'in_file')]), # binarize dilated and transformed brainmask
                 (binarizeCortical, wholebrainmask, [('binary_file','in_file')]),
                 (binarizeSubcortical, wholebrainmask, [('binary_file', 'operand_file')]), # combine aparc_aseg and ribbon files to get a whole brain mask
                 (binarizeCortical, mriconvert_cortical_mask, [('binary_file', 'in_file')]), # convert ribbon file (cortical mask) to nifti
                 (mriconvert_cortical_mask, applyVolTrans_cortical_mask, [('out_file', 'source_file')]), # transform ribbon file (cortical mask) to functional space
                 (realign, applyVolTrans_cortical_mask, [('mean_image', 'target_file')]),
                 (applyVolTrans_cortical_mask, dilate_cortical_mask, [('transformed_file', 'in_file')]), # dilate transformed ribbon file (cortical mask)
                 (dilate_cortical_mask, binarizeDilatedCorticalMask, [('binary_file', 'in_file')]), # binarize dilated and transformed ribbon file (cortical mask)
                 (meanfuncmask, aparc_robust_BET_mask, [('mask_file', 'in_file')]), # create a combined mask from ribbon file (cortical mask) and robust_BET mask
                 (binarizeDilatedCorticalMask, aparc_robust_BET_mask, [('binary_file', 'in_file2')]),
                 (wholebrainmask, mriconvert_complete_mask, [('out_file', 'in_file')]), # convert whole brain mask to nifti
                 (mriconvert_complete_mask, applyVolTrans_complete_mask, [('out_file', 'source_file')]), # transform complete mask to functional space
                 (realign, applyVolTrans_complete_mask, [('mean_image', 'target_file')]),
                 (applyVolTrans_complete_mask, dilate_complete_mask, [('transformed_file', 'in_file')]), # dilate transformed whole brain mask
                 (dilate_complete_mask, binarizeDilatedCompleteMask, [('binary_file', 'in_file')]), # binarize dilated and transformed whole brain mask
                 ])
       
##### Specify input and output stream #####

# Infosource - a function free node to iterate over the list of subject names
infosource = Node(IdentityInterface(fields=['subject_id']),
                  name="infosource")
infosource.iterables = [('subject_id', subject_list)]

# SelectFiles - to grab the data (alternativ to DataGrabber)
templates = {'func': '{subject_id}/func/sub*.nii.gz',
             'aparc_aseg': 'derivatives/mindboggle/freesurfer_subjects/{subject_id}/mri/aparc+aseg.mgz',
             'brainmask': 'derivatives/mindboggle/freesurfer_subjects/{subject_id}/mri/brainmask.mgz',
             'ribbon': 'derivatives/mindboggle/freesurfer_subjects/{subject_id}/mri/ribbon.mgz'}
selectfiles = Node(SelectFiles(templates,
                               base_directory=experiment_dir),
                   name="selectfiles")
       
# Datasink - creates output folder for important outputs
datasink = Node(DataSink(base_directory=experiment_dir,
                         container=output_dir),
                name="datasink")

# Use the following DataSink output substitutions
substitutions = [('_subject_id_', ''),
                 ('_detrended', ''),
                 ('_warped', '')]
datasink.inputs.substitutions = substitutions

### create the main pipeline
prepro_ALPACA=Workflow(name='prepro_ALPACA')

##### establish input and output streams by connecting Infosource, SelectFiles and DataSink to the main workflow #####
preproc_ALPACA.connect([(infosource, selectfiles, [('subject_id', 'subject_id')]),
                  (infosource, preproc_ALPACA_base, [('subject_id', 'bbregister.subject_id')]),
                  (selectfiles, preproc_ALPACA_base, [('func', 'gunzip.in_file')]),
                  (selectfiles, preproc_ALPACA_maskflow, [('aparc_aseg', 'binarizeSubcortical.in_file')]),
                  (selectfiles, preproc_ALPACA_maskflow, [('ribbon', 'binarizeCortical.in_file')]),
                  (selectfiles, preproc_ALPACA_maskflow, [('brainmask', 'binarizebrainmask.in_file')]),
                  (preproc_ALPACA_base, preproc_ALPACA_MVPA, [('realign.out_file', 'despike.in_file')]),
                  (preproc_ALPACA_base, preproc_ALPACA_MVPA, [('bbregister.out_reg_file', 'applyVolReg.reg_file')]),
                  (preproc_ALPACA_MVPA, volume_flow, [('zstandardize.out_file', 'concatVol.in_files')]),
                  (preproc_ALPACA_MVPA, surface_flow, [('zstandardize.out_file', 'samplerLH.source_file'),
                                                       ('zstandardize.out_file', 'samplerRH.source_file'),
                                                       ('bbregister.out_reg_file', 'samplerLH.reg_file'),
                                                       ('bbregister.out_reg_file', 'samplerRH.reg_file')]),
                  (preproc_ALPACA_base, datasink, [('art.plot_files', 'art.@plot'),
                                                   ('art.outlier_files', 'art.@stat')]),
                  (preproc_ALPACA_maskflow, datasink, [('binarizeDilatedCorticalMask.binary_file', 'masks.@binarized_dilated_cortical_mask'),
                                                       ('binarizeDilatedBrainMask.binary_file', 'masks.@binarized_dilated_brain_mask')]),
                                                       ('binarizeDilatedCompleteMask.binary_file', 'masks.@binarized_dilated_complete_mask'),
                                                       ('meanfuncmask. mask_file', 'masks.@mean_func_mask'),
                                                       ('aparc_robust_BET_mask.out_file', 'masks.@aparc_robust_BET_mask'),
                  (volume_flow, datasink, [('concatVol.concatenated_file', 'volumes')]),
                  (surface_flow, datasink, [('mriconvertSurfLH.out_file', 'surfaces_lh'),
                                            ('mriconvertSurfRH.out_file', 'surfaces_rh')]),
                  (preproc_ALPACA_base, datasink, [('realign.mean_image', 'realign.@mean'),
                                                   ('realign.realignment_parameters', 'realign.@parameters')]),
                  (preproc_ALPACA_base, datasink, [('art.outlier_files', 'art.@outliers'),
                                                   ('art.plot_files', 'art.@plot')]),
                  (preproc_ALPACA_base, datasink, [('bbregister.out_reg_file', 'bbregister.@out_reg_file'),
                                                   ('bbregister.out_fsl_file', 'bbregister.@out_fsl_file'),
                                                   ('bbregister.registered_file', 'bbregister.@registered_file')]),
                  (preproc_ALPACA_base, datasink, [('smooth.smoothed_files', 'smooth.@smoothed_files')]),
                  ])

#### visualize the pipeline ####

# Create a colored pipeline graph
preproc_ALPACA.write_graph(graph2use='colored',format='png', simple_form=True)

# Create a detailed pipeline graph
preproc_ALPACA.write_graph(graph2use='flat',format='png', simple_form=True)

#### run the workflow using multiple cores ####
preproc_ALPACA.run('MultiProc', plugin_args={'n_procs':4})
