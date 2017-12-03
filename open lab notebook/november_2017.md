# October 30th - November 5th, 2017
## this week
- continued working on the workshop hp (check the repo [here](https://github.com/PeerHerholz/openreproneuro2018marburg.github.io))
- started server setup, check the current specifications [here](https://github.com/PeerHerholz/open_science_fellowship_project/blob/master/resources/server_specifications.md)

  
## next week

- continue the server setup
- finish and check jupyter notebook based seminars for an open
  and reproducible education
- search for computational models concerning hearing implemented in python 


# November 6th - 12th, 2017
## this week
- continued server setup
- jupyter notebooks work on the new server system and
  are used in the course ["mri in cognitive neuroscience - an answer to physics,
  statistics and all the rest"](https://qis.verwaltung.uni-marburg.de/qisserver/rds?state=verpublish&status=init&vmfile=no&publishid=168320&moduleCall=webInfo&publishConfFile=webInfo&publishSubDir=veranstaltung&noDBAction=y&init=y)
- found a nice [github repo](https://github.com/faroit/awesome-python-scientific-audio), more precisely a collection of scientific audio related python projects
  - it includes a section on [perceptual models](https://github.com/faroit/awesome-python-scientific-audio#perceptial-models---auditory-models)
  - through that I found two very interested and open packages that I plan to use in the project: [cochlea](https://github.com/mrkrd/cochlea) and [DSAM](http://dsam.org.uk)

## next week
- more server setup fun
- a lot of organizational work
- check for free and open accessible data of previous studies on the auditory cortex, especially
  [regions of interest masks](http://mindhive.mit.edu/node/101)

# November 13th - 19th, 2017

## this week
- truly happy to announce that through the support of the fellowship, colleagues/friends and I launched  
  the ´["open science initiative university of marburg"](https://openscienceinitiativeuniversitymarburg.github.io/osium.github.io/)
  - it's an university wide initiative fostering the perception and implemenation of the [open science principles](https://en.wikipedia.org/wiki/Open_science)
  - we already established a collaboration with the ["research data management"](https://www.uni-marburg.de/projekte/forschungsdaten/fodaenglisch?set_language=en)
  - the whole team went to this years [MARA day](https://www.uni-marburg.de/mara/veranstaltungen/maraday/maraday2017/maraday2017-programm.pdf) which also featured an open science roundtable
    - we met a lot of fun, interesting and motivated people talking about their projects, our initiative and we how we could
      work together
  - check out our [website](https://openscienceinitiativeuniversitymarburg.github.io/osium.github.io/) and get in touch
- server's looking good and seems to work properly (at least the stuff I briefly tested), now it's about setting profiles,
  etc. to enable people to efficiently use it
- found some amazing region of interest masks which are freely available and open accessible [here](http://web.mit.edu/svnh/www/Resolvability/ROIs.html)
  - they were made available by [sam norman-haignere](http://web.mit.edu/svnh/www/homepage/Research.html) who did a lot of 
    fantastic work in the realm of auditory neuroscience
  - more precisely they include [volume (in .nii)](https://brainder.org/2012/09/23/the-nifti-file-format/) and [surface (in .label)](https://surfer.nmr.mgh.harvard.edu/fswiki/LabelsClutsAnnotationFiles) files in [two versions](http://web.mit.edu/svnh/www/ResolvabilityFigures/Figure_4.html)
  - the regions are part of a [paper](https://doi.org/10.1523/JNEUROSCI.2880-13.2013) Sam published, in which he compared different parcellations and their responses to pitch
    - the "classic" ones are based on probabilistic volume maps ([Morosan et al., 2001](https://doi.org/10.1006/nimg.2000.0715); [Desikan et al., 2006](https://doi.org/10.1016/j.neuroimage.2006.01.021)) 
    - the "new" ones are based on ["along the posterior-to-anterior axis of the superior temporal plane, and to each include an equal number of sound-responsive voxels"](http://web.mit.edu/svnh/www/ResolvabilityFigures/Figure_4.html)
  - the plan is to write a [nipype](http://nipype.readthedocs.io/en/latest/#) pipeline to transform the regions (both parcellations and both file types) from the [MNI305 reference space](http://nist.mni.mcgill.ca/?p=957) to the native participant space

## next week
- further organizational work, connecting with more people around the university
- start writing anatomical processing pipeline

# November 20th - 26th, 2017

## this week
- started working on a anatomical processing pipeline in [nipype](http://nipype.readthedocs.io/en/latest/#)
  - it'll mainly include stuff from [FreeSurfer](https://surfer.nmr.mgh.harvard.edu), [ANTs](http://stnava.github.io/ANTs/)
- a lot of conversations and discussions regarding our [open science initiative](https://openscienceinitiativeuniversitymarburg.github.io/osium.github.io/)
- cloned the current server setup and copied it to another one, so that folks can work on two sun server systems running
  ubuntu server
  - as the current setup is limited to 16 cores, I'll upgrade the whole thingy to a system with 64 cores in mid December  

## next week
- more work on anatomical processing pipeline
- create user accounts for the folks and let them run some tests
- meetings with the psychology & linguistics department regarding the open science initiative

# November 27th - Dezember 3rd, 2017

## this week
- continued work on anatomical processing pipeline, the [volume](https://brainder.org/2012/09/23/the-nifti-file-format/) stream works fine
   - while working on the anatomical processing pipeline, I found a possible bug in [nipype's](http://nipype.readthedocs.io/en/latest/) [label2label](https://surfer.nmr.mgh.harvard.edu/fswiki/mri_label2label) [interface](http://nipype.readthedocs.io/en/0.12.0/interfaces/generated/nipype.interfaces.freesurfer.model.html#label2label) <br/>
   &rarr; I asked about it on [neurostars.org](https://neurostars.org/t/possible-bug-nipype-freesurfer-label2label/991) and opened an issue on [the nipype github page](https://github.com/nipy/nipype/issues/2310)
- created additional user profiles for some colleagues and started some tests (e.g. [mindboggle](http://www.mindboggle.info) outside and inside a docker container) that are still running/being evaluated 
- unfortunately didn't manage to arrange a meeting with the psychology & linguistics department 

## next week
- try to find a workaround regarding the pipeline errors
- include more anatomical masks from different atlases within the anatomical processing pipeline
- meetings with psychology & linguistics department, additionally with the mathematics / computer science department
