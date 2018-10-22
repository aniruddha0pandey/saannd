# saannd 

```bash
$ pip install pyinstaller
$ pyinstaller setup.py >> "(log)`date +\(%d-%m-%Y\)\(%H:%M:%S\)`" 2>&1
$ rm -rf build/ dist/ log __pycache__/ setup.spec 
```  
  
## File Structure
```
saannd/
├── __pycache__/
├── build/
├── dist/
│   └── setup/
|       └── ./setup <--- Binaries
├── log/
│   └── date.log
├── packages/
│   ├── nav/
|   ├── toolbar/
|   └── sign/
├── README.md
├── setup.py
└── setup.spec
```
