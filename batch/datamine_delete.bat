:: used at old workplace for truly removing everything from the monitoring software we used.
@ECHO OFF
TITLE Automated Cleaning/Remover of Dataminer
ECHO Starting automated EXTERMATION of Dataminer
PING -n 3 127.0.0.1>nul
CLS

ECHO Cleaning Skyline OneClick 
RD /S /Q "C:\%HOMEPATH%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Skyline Communications"
RD /S /Q "C:\ProgramData\Skyline"
CLS

ECHO Deleting Dataminer Cube Standalone version x.x.x.x
wmic product where name="DataMiner Cube *.*.*.*" call uninstall /nointeractive > log.txt
CLS 

ECHO Done Running Automated Dataminer Remover 
PING -n 3 127.0.0.1>nul 
EXIT
