@echo off

cd ../../../

title GUI Editor
set GUI=

:main

"C:\Panda3D-1.10.0\python\ppython.exe" "dev/tools/gui/EditorStart.py"

echo.
echo.

goto main