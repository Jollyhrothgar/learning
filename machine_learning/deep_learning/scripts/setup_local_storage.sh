docker run -ti --gpus all --rm -u $(id -u):$(id -g) \
	-v "${HOME}/.config/jupyter:/.jupyter" \
	tensorflow/tensorflow:latest-gpu-jupyter \
	bash -c "source /etc/bash.bashrc && jupyter serverextension enable --py jupyter_http_over_ws"

