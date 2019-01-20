# saannd 

### Dependencies
```bash
$ pip install pyinstaller # py2exe
$ wget https://raw.githubusercontent.com/aniruddha0pandey/dotfiles/master/.scripts/ydaami.c
```
### Build
```bash
$ ./buildapp.sh                   # build application
$ ./ydaami -rm! saannd/ README.md # (optional) build project-structure markdown
$ # tree >> README.md # (otherwise)
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
├── README.md
├── setup.py
├── setup.spec
└── TODOs
```
