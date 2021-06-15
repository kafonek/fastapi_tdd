FROM jupyter/minimal-notebook:latest

COPY ./requirements.txt /tmp/requirements.txt

RUN python -m pip install \
    --no-cache-dir \
    --disable-pip-version-check \
    -r /tmp/requirements.txt

RUN jupyter contrib nbextension install --user

COPY ./config/jupyter_notebook_config.py /opt/conda/etc/jupyter/jupyter_notebook_config.py
COPY ./config/notebook.json /opt/conda/etc/jupyter/nbconfig/notebook.json
COPY ./config/vimrc.local /etc/vim/vimrc.local