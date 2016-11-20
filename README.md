# Installation

## External Dependencies
* imagemagick
* tesseract
* rabbitmq
* mysql

## Install Tesseract Core
```
brew install imagemagick
brew install tesseract
```

## Configure Python environment
```
$ pip install virtualenv # If not already installed
$ virtualenv venv && . venv/bin/activate
$ pip install -r requirements.txt
```

# Run Application

```
$ python app.py
```