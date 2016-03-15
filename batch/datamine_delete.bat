ECHO OFF
TITLE Automated Cleaning/Remover of Dataminer
ECHO.  
ECHO Starting automated EXTERMATION of Dataminer
ECHO. 
PING -n 3 127.0.0.1>nul
CLS
ECHO. 
ECHO Cleaning Skyline OneClick 
ECHO. 
PING -n 3 127.0.0.1>nul 
RD /S /Q "C:\%HOMEPATH%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Skyline Communications"
PING -n 3 127.0.0.1>nul
RD /S /Q "C:\ProgramData\Skyline"
PING -n 3 127.0.0.1>nul
CLS
ECHO.
ECHO Deleting Dataminer Cube Standalone version x.x.x.x
ECHO.
wmic product where name="DataMiner Cube *.*.*.*" call uninstall /nointeractive > log.txt
CLS
ECHO.  
ECHO Done Running Automated Dataminer Remover
ECHO. 
PING -n 3 127.0.0.1>nul 
EXIT
