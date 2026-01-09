@echo off
REM Replace with your server details
set SERVER_IP=ec2-65-0-101-106.ap-south-1.compute.amazonaws.com
set SERVER_USER=ubuntu
set KEY_FILE=C:\Users\rajkl\Documents\EnterpriseSI\test-jupyterhub.pem

echo Copying files to server...

REM Copy files using SCP
scp -i "%KEY_FILE%" url_authenticator.py %SERVER_USER%@%SERVER_IP%:/tmp/
scp -i "%KEY_FILE%" jupyterhub_config.py %SERVER_USER%@%SERVER_IP%:/tmp/
scp -i "%KEY_FILE%" jupyter_server_config.py %SERVER_USER%@%SERVER_IP%:/tmp/

echo Installing files on server...

REM SSH to server and install files
ssh -i "%KEY_FILE%" %SERVER_USER%@%SERVER_IP% "sudo cp /tmp/url_authenticator.py /opt/tljh/config/jupyterhub_config.d/ && sudo cp /tmp/jupyterhub_config.py /opt/tljh/config/jupyterhub_config.d/ && sudo cp /tmp/jupyter_server_config.py /opt/tljh/config/ && sudo chown root:root /opt/tljh/config/jupyterhub_config.d/url_authenticator.py && sudo chown root:root /opt/tljh/config/jupyterhub_config.d/jupyterhub_config.py && sudo chown root:root /opt/tljh/config/jupyter_server_config.py && sudo systemctl restart jupyterhub"

echo Deployment complete!
pause