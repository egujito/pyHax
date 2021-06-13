@echo off

TITLE pyHax builder
COLOR 2

goto INIT

REM USE --noconsole to build without the console. Not ideal for debugging

:INIT

set /p val = "Do you have pyinstaller installed? <y/n> "

if (%val% == "y") (goto BUILDER) else (pip install pyinstaller)

goto BUILDER

:BUILDER
pyinstaller ..\main.py --onefile --icon ..\assets\icon.ico
