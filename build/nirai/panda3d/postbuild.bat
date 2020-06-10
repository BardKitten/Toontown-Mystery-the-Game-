@echo off
cd built
echo Deleting unneeded files...
rd /Q /S bin 2>nul
rd /Q /S direct\extensions 2>nul
rd /Q /S etc 2>nul
rd /Q /S models 2>nul
rd /Q /S plugins 2>nul
rd /Q /S python 2>nul
del LICENSE 2>nul
del ReleaseNotes 2>nul

cd lib
del libp3pystub.lib 2>nul

cd ..
cd ..
