# saannd 

### Dependencies
```bash
$ pip install pyinstaller
```
### Build
```bash
$ chmod u+x buildApp.sh
$ ./buildApp.sh
```
### Rebuild / Clean
```bash
$ chmod u+x cleanApp.sh
$ ./cleanApp.sh
```  
  
### File Structure
```
saannd/
├── build/
│   └── setup/
├── dist/
│   └── setup/
|       └── ./setup
├── logs/
│   └── day:month:year-hour:min:sec.log
├── packages/
│   └── menuBar/
├── __pycache__/
│   └── setup.cpython-37.pyc
├── README.md
├── setup.py
└── setup.spec
```
