# saannd 

### Dependencies
```bash
$ pip install pyinstaller
```
### Build
```bash
$ ./buildapp.sh
```
### Rebuild / Clean
```bash
$ ./cleanapp.sh
```  
<sub><code>chmod u+x</code> to make it executable.</sub>
  
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
