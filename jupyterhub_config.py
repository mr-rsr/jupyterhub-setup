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

# Iframe support
c.JupyterHub.tornado_settings = {
    'headers': {'Content-Security-Policy': "frame-ancestors 'self' *"}
}
c.JupyterHub.cookie_options = {'SameSite': 'None', 'Secure': False}