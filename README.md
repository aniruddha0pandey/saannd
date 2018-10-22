# saannd 

### Dependencies
```bash
$ pip install pyinstaller
```
### Build
```bash
$ pyinstaller setup.py >> logs/"`date +%d:%m:%Y-%H:%M:%S.log`" 2>&1 # make sure logs/ directory is present
```
### Rebuild / Clean
```bash
$ rm -rf build/ dist/ __pycache__/ setup.spec
```  
  
## File Structure
```
saannd/
├── build/
│   └── setup/
├── dist/
│   └── setup/
|       └── ./setup <--- Binaries
├── logs/
│   └── day:month:year-hour:min:sec.log
├── packages/
│   ├── nav/
|   ├── toolbar/
|   └── sign/
├── __pycache__/
│   └── setup.cpython-37.pyc
├── README.md
├── setup.py
└── setup.spec
```
