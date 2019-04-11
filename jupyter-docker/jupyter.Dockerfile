FROM jupyter/base-notebook

USER $NB_USER

COPY jupyter_notebook_config.py /home/$NB_USER/.jupyter/
