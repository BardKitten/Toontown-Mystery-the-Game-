@echo off
title Toontown Mystery Astron Cluster
mode con: cols=60 lines=20
cd "../dependencies/astron/"

astrond --loglevel info config/cluster.yml
pause
