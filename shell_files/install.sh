pip3 install virtualenv
virtualenv venv
source venv/bin/activate
sudo apt-get update
pip install -U pip setuptools wheel
pip install -r requirements.txt

# for git push : git push --set-upstream origin small_projects