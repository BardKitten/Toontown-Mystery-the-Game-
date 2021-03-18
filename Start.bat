@echo off
title Toontown Mystery Launcher
:launcher
cls
echo What do you want to do?
echo ===============================
echo Enter 1 to start a server and play the game.
echo Enter 2 to connect to a server
echo ===============================


choice /C:123 /n /m "Choose: "%1
if errorlevel ==2 goto testing
if errorlevel ==1 goto startserver




:startserver
cls
echo Starting server...
cd tools
start start-ai-server.bat
start start-uberdog-server.bat
start start-astron-cluster.bat
goto joinserver

:testing
cls
cd tools
goto joinserver



:joinserver
echo Press 1 if you want to play, or press 2 if you want to connect to a server. (You need the ip)
echo ===============================
echo #1 - Localhost
echo #2 - Connect to a server
echo ===============================


set INPUT=-1
set /P INPUT=Selection: 
if %INPUT%==1 (
    set TTS_GAMESERVER=127.0.0.1

) else if %INPUT%==2 (
echo ===============================
echo Enter the server IP
echo ===============================
    set /P TTS_GAMESERVER=Gameserver: 
) else (
	goto selection
)
cls


if %INPUT%==2 (
echo ===============================
echo Enter a username.
echo ===============================
    set /P ttsUsername="Username: "
    cls

) else (
    set /P TTS_PLAYCOOKIE=Username: 
)

echo.

echo ===============================
echo Starting Toontown Mystery...
echo python: "panda3d/python/python.exe"

if %INPUT%==2 (
    echo Username: %ttsUsername%
) else if %INPUT%==4 (
    echo Username: %ttsUsername%
) else (
    echo Username: %TTS_PLAYCOOKIE%
)

echo Gameserver: %TTS_GAMESERVER%
echo ===============================

cd ..
:main
if %INPUT%==2 (   
    "panda3d/python/python.exe" -m toontown.toonbase.ToontownStart
) else (
    "panda3d/python/python.exe" -m toontown.toonbase.ToontownStart
)
pause

goto launcher

