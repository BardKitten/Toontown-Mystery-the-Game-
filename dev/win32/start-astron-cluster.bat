@echo off
cd "../../dependencies/astron/"

astrond --loglevel info config/cluster.yml
pause
