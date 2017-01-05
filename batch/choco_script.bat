@echo off
goto check_Permissions

:check_Permissions
    echo Administrative permissions required. Detecting permissions...

    net session >nul 2>&1
    if %errorLevel% == 0 (

        color 02
        echo Success: Administrative permissions confirmed.

        ping 127.0.0.1 >nul
        goto choco_core

    ) else (
    	color 04
        echo Failure: Administrative permissions denied.
        ping 127.0.0.1 >nul

        echo Please restart the script with Administrative rigths.         
        ping 127.0.0.1 >nul
        
        goto exit
    )

    pause

:exit
pause
exit

:internett 
    echo checking for internett
    if ping www.google.no>1  (
        
        color 02
        echo internett access!
        echo moving rigth along
        
        ) else (
        
        color 04
        echo no internett, come back later when you got some!
        goto exit
        )



:choco_core
echo installing chocolatey core.
@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
if %errorLevel% == 0 (
    color 02    
    echo Success
    
    ) else (
    
    color 04
    echo Failure, try again later. check the log.
    )

pause
cls
echo Installing programs for skandix workstation
ping 127.0.0.1 > nul
cls

echo installing Chocolatey 0.9.10.3
choco install chocolatey -y
cls
exit
