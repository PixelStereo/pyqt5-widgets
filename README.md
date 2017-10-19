# PyOssia Widgets
[![Build Status](https://travis-ci.org/PixelStereo/pyossia_widgets.svg?branch=master)](https://travis-ci.org/PixelStereo/pyossia_widgets)    
    
PyOssia Widgets is a python Package that provides widgets for [pyossia](http://github.com/PixelStereo/pyossia)    
It will use pyossia and libossia thanks to pybind11    

# Installation

## latest stable
pyossia does not have yet a stable version

## latest unstable (git master branch)
`pip install git+https://github.com/PixelStereo/pyossia_widgets.git@master`    

## git repo (for contribution)    

```git clone https://github.com/PixelStereo/pyossia_widgets.git```

```cd pyossia    ```

```pip install -ve .```

```-e``` option will just add the git repo to your python path

# Dependancies
For now, pxst-widgets are dependant of PyQt5 Framework.
## MaxOs
tested on MacOs Sierra aka 10.12 with homebrewed python3
```
pip3 install PyQt5
```

## Linux    

# Raspeberry Pi    
tested on rpi 2 / raspbian stretch    
apt-get install qt5-default pyqt5-dev pyqt5-dev-tools    

# Credits

Pyossia Widgets is written by Pixel Stereo, under GPL 3 licence    