import sys
sys.path.insert(0, '/opt/tljh/config/jupyterhub_config.d')
from url_authenticator import URLAuthenticator

c.JupyterHub.authenticator_class = URLAuthenticator
c.JupyterHub.bind_url = 'http://0.0.0.0:8000'
c.Authenticator.admin_users = {'admin'}
c.Authenticator.allow_all = True

# TLJH Spawner settings
c.SystemdSpawner.default_url = '/lab'
c.SystemdSpawner.unit_name_template = 'jupyter-{USERNAME}'
c.SystemdSpawner.start_timeout = 60
c.SystemdSpawner.http_timeout = 30

# Hub iframe support
c.JupyterHub.tornado_settings = {'headers': {'Content-Security-Policy': "frame-ancestors *;"}}
c.JupyterHub.cookie_options = {'SameSite': 'None', 'Secure': False}

# Disable CSP reporting
c.JupyterHub.extra_handlers = []

# Single-user server iframe support
c.Spawner.cmd = ['jupyter-labhub']
c.Spawner.default_url = '/lab'
c.Spawner.args = ['--ServerApp.allow_origin=*', '--ServerApp.disable_check_xsrf=True', '--config=/opt/tljh/config/jupyter_server_config.py']
c.Spawner.environment = {
    'JUPYTER_CONFIG_DIR': '/opt/tljh/config'
}