@echo off
title Toontown Mystery Ai Server
mode con: cols=60 lines=20
rem Define some constants for our AI server:
set MAX_CHANNELS=999999
set STATESERVER=4002
set ASTRON_IP=127.0.0.1:7100
set EVENTLOGGER_IP=127.0.0.1:7198


set DISTRICT_NAME=Toontown Mystery
set BASE_CHANNEL=401000000

echo ===============================
echo Starting Toontown Mystery AI server...
echo District name: %DISTRICT_NAME%
echo Base channel: %BASE_CHANNEL%
echo Max channels: %MAX_CHANNELS%
echo State Server: %STATESERVER%
echo Astron IP: %ASTRON_IP%
echo Event Logger IP: %EVENTLOGGER_IP%
echo ===============================

cd ..

:main
"panda3d/python/python.exe" -m toontown.ai.ServiceStart --base-channel %BASE_CHANNEL% ^
               --max-channels %MAX_CHANNELS% --stateserver %STATESERVER% ^
               --astron-ip %ASTRON_IP% --eventlogger-ip %EVENTLOGGER_IP% ^
               --district-name "%DISTRICT_NAME%"
goto main
