# saannd 

```bash
$ pip install pyinstaller
$ pyinstaller setup.py >> log 2>&1
$ rm -rf build/ dist/ log __pycache__/ setup.spec 
```  
  
## File Structure
```
saannd/
├── __pycache__/
├── build/
├── dist/
│   └── setup/
|       └── ./setup
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
