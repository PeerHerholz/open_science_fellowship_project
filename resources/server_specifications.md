# specifications of the "open and reproducible neuroscience" server

Here you'll find some information about the "open and reproducible neuroscience" server I'm setting up and why I'm doing it.

## background
Starting my [open science fellowship](https://en.wikiversity.org/wiki/Wikimedia_Deutschland/Open_Science_Fellows_Program) [application](https://de.wikiversity.org/wiki/Wikiversity:Fellow-Programm_Freies_Wissen/Einreichungen/ALPACA_–_Automated_Labelling_and_Parcellation_of_Auditory_Cortex_Areas) I realized, that the setup I'm using at the [institute in Marburg](http://www.ukgm.de/ugm_2/deu/umr_psy/6618.html) isn't suited for a broader use, in terms of computational power, storage and especially accessibility I decided to also include a working package that solely focuses on setting up a completely new server system that uses nothing but open source software and supports all tools necessary for "open and reproducible neuroscience". Is that really a big thingy, you ask? Well, yup! The last couple of years I, more or less, builed my own setup of machines and networks. This was necessary as the old/default server systems covered something around 10 % of all (free and open source) software I needed, couldn't easily be changed in that way, I (of course) didn't get admin privileges and most of all: people didn't care. The problem with building a setup yourself is that I nearly paid everything myself (because no one needed or used the stuff I did, or planned to do so in the future) and hence, tailored it specifically to my needs. One further problem resulting from the first point is that I could only afford rather small machines that maybe work well with 3-5 peeps working on them, but not more. The same accounts for the network. As I was granted the chance to reuse some old emitted server systems from the university's IT for free, I decided to take a leap of faith (having degrees in neuropsychology & neuroscince, never receiving formal training in anything related to computers) and setup / build a completely new server system from scratch, supported by the financial resources that I would receive throug the fellowship in case of an successfull application (being small things like network switches, pay myself, etc.). As the open science gods had mercy, I received the fellowship, actually starting with the server system right away. 

## inspiration and motivation
My inspiration and motivation to do this was/is based on pure need of certain software and system settings, enabling state of the art methods and (I know this sounds cheesy) basically doing the right thing making "open and reproducible neuroscience" at the institute at least possible. Experiencing major repercussions in the beginning, combined with my lack of knowledge, made my question my beliefs and plans, but after my time in Montréal, working with amazing people in great institutes like [The Neuro](https://www.mcgill.ca/neuro/) and seeing that open science actually can work incredibly well at an insitutional level, I decided to just go for it.

## current specifications

- 
- [Ubuntu Server 16.04.3 LTS](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes?_ga=2.7141170.1278724334.1510490510-1361653877.1510490510)
- [git](https://git-scm.com)
- [docker](https://www.docker.com), including the following containers 
   - [FMRIPREP](http://fmriprep.readthedocs.io/en/stable/index.html)
   - [MRIQC](http://mriqc.readthedocs.io/en/stable/)
   - [mindboggle](http://www.mindboggle.info)
   - [C-PAC](https://fcp-indi.github.io)
   - [nipype](http://nipype.readthedocs.io/en/latest/)
   - [neurodocker](https://hub.docker.com/r/kaczmarj/neurodocker/)
- [singularity](http://singularity.lbl.gov)
- [Anaconda distribution version 5.0.1](https://www.anaconda.com), for both [Python 2.7 & 3.6](www.anaconda.com/download/)
  - not listing all python packages here, because there just too many, but the server got you covered with nearly everything from the neuroimaging in python world ([nibabel](http://nipy.org/nibabel/), [nilearn](http://nilearn.github.io/index.html), [nipype](http://nipype.readthedocs.io/en/latest/), [mne](https://martinos.org/mne/stable/index.html), [dipy](http://nipy.org/dipy/), [datalad](http://datalad.org) etc.)
- [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki)
- [FreeSurfer](https://surfer.nmr.mgh.harvard.edu)
- [AFNI](https://afni.nimh.nih.gov)
- [ANTs](http://stnava.github.io/ANTs/)
- [SPM (standalone)](https://en.wikibooks.org/wiki/SPM/Standalone)
- [Neurodebian repo](http://neuro.debian.net)
- [connectome workbench](https://www.humanconnectome.org/software/connectome-workbench)
- [dsi studio](http://dsi-studio.labsolver.org)
- [mricron](https://www.nitrc.org/projects/mricron)
- [mango](http://ric.uthscsa.edu/mango/)
- [itk-snap](http://www.itksnap.org/pmwiki/pmwiki.php)
- [spyder](https://pythonhosted.org/spyder/index.html)
- [pycharm](https://www.jetbrains.com/pycharm/)
- [rstudio](https://www.rstudio.com)
- [sublime](https://www.sublimetext.com)
- [atom](https://atom.io)
- [octave](https://www.gnu.org/software/octave/)
- [psychopy](http://www.psychopy.org)
- [opensesame](http://osdoc.cogsci.nl)
- [pygaze](http://www.pygaze.org)


