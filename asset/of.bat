@echo off
cd /d "%~dp0"
taskkill /IM winmonitor-common.exe /F
exit
