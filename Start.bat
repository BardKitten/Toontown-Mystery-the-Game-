@echo off
title Toontown Mystery Launcher
:launcher
cls
echo Toontown Mystery Launcher
echo ===============================
echo Enter 1 to start a server and play the game.
echo Enter 2 to join a server.
echo ===============================


choice /C:123 /n /m "Choose: "%1
if errorlevel ==2 goto joinserver
if errorlevel ==1 goto startserver




:startserver
cls
echo Starting server...
cd tools
start start-ai-server.bat
start start-uberdog-server.bat
start start-astron-cluster.bat
goto joinserver


:joinserver
cls
echo Press 1 if you want to play, or press 3 if you want to play Miniserver.
echo.
echo #1 - Localhost
echo #2 - Custom
echo #3 - Offical server
echo.

:selection

set INPUT=-1
set /P INPUT=Selection: 

if %INPUT%==1 (
    set TTS_GAMESERVER=127.0.0.1
) else if %INPUT%==3 (
    SET TTS_GAMESERVER=52.146.35.215
) else if %INPUT%==2 (
    echo.
    set /P TTS_GAMESERVER=Gameserver: 
) else (
	goto selection
)

echo.

if %INPUT%==2 (
    set /P ttsUsername="Username: "
    set /P ttsPassword="Password: "
) else if %INPUT%==4 (
    set /P ttsUsername="Username: "
    set /P ttsPassword="Password: "
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
    "panda3d/python/python.exe" -m toontown.toonbase.ToontownStartRemoteDB
) else if %INPUT%==4 (
    "panda3d/python/python.exe" -m toontown.toonbase.ToontownStartRemoteDB
) else (
    "panda3d/python/python.exe" -m toontown.toonbase.ToontownStart
)
pause

goto launcher


