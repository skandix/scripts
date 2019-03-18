@echo off 
md C:\urxvt\keys
md C:\urxvt\misc
choco install firefox -y
choco install 7zip -y
choco install twitch -y
choco install vscode -y
choco install audacity -y
choco install battle.net -y --allow-empty-checksums
choco install discord -y
choco install filezilla -y
choco install foobar2000 -y
choco install github-desktop -y
choco install plexmediaplayer -y
choco install jre8 -y
choco install mpv -y
choco install keepass -y 
choco install firefox -y
choco install ontopreplica -y
choco install obs-studio -y
choco install python -y
choco install sharex -y
choco install slack -y
choco install speccy -y
choco install spotify -y
choco install teamspeak -y
choco install teamviewer -y --ignore-checksums
choco install telegram -y
choco install veracrypt -y
choco install windows-tweaker -y
choco install vibrancegui -y
choco install wireshark -y
choco install steam -y
choco install tor-browser -y --ignore-checksums
choco install puttytray -y
choco install wget -y
wget https://the.earth.li/~sgtatham/putty/latest/w64/pageant.exe
wget https://loot.datapor.no/dzikvy9v.zip
wget https://app-updates.plays.tv/builds/PlaysSetup.exe
move https://the.earth.li/~sgtatham/putty/latest/w64/pageant.exe C:/urxvt/keys
cd C:/urxvt/keys/
pageant.exe skandix.ppk
