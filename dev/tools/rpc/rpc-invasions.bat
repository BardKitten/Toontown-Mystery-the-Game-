@echo off
cd ../../../
set /P serv=RPC Server:
"C:\Panda3D-1.10.0\python\ppython.exe" "dev/tools/rpc/rpc-invasions.py" 6163636f756e7473 %serv%
pause