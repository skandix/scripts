@echo off 
md C:\urxvt\keys
md C:\urxvt\misc
choco install google-chrome-x64 -y
choco install mumble -y
choco install filezilla -y
choco install git -y
choco install teamspeak -y
choco install steam -y
choco install utorrent -y --allow-empty-checksums
choco install battle.net -y --allow-empty-checksums
choco install 7zip -y
choco install javaruntime -y
choco install procmon -y
choco install teamviewer -y --allow-empty-checksums
choco install wireshark -y
choco install spotify -y
choco install discord -y
choco install sharex -y
choco install jre8 -y
choco install foobar2000 -y
choco install veracrypt -y
choco install vim -y
choco install github -y
choco install openvpn -y
choco install firefox -y
choco install cygwin -y --allow-empty-checksums
choco install tor-browser -y --allow-empty-checksums
choco install windows-tweaker -y
choco install mpc-hc -y --allow-empty-checksums
choco install python2 -y
choco install keepass -y 
choco install jrt -y
choco install hijackthis -y
choco install sandboxie.install -y
choco install puttytray -y
choco install wget -y
wget https://the.earth.li/~sgtatham/putty/latest/w64/pageant.exe
move https://the.earth.li/~sgtatham/putty/latest/w64/pageant.exe C:/urxvt/keys
cd C:/urxvt/keys/
pageant.exe skandix.ppk
