#!/bin/bash

docker run -it -u $(id -u):$(id -g) \
	--gpus all -p 8888:8888 \
	-v "${HOME}/.config/jupyter:/.jupyter" \
	-v "${HOME}/workspace/deep_learning:/notebooks" \
	tensorflow/tensorflow:latest-gpu-jupyter \
	bash -c "source /etc/bash.bashrc && jupyter notebook --notebook-dir=/notebooks --ip 0.0.0.0 --no-browser --NotebookApp.allow_origin='https://colab.research.google.com'"

