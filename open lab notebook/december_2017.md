# December 4th - December 10th, 2017
## this week
- more work on the structural workflow
  - including more ROIs/ same probabilistic ROIs regarding the auditory system from different atlases <br/>
    &rarr; from [freesurfer](https://surfer.nmr.mgh.harvard.edu) [parcellation](https://surfer.nmr.mgh.harvard.edu/fswiki/CorticalParcellation) <br/>
    &rarr; [Harvard-Oxford-Atlas](http://neuro.debian.net/pkgs/fsl-harvard-oxford-atlases.html) as included in [fsl](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Atlases)<br/>
    &rarr; [BASC](https://figshare.com/articles/basc/1285615) as included in [nilearn](http://nilearn.github.io) <br/>
    &rarr; [Allen 2011](http://mialab.mrn.org/data/index.html) as included in [nilearn](http://nilearn.github.io) <br/>
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- they have a lot of very cool and rare data [freely available online](http://www.brainspan.org/static/atlas?_ga=2.10356337.518479951.1512721284-688602235.1512721284)
- appointments with the [linguistics](https://www.uni-marburg.de/fb09/igs) and [mathematics & computer science department](https://www.uni-marburg.de/fb12/en/index_html?set_language=en) regarding possible collaborations and open science
  
## next week
- finish structural processing pipeline
- create graph for the whole processing pipeline


# December 11th - 17th, 2017
## this week
- didn't manage to finish the structural worklfow, but still made some progress
  - currently working on combining all subworkflows into one
- finally put the website for the ["open & reproducible neuroscience using python" workshop](https://openreproneuro2018marburg.github.io) online
  - this whole thing is part of my fellowship project, as, besides the work on the auditory cortex, I also
    wanted to foster open science in our department/institute and the whole university
  - the workshop is a satellite event of the [60th teap](https://www.teap.de/index.php/teap2018/marburg)
  - it will pass into the first Marburg Brainhack which will take during the conference
- further planning of collaborations on open science
- December, 15th - 19th I'll be back at the [Max-Planck-Institute for Human Cognitive and Brain Sciences](https://www.cbs.mpg.de/en) to attend a [workshop/conference](https://www.cbs.mpg.de/events/11616/3393669) and a [brainhack](https://www.cbs.mpg.de/events/11617/339366)

## next week
- [brainhack](https://www.cbs.mpg.de/events/11617/339366) at [MPI CBS](https://www.cbs.mpg.de/en)
- once again: finish the structural processing pipeline
- upload a jupyter notebook describing how to get different freely available atlases
  and how extract and save certain ROIs 

# December 18th - 24th, 2017

## this week
- amazing [workshop/conference](https://www.cbs.mpg.de/events/11616/3393669) & [brainhack](https://www.cbs.mpg.de/events/11617/339366)
   - slides from nearly every talk can be found [here](https://osf.io/2bcg5/)
   - some pointers from the brainhack presented by [satra](https://github.com/satra) can be found [here](https://github.com/PeerHerholz/open_science_fellowship_project/blob/master/resources/pointers_brainhack_Leipzig_2017.txt) 
- still working on the structural workflow, as I decided to make it more robust and comprehensive 
  - hence I started to write a [jupyter notebook](https://miykael.github.io/nipype_tutorial/notebooks/introduction_jupyter-notebook.html) around the structural workflow which also includes a lot of necessary information wrt data structure and preprocessing
- also extended the atlas to ROI [jupyter notebook](https://miykael.github.io/nipype_tutorial/notebooks/introduction_jupyter-notebook.html) to include a transformation from volume (.nii.gz) to surface (.label)
- happy holidays

## next week
- happy holidays
- as usual: work on pipelines

# December 25th - 31th, 2017

## this week
- happy holidays
- extended the structural pipeline incorporating existing robust (open source) processing workflows and structures 
  - hence, the prerequisites for running the ALPACA structural pipeline are: 
    - as always planned: accept and work with [BIDS](http://bids.neuroimaging.io) as input
    - apply [MRIQC](http://mriqc.readthedocs.io/en/latest/) to check the quality of the data
    - process structural data using the [mindboggle pipeline](http://www.mindboggle.info)
  - till now it's planned that the structural pipeline will build upon the outputs of these processing steps,
    which are also beneficial in a lot of ways: data quality & structure, reproducibility, completely open, etc. 
  - furthermore their processing steps and outputs will also be used within the functional pipeline
  - to enable a flexible application (e.g. if peeps don't want to use these tools) an easy adaptable version will be provided
    later on
- got some more atlases for the atlas to ROI jupyter notebook
- started [interim report](https://de.wikiversity.org/wiki/Wikiversity:Fellow-Programm_Freies_Wissen/Zwischenbericht)

## next week
- happy new year
- finish interim report
