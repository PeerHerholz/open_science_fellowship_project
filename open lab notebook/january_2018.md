# January 1st - 7th, 2018
## this week
- more meetings wrt ethics proposal & MRI costs 
- started playing around with docker image creation and testing
- more work on the open source server
- start working on [automatic BIDS conversion](https://github.com/nipy/heudiconv) of dicom data on the open science server 
- more work on interim report
- started planning a talk with [Felix](https://github.com/Felix11H), also an open science fellow, where he'll present
his project and we'll give a short workshop on docker
  
## next week
- finish interim report
- upload more tutorials

# January 8th - 14th, 2018
## this week
- more meetings with different departments wrt our [open science initiative](https://openscienceinitiativeuniversitymarburg.github.io)
- it's planned that [José](https://github.com/JoseAlanis) will give a talk at the psychology department
at the 29th
- finished interim report and uploaded it to [github](https://github.com/PeerHerholz/open_science_fellowship_project/blob/master/open%20lab%20notebook/ALPACA_Zwischenbericht.md)
and the [project's wikiversity site](https://de.wikiversity.org/wiki/Wikiversity:Fellow-Programm_Freies_Wissen/Einreichungen/ALPACA_–_Automated_Labelling_and_Parcellation_of_Auditory_Cortex_Areas/Zwischenbericht)
- uploaded first half of pre-analyses tutorial, which deals with data structure and prerequisites, check it [here](https://github.com/PeerHerholz/open_science_fellowship_project/blob/master/resources/ALPACA_data_organization_prerequisites.ipynb) 
- finished the first draft of the ALPACA docker image and pushed it to [dockerhub](https://hub.docker.com/r/peerherholz/alpaca/)
  - as you can see, it's way too heavy, as I included complete software packages and modules from which I intend to only use certain subfunctions &rarr; hence, I'll work on minimizing the docker image
  - you can check the shell script I used to create and build the docker image in my [resources folder](https://github.com/PeerHerholz/open_science_fellowship_project/blob/master/resources/ALPACA_create_dockerfile.sh) &rarr; it uses the amazing [neurodocker](https://hub.docker.com/r/kaczmarj/neurodocker/) and besides rebuilding of ALPACA also allows easy adaption for other docker images
  - I'll upload a jupyter notebook on how to create and build the docker image within the next few days

## next week
- finish the tutorial notebooks
- pipeline for converting and preprocessing files on the new server system 

# January 15th - 21th, 2018

## this week
- starting looking into the pipeline for converting and preprocessing files on the new server system
  - I've to wait for a response from the institute's and university's IT wrt [docker](https://www.docker.com)
  - the pipeline will include:
    - [heudiconv](https://github.com/nipy/heudiconv)
    - [MRIQC](https://mriqc.readthedocs.io/en/latest/index.html)
    - [mindboggle](http://www.mindboggle.info)
    - [fmriprerp](http://fmriprep.readthedocs.io/en/latest/)
- preparing open science talk at psychology department
- more work on the tutorial notebook 

## next week
- preparing lectures
- preparing open science talk
- meeting with ["Stabsstelle Forschungsdatenmanagement"](https://www.uni-marburg.de/projekte/forschungsdaten/projekt/stabsstelle)

# January 21th - 28th, 2018

## this week
- meeting with ["Stabsstelle Forschungsdatenmanagement"](https://www.uni-marburg.de/projekte/forschungsdaten/projekt/stabsstelle)
  - [talk about electronic lab notebooks](https://www.uni-marburg.de/projekte/forschungsdaten/elns)
  - some planning wrt new projects
- work on lectures
  - open educational resources
  - docker images for the course "MRI in cognitive neuroscience - neuroinformatics"
  - jupyter notebooks
- preparing open science talk

## next week


# January 29th - February 4th, 2018
