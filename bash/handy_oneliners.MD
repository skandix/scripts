Showing who's streaming what from my plex and when.
```bash
strace -Tt -o /tmp/tail.trace tail --follow=name Plex\ Media\ Server.log | egrep '\[.{0,3}\].[a-zA-Z ]{0,}\(ID. [0-9]{1,8}\)'
```
Header grabber with netcat
```bash
for f in {80..1024}; do nc -v 127.0.0.1 $f; done 
```

Used to upload screenshot to my server,
```bash
name=$(cat /proc/sys/kernel/random/uuid).jpg;import $name;scp -q $name loot:/var/www/html/loot;echo http://datapor.no/loot/$name | xclip;
```
other
```bash
wget -qO- https://www.spotify.com/no/download/linux | egrep 'recv-keys\s\w+'
puttygen key.ppk  -O private-openssh -o id_rsa
puttygen key.ppk  -O public-openssh -o id_rsa.pub
```
