from jupyter_core.paths import jupyter_data_dir

c = get_config()
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = True
c.NotebookApp.token = ''
c.NotebookApp.password = ''
