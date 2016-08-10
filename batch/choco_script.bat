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

echo installing Google Chrome
choco install google-chrome-x64 -y

echo installing mumble
choco install mumble -y

echo installing filezilla
choco install filezilla -y

echo installing teracopy
choco install teracopy -y

echo installing puttyTray
choco install puttyTray -y

echo installing git
choco install git -y

echo installing teamspeak3
choco install teamspeak -y

echo installing steam
choco install steam -y

echo installing uTorrent
choco install utorrent -y

echo installing battlenet
choco install battle.net -y

echo installing 7zip
choco install 7zip -y

echo installing flash player
choco install flashplayerplugin -y

echo installing java_7
choco install javaruntime -y

echo installing TeamViewer
choco install teamviewer -y

echo installing Adobe AIR 
choco install AdobeAIR -y

echo installing SublimeText3
choco install SublimeText3 -y

echo Installing Wireshark
choco install wireshark -y

echo installing Greenshot
choco install greenshot -Version 1.1.9.13 -y

echo installing Google drive
choco install googledrive -y

echo installing Spotify
choco install spotify -y

echo installing f.lux
choco install f.lux -y

pause
exit
