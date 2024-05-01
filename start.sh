#!/bin/bash
sudo apt-get update 
sudo su
apt install docker.io -y
docker run -d -p 8080:8000 --name revhire abinash8/myrepo:lts
git clone https://github.com/Abinashkhuntia/revhire.git 
cd revhire

# ubtuntu does not come with python3-pip pre-installed and not allowed me to install without venv
apt install python3-pip -y
apt install python3.12-venv -y

python3 -m venv myenv
source myenv/bin/activate
pip install fastapi uvicorn jwt

# sudo pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 
# run the server
