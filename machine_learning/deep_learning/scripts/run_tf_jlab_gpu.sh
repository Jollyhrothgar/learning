#!/bin/bash

docker run -it -u $(id -u):$(id -g) \
	--gpus all -p 8888:8888 \
	-v "${HOME}/.config/jupyter:/.jupyter" \
	-v "${HOME}/workspace/deep_learning:/notebooks" \
	-v "${HOME}/workspace/deep_learning/notebooks:/tensorflow_datasets" \
	-v "/root/.nvm" \
	tf_gpu_jlab:latest \
	bash -c "source /etc/bash.bashrc && jupyter lab --notebook-dir=/notebooks --ip 0.0.0.0 --no-browser"
