# ZHAW CAS Foundations of AI and Machine Learning

# Module: Deep Learning (Fall Term 2026)

The notebooks use **Keras 3** with the **PyTorch backend**.

# Setup Instructions

## Versions required

	Python 3.12
	Keras 3.15.1
	PyTorch 2.14.1
	torchvision 0.29.1
	CUDA 13.2 (GPU only, comes with PyTorch)
	scikit-image 0.26.0
	scikit-learn 1.9.1
	numpy 2.5.5

TensorFlow is not needed.

## Install Miniforge (recommended)

We recommend [Miniforge](https://github.com/conda-forge/miniforge) as the conda distribution. It is a minimal installer that uses the community-driven conda-forge channel by default and includes `conda` and `mamba`. If you already have a working conda installation, you can skip this step.

**Windows:** download and run the installer [Miniforge3-Windows-x86_64.exe](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe). Afterwards, open the "Miniforge Prompt" from the Start menu and run the commands below there.

To use `conda` in a normal PowerShell or the VS Code terminal as well, run once in the Miniforge Prompt

	conda init powershell

and open a new terminal. If you use Git Bash, run `conda init bash` instead. (Do not tick "Add Miniforge3 to my PATH" in the installer; `conda init` is the recommended way.)

**Linux / macOS:** run in a terminal

	curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
	bash Miniforge3-$(uname)-$(uname -m).sh

Accept the defaults, answer "yes" when asked to initialize conda, then open a new terminal. If you answered "no", run `~/miniforge3/bin/conda init` (for zsh, the default on macOS: `~/miniforge3/bin/conda init zsh`) and open a new terminal. On macOS, `brew install miniforge` works as well.

Check the installation with

	conda --version

## Automatic Environment Setup

### CPU

	conda env create -f env.yaml

This creates the conda environment "cas_main_dl" and installs the packages listed in "env.yaml" (CPU only). This also works on macOS 14 (Sonoma) or newer with Apple Silicon.

### GPU (NVIDIA)

	conda env create -f env_gpu.yaml

This creates the conda environment "cas_main_dl_gpu" with PyTorch for CUDA 13.2. The CUDA and cuDNN libraries come with the PyTorch packages, so you only need a recent NVIDIA driver (version 595 or newer). Check your driver version with `nvidia-smi`. This works on Linux and on native Windows (WSL2 is not required).

Check that the GPU is found:

	python -c "import torch; print(torch.cuda.is_available())"

### Manual Setup

	# create and activate env
	conda create -n cas_main_dl python=3.12
	conda activate cas_main_dl

	# Install PyTorch
	# Either: GPU (CUDA 13.2)
	pip install torch==2.14.1 torchvision==0.29.1 --index-url https://download.pytorch.org/whl/cu132
	# Or: CPU (on macOS, omit --index-url)
	pip install torch==2.14.1 torchvision==0.29.1 --index-url https://download.pytorch.org/whl/cpu

	# install Keras and other packages (check versions above)
	pip install keras==3.15.1 tensorboard notebook matplotlib pandas tqdm ipywidgets scikit-learn scikit-image wget gdown opencv-python

Official PyTorch installation instructions: https://pytorch.org/get-started/locally/

## Keras backend

Keras 3 runs on top of PyTorch, TensorFlow or JAX. The backend is selected with the environment variable `KERAS_BACKEND`, which must be set **before** `keras` is imported. Each notebook does this in its first code cell:

	import os
	os.environ["KERAS_BACKEND"] = "torch"
	import keras

If you change the backend, restart the kernel. Without this variable, Keras falls back to TensorFlow and fails to import if TensorFlow is not installed.

## Run directly in Colab

In the Notebook, click on this link to open it in Colab directly: ![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)

Or, if you have forked the repository, you can run a notebook directly in Google Colab by using a link like this:

https://colab.research.google.com/github/(YOUR_GITHUB_ID)/cas_main_dl_2026/blob/master/01_mnist.ipynb

Colab comes with PyTorch and Keras 3 preinstalled. Since the backend is set in the first cell of each notebook, no further setup is needed.
