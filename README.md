# saannd 

### Dependencies
```bash
$ pip install pyinstaller
$ wget https://github.com/aniruddha0pandey/dotfiles/blob/master/.scripts/ydaami.c
```
### Build
```bash
$ ./buildapp.sh                      # build application
$ ./ydaami -rm! saannd/ >> README.md # (optional) build project-structure markdown
```
### Rebuild / Clean
```bash
$ ./cleanapp.sh
```  
<sub><code>chmod u+x</code> to access build scripts as executables and <code>make</code> for making <code>ydaami</code> binaries.</sub>
  
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
