from jupyterhub.auth import Authenticator
from jupyterhub.handlers import BaseHandler
from tornado import web
import pwd
import subprocess

class URLAuthenticator(Authenticator):
    
    def get_handlers(self, app):
        return [(r'/auto-login/([^/]+)', AutoLoginHandler)]
    
    async def authenticate(self, handler, data):
        username = data.get('username')
        if username:
            self.create_system_user(username)
            return {'name': username}
        return None
    
    def create_system_user(self, username):
        try:
            pwd.getpwnam(username)
        except KeyError:
            subprocess.run(['sudo', 'useradd', '-m', username], check=True)

class AutoLoginHandler(BaseHandler):
    
    async def get(self, username):
        user = await self.login_user({'username': username})
        if user:
            self.redirect(f'/hub/spawn/{username}')
        else:
            raise web.HTTPError(403)