import sys
import os
sys.path.insert(0, '/opt/tljh/config/jupyterhub_config.d')
from url_authenticator import URLAuthenticator

# --- Authenticator Settings ---
c.JupyterHub.authenticator_class = URLAuthenticator
c.JupyterHub.bind_url = 'http://0.0.0.0:8000'
c.Authenticator.admin_users = {'admin'}
c.Authenticator.allow_all = True

# --- Hub & Proxy Settings ---
c.JupyterHub.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' http://lab.enterprisesi.co https://lab.enterprisesi.co",
        'X-Frame-Options': 'ALLOWALL',
    }
}

c.JupyterHub.cookie_options = {'SameSite': 'Lax', 'Secure': False}

c.ConfigurableHTTPProxy.command = [
    'configurable-http-proxy',
    '--unauthenticated-csp-header=frame-ancestors \'self\' http://lab.enterprisesi.co https://lab.enterprisesi.co'
]

# --- Spawner Settings ---
c.SystemdSpawner.default_url = '/lab'
c.SystemdSpawner.unit_name_template = 'jupyter-{USERNAME}'
c.SystemdSpawner.start_timeout = 60
c.SystemdSpawner.http_timeout = 30

# Environment variables for the single-user server
c.SystemdSpawner.environment = {
    'JUPYTERHUB_DISABLE_USER_CONFIG': '0',
}


# Double-brace formatting for JSON strings
c.SystemdSpawner.args = [
    '--ServerApp.tornado_settings={{"headers":{{"Content-Security-Policy":"frame-ancestors \'self\' http://lab.enterprisesi.co https://lab.enterprisesi.co","X-Frame-Options":"ALLOWALL"}}}}',
    '--ServerApp.allow_origin=*',
    '--ServerApp.disable_check_xsrf=True',
    '--NotebookApp.tornado_settings={{"headers":{{"Content-Security-Policy":"frame-ancestors \'self\' http://lab.enterprisesi.co https://lab.enterprisesi.co","X-Frame-Options":"ALLOWALL"}}}}',
    '--NotebookApp.allow_origin=*',
    '--NotebookApp.disable_check_xsrf=True',
]

# --- Pre-spawn hook to fix the Permission Denied Error ---
def pre_spawn_hook(spawner):
    username = spawner.user.name
    # Define home-based paths so users have write access
    user_home = f'/home/jupyter-{username}'
    workspace_path = os.path.join(user_home, '.jupyter/lab/workspaces')
    settings_path = os.path.join(user_home, '.jupyter/lab/settings')
    
    # Create directories if they don't exist
    os.makedirs(workspace_path, exist_ok=True, mode=0o755)
    os.makedirs(settings_path, exist_ok=True, mode=0o755)
    
    # Inject paths into environment
    spawner.env['JUPYTERLAB_WORKSPACES_DIR'] = workspace_path
    spawner.env['JUPYTERLAB_SETTINGS_DIR'] = settings_path

c.SystemdSpawner.pre_spawn_hook = pre_spawn_hook