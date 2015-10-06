// need to update this so i can use it in "production"
@echo off
goto check_Permissions

:check_Permissions
    echo Administrative permissions required. Detecting permissions...

    net session >nul 2>&1
    if %errorLevel% == 0 (
        color 12
        echo Success: Administrative permissions confirmed.

        ping 127.0.0.1 >nul
        goto choco_core
    ) else (
    	color 14
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
    if ping www.vg.no>1  (
        color 12
        echo internett access!
        echo moving rigth along
        ) else (
        color 14
        echo no internett, come back later when you got some!
        goto exit
        )


  //make if statement if connected to internett before installing ?

:choco_core
echo installing chocolatey core.
@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
if %errorLevel% == 0 (
    color 12    
    echo Success
    ) else (
    color 14
    echo Failure, try again later. check the log.
    )

pause
cls
echo Installing programs for skandix workstation
ping 127.0.0.1 > nul
cls
echo installing Chocolatey 0.9.8.27
choco install chocolatey -Version 0.9.8.27
cls
echo installing Google Chrome
choco install GoogleChrome
echo installing 7zip
choco install 7zip
echo installing Eclipse
choco install eclipse-standard-luna
echo installing flash player
choco install flashplayerplugin
echo installing java 7
choco install javaruntime
echo installing DropBox
choco install dropbox
echo installing Virtualbox
choco install virtualbox
echo installing TeamViewer
choco install teamviewer
echo installing Adobe AIR 
choco install AdobeAIR
echo installing SublimeText3
choco install SublimeText3
echo Installing Wireshark
choco install wireshark
echo installing Greenshot
choco install greenshot -Version 1.1.9.13
echo installing quicktime
choco install Quicktime
echo installing Google drive
choco install googledrive
echo installing Spotify
choco install spotify
echo installing nmap
choco install nmap
echo installing yumi
choco install yumi
echo installing Remote Desktop Connection Manager
choco install rdcman
echo installing GitHub
choco install githubforwindows
echo installing f.lux
choco install f.lux
echo installing android-sdk
choco install android-sdk
echo installing adobe reader
choco install adobereader
pause
exit
