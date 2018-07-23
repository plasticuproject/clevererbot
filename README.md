# clevererbot
A simple CLI Cleverbot chat app for linux, using the cleverbotfree <br />
API and espeak. <br />

## Requirments
You need to have Python 3.x, pip, cleverbotfree, linux espeak and the latest <br />
Firefox browser installed <br />
To install espeak:
```
sudo apt-get install espeak
```

To install cleverbotfree:
```
pip install cleverbotfree
```

<b>Drivers</b>

Selenium requires a driver to interface with the headless browser. Firefox <br />
requires geckodriver, which needs to be installed before this module can be <br />
used. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin. <br />

You can download the geckodriver at https://github.com/mozilla/geckodriver/releases <br />

Failure to observe this step will give you the error <br />
"Message: ‘geckodriver’ executable needs to be in PATH." <br />


## Usage
Just run the script with Python:
```
python clevererbot.py
```
