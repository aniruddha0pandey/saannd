# saannd 

```bash
$ pip install pyinstaller
$ pyinstaller setup.py >> log/"`date +%d:%m:%Y-%H:%M:%S.log`" 2>&1
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
├── log/
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
