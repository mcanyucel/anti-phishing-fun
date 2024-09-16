## How to use

### Installation
Install the [driver for selenium](https://packages.debian.org/buster/chromium-driver):

```bash
sudo apt install chromium # may already be installed, but just in case
sudo apt install chromium-driver
```

Create a new environment for python

```bash
python -m venv .venv
source .venv/bin/activate
```

### Testing
Use *driver-test.py* to see if the installation is successful:

```bash
python ./driver-test.py 
```