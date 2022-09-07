INSTALLATION

1. git clone https://github.com/akuzmishyn/texts_autoscreen.git
2. cd texts_autoscreen
3. git checkout v2
4. git pull
4. pip install -r requirements.txt (or) pip3 install -r requirements.txt

NOTE: u need have Python 3.9+ version for UI library
If u don't have Python3.9+ version:
1. Download from Python.org python3.9+ version (3.9 - is good)
2. Install brew:
/bin/bash -c “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)”
3. pip install -r requirements.txt (or) pip3 install -r requirements.txt
4. Install UI library:
brew install python-tk@3.9


RUN
1. put game name, branch name, shifts, languages and timings in config.json
2. run in console: **python main.py** (or) **python3 main.py**