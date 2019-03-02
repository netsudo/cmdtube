# Cmdtube - Simple cmdline streaming app

### Installation
Python3, pip and gstreamer is required. After you've installed those you can follow these instructions to get it working in your virtualenv:
```
git clone https://github.com/netsudo/cmdtube.git
cd cmdtube
python3 -m venv env
source env/bin/activate
pip install pipenv
pipenv install
pip install vext vext.gi
python src/main.py
```
Need to work on a better setup, currently pipenv is giving me difficulties installing vext.gi for whichever reason.
