:: Used at old workplace for quickly terminating all process when leaving work..
@echo off
Echo killing all Programs that have been choosen!
taskkill /F /IM putty.exe
taskkill /F /IM chrome.exe
taskkill /F /IM skype.exe
taskkill /F /IM cmd.exe
taskkill /F /IM iexplore.exe
taskkill /F /IM pageant.exe
taskkill /F /IM Greenshot.exe
taskkill /F /IM explorer.exe
start explorer.exe
pause
