# Installing Sabnzdb
echo "installing Sabnzdb"
sudo apt-get install python-gdbm python-cheetah python-openssl par2 unzip -y

echo "deb http://ppa.launchpad.net/jcfp/ppa/ubuntu precise main" | tee -a /etc/apt/sources.list.d/sabnzbdplus.list
sudo apt-key adv --keyserver hkp://pool.sks-keyservers.net:11371 --recv-keys 0x98703123E0F52B2BE16D586EF13930B14BB9F05F
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install sabnzbdplus -y
sudo service sabnzbdplus restart
sudo update-rc.d sabnzbdplus defaults


# echo "sudo nano /etc/default/sabnzbdplus"
# USER=username
# HOST=0.0.0.0
# PORT=8080

# Installing Sonarr
# sauce https://github.com/Sonarr/Sonarr/wiki/Installation
echo "Installing Sonarr TV Series PVR"

sudo apt-get update -y
sudo apt-get install mono-devel -y

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC
echo "deb http://apt.sonarr.tv/ master main" | sudo tee /etc/apt/sources.list.d/sonarr.list

sudo apt-get update -y
sudo apt-get install nzbdrone -y
# to test sonarr; mono --debug /opt/NzbDrone/NzbDrone.exe


# installing plex
# Sauce http://www.htpcguides.com/install-plex-media-server-on-debian-linux/
echo installing plex
wget -O - http://shell.ninthgate.se/packages/shell.ninthgate.se.gpg.key | sudo apt-key add -
echo "deb http://www.deb-multimedia.org wheezy main non-free" | sudo tee -a /etc/apt/sources.list.d/deb-multimedia.list
echo "deb http://shell.ninthgate.se/packages/debian wheezy main" | sudo tee -a /etc/apt/sources.list.d/plex.list

sudo apt-get update -y
sudo apt-get install deb-multimedia-keyring -y

sudo apt-get update -y
sudo apt-get install plexmediaserver -y

#fixxing usermod
sudo usermod -aG skandix plex
sudo chmod -R 775 /mnt/disk-0

echo "Now; sudo nano /etc/default/plexmediaserver"
echo " "
echo "And edit this; PLEX_MEDIA_SERVER_USER=plex"
echo "to this;PLEX_MEDIA_SERVER_USER=skandix"
echo " "
echo "then sudo service plexmediaserver restart "

# disk-0 (zfs-raid)
# disk-1 (Temp Download)
# disk-2 (Complete Downloads)
