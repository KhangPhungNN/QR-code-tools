@rem Check and install Python automatically
@echo off

echo Install Chocolatey ...
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
cls

echo Install Python ...
choco install -y python3
cls

echo Python vesion ...
python --version

pause