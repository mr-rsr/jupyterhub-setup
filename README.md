# JupyterHub Iframe Integration

This setup provides The Littlest JupyterHub with automatic user provisioning and iframe embedding capabilities.

## Features

- **Automatic User Provisioning**: Creates system users on-demand
- **Iframe Embedding**: Direct JupyterLab access without login screens
- **Persistent Storage**: User notebooks persist across sessions
- **URL-based Authentication**: Pass username via URL parameter

## Installation

1. **Run on Ubuntu/Debian VM**:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

2. **Manual Installation**:
   ```bash
   # Install TLJH
   curl -L https://tljh.jupyter.org/bootstrap.py | sudo python3 - --admin admin
   
   # Copy config files
   sudo cp jupyterhub_config.py /opt/tljh/config/
   sudo cp url_authenticator.py /opt/tljh/config/
   
   # Restart service
   sudo systemctl restart jupyterhub
   ```

## Usage

### Iframe Integration

Use this URL format in your iframe:
```
http://your-server:8000/auto-login/USERNAME
```

### Example Integration

```html
<iframe src="http://localhost:8000/auto-login/alice" 
        width="100%" height="600px"></iframe>
```

### JavaScript Integration

```javascript
function loadUserNotebook(username) {
    const iframe = document.getElementById('jupyter-frame');
    iframe.src = `http://your-server:8000/auto-login/${username}`;
}
```

## Configuration

- **Server URL**: Modify `c.JupyterHub.bind_url` in `jupyterhub_config.py`
- **Admin Users**: Update `c.Authenticator.admin_users`
- **HTTPS**: Set `Secure: True` in cookie options for production

## Security Notes

- Use HTTPS in production
- Implement proper user validation in your frontend
- Consider network isolation for the JupyterHub VM
- Regular security updates for the system

## Troubleshooting

- Check logs: `sudo journalctl -u jupyterhub -f`
- Restart service: `sudo systemctl restart jupyterhub`
- Verify config: `sudo /opt/tljh/hub/bin/jupyterhub --config=/opt/tljh/config/jupyterhub_config.py --dry-run`