@echo off 
start powershell -Command {Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))}
md C:\urxvt\keys
md C:\urxvt\misc
choco install 7zip -y
choco install openhardwaremonitor -y
choco install audacity -y
choco install battle.net -y --allow-empty-checksums
choco install burp-suite-free-edition -y
choco install discord -y
choco install filezilla -y
choco install foobar2000 -y
choco install github -y --ignore-checksums
choco install jre8 -y
choco install keepass -y 
choco install megasync -y
choco install firefox -y
choco install mumble -y
choco install obs-studio -y
choco install postman -y
choco install python2 -y
choco install sharex -y
choco install slack -y
choco install speccy -y
choco install speedfan -y
choco install spotify -y
choco install sublimetext3 -y
choco install teamspeak -y
choco install teamviewer -y --ignore-checksums
choco install telegram -y
choco install veracrypt -y
choco install windows-tweaker -y
choco install wireshark -y
choco install utorrent -y --ignore-checksums
choco install steam -y
choco install tor-browser -y --ignore-checksums
choco install puttytray -y
choco install wget -y
wget https://the.earth.li/~sgtatham/putty/latest/w64/pageant.exe
move https://the.earth.li/~sgtatham/putty/latest/w64/pageant.exe C:/urxvt/keys
cd C:/urxvt/keys/
pageant.exe skandix.ppk
