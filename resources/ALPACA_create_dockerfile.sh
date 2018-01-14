

# Generate Dockerfile.
docker run --rm kaczmarj/neurodocker:master generate \
--base debian:stretch --pkg-manager apt \
--afni version=latest \
--ants version=2.2.0 \
--c3d version=1.0.0 \
--dcm2niix version=latest \
--freesurfer version=6.0.0 min=true \
--fsl version=5.0.10 \
--user alpaca \
--miniconda env_name=alpaca \
            conda_opts="--channel vida-nyu" \
            conda_install="python=3.6 numpy pandas  traits jupyter jupyterlab pandas matplotlib scikit-learn seaborn altair traitsui apptools configobj reprozip reprounzip vtk jupyter_contrib_nbextensions" \
            pip_install="nipype mne mayavi nilearn datalad ipywidgets pythreejs nibabel" \
            activate=true \
--miniconda env_name=alpaca \
            pip_install="pylsl" \
--miniconda env_name=py27 \
            conda_install="python=2.7" \
--user root \
--mrtrix3 \
--neurodebian os_codename="stretch" \
              download_server="usa-nh" \
              pkgs="dcm2niix git-annex-standalone" \
--install git vim \
--user alpaca \
--workdir /home/alpaca \
--no-check-urls > /Users/peerherholz/google_drive/ALPACA/docker_files/generated-full.Dockerfile

# Build Docker image using the saved Dockerfile.
docker build -t alpaca -f generated-full.Dockerfile /Users/peerherholz/google_drive/ALPACA/




