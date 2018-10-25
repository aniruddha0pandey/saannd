# saannd 

### Dependencies
```bash
$ pip install pyinstaller
```
### Build
```bash
$ chmod u+x buildApp.sh
$ ./buildapp.sh
```
### Rebuild / Clean
```bash
$ chmod u+x cleanApp.sh
$ ./cleanapp.sh
```  
  
### File Structure
```
saannd/
├── build/
│   └── setup/
├── buildApp.sh
├── cleanApp.sh
├── dist/
│   └── setup/
|       └── ./setup
├── .gitignore
├── logs/
│   └── day:month:year-hour:min:sec.log
├── packages/
│   └── menuBar/
├── __pycache__/
│   └── setup.cpython-37.pyc
├── README.md
├── setup.py
├── setup.spec
└── TODOs
```
