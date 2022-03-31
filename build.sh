#!/bin/sh
pyinstaller --onefile --noconsole -F -y --hidden-import http.cookies byteProcessor.py --icon=HexToBytes.icns
