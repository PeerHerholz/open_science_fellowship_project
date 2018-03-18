# February 5th - 11th, 2018

## this week
- quality control of test measurements
  - measured 4 test participants (all peeps from the lab) with different
    protocols and sequences to test for artifacts that might be related to that
  - run [mriqc](http://mriqc.readthedocs.io/en/latest/index.html) on all images (structural and functional)
  - artifacts are more or less slightly visible
  - [mriqc classifier](http://mriqc.readthedocs.io/en/latest/classifier.html) predicted that no scan needs to be rejected
  - hence, I decided to keep the parameters and headphones
  - as using [mriqc](http://mriqc.readthedocs.io/en/latest/index.html) standardized for all measurements (and provide results openly) was the plan all along, quality control throughout the complete study is guaranteed (and thus possible problems can be tackled) and also hopefully will help others who are planning comparable studies
 - more notebooks
 - work on converter script
  
## next week
- notebooks
- checking [dockerfile and container](https://github.com/PeerHerholz/open_science_fellowship_project/blob/master/resources/ALPACA_create_dockerfile.sh) again
- try to get a final response on how to pay for measurement using the fellowship money
- data storage on new server system
- open science policies at the institute

# February 12th - 18th, 2018

## this week
- talked about data conversion and storage on our new [open neuroscience server system]()
  - I need to get the university IT's final ok for [git](https://git-scm.com) and [docker](https://en.wikipedia.org/wiki/Docker_(software))/[singularity](https://en.wikipedia.org/wiki/Singularity_(operating_system))
    - to get that I need to ensure that the new server system is completely detached from the old/default one
    - hence, the planned automatic data transfer and conversion / processing over night isn't possible
- notebooks
  - started some new ones: 
    - [ALPACA_create_docker.ipynb](https://github.com/PeerHerholz/open_science_fellowship_project/blob/master/resources/ALPACA_create_docker.ipynb) --> how to create and the build the [ALPACA docker container](), together with information on whats in it and why
    - [ALPACA_atlas_to_ROI.ipynb](https://github.com/PeerHerholz/open_science_fellowship_project/blob/master/resources/ALPACA_atlas_to_ROI.ipynb) --> it contains two sections: how to extract (auditory cortex) ROIs from openly available atlases and how to transform ROIs from reference spaces into participant's native space
 - further workshop planning
   - the workshop has it's own [github repository](https://github.com/miykael/workshops/tree/master/180309_marburg) where you check and track the current status and changes

## next week
- notebooks
- server system
- workshop planning  


# February 19th - 25th, 2018

## this week
- more work on notebooks
- current plan regarding the server system: get raw dicoms directly at the scanner and subsequently transfer them manually to the new system, starting the conversion and processing workflow directly there
- workshop preparation (slides, docker image, accommodation, food, rooms, infrastructure, etc.)  

## next week
- workshop preparation
- docker and singularity on the new server system (system wide and user specific)

# February 25th - March 4th, 2018

## this week
- workshop preparation
  - everything infrastucture related set and ready to go
  - more work on slides and docker image
  - rearranging time slots
- reading about docker and singularity server set ups
  - a scheduler like [slurm](https://slurm.schedmd.com) or [kubernetes](https://kubernetes.io)

## next week
- workshop
