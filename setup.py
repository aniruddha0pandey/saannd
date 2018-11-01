#!/usr/bin/env python
# -*- ENCODING: UTF-8 -*-
# -*- PYTHON DEVL: (3.7.2) -*-
 
try:
	import Tkinter as tk # python 2.x
except ImportError:
	import tkinter as tk # python 3.x

from packages.menuBar import *


def main():
	menuBar.showMenu()

if __name__ == "__main__":
    main()
