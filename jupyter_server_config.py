# Jupyter configuration for iframe support
c.ServerApp.allow_origin = '*'
c.ServerApp.disable_check_xsrf = True
c.NotebookApp.allow_origin = '*'
c.NotebookApp.disable_check_xsrf = True
c.ServerApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors *;"
    }
}

# For older notebook versions
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors *;"
    }
}

# For JupyterLab
c.LabApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors *;"
    }
}