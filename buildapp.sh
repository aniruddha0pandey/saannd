#!/bin/bash
pyinstaller setup.py >> ./logs/"`date +%d:%m:%Y-%H:%M:%S.log`" 2>&1 # make sure logs/ directory is present