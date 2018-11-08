#!/bin/bash
if [ ! -d "logs" ]; then mkdir logs/; fi
pyinstaller setup.py >> ./logs/"`date +%d-%m-%Y@%H-%M-%S.log`" 2>&1
echo -e "🐍 Build Completed 🐍"