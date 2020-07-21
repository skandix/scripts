# README.md
Showing who's streaming what from my plex and when.
```bash
strace -Tt -o /tmp/tail.trace tail --follow=name Plex\ Media\ Server.log | egrep '\[.{0,3}\].[a-zA-Z ]{0,}\(ID. [0-9]{1,8}\)'
```
```bash
for f in {80..1024}; do nc -v 127.0.0.1 $f; done 
```

```bash
name=$(cat /proc/sys/kernel/random/uuid).jpg;import $name;scp -q $name loot:/var/www/html/loot;echo http://datapor.no/loot/$name | xclip;
```

```bash
uname=$(cat /proc/sys/kernel/random/uuid);ext=${1#*.};obfusc="$uname.$ext";mv $1 $obfusc;scp -q $obfusc loot:/var/www/html/loot;echo https://loot.datapor.no/$obfusc | xclip;rm $obfusc -f;
```

```bash
ext_ip=$(docker exec -it transmission /bin/sh -c "wget -qO- http://ipecho.net/plain"); rev_ip_chk=$(host $ext_ip | cut -d' ' -f 5);if [ $rev_ip_chk != "customer.tigerbackbone.com" ];then echo "All good\n$rev_ip_chk" ;else docker stop transmission -q;fi
```


```bash
for k in $(grep -r "import" | cut -d' ' -f2 | sort --unique);do pip install  $k;done;
```


```bash
for k in $(cat fail2ban.log | cut -d' ' -f 19 | uniq | strings | egrep [0-9]+); do echo ; whois $k -H | egrep "(netname|descr|person|country|route)";echo ;done;
```


```bash
find /sys/kernel/iommu_groups/ -type l | grep "$(lspci -nn | grep VGA | cut -d':' -f1)"
```

### other
```bash
wget -qO- https://www.spotify.com/no/download/linux | egrep 'recv-keys\s\w+'
puttygen key.ppk  -O private-openssh -o id_rsa
puttygen key.ppk  -O public-openssh -o id_rsa.pub
boolivar=$1;docker="docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build "; if [ "$boolivar" = True ];then echo $docker"-d";else echo $docker;fi
ffmpeg -i in.mp4 -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 out.mp3
find -type d -print0 | xargs -0 chmod -c 775 && find -type f -print0 | xargs -0 chmod -c 664
 sudo certbot certonly --standalone-d kek.example.com --pre-hook "service nginx stop" --post-hook "service nginx start"
certbot certonly --manual --preferred-challenges=dns --email hunter2k@example.com --server https://acme-v02.api.letsencrypt.org/directory --agree-tos  -d *.example.com  --pre-hook "service nginx stop" --post-hook "service nginx start"
sudo dd if=something.iso of=/dev/sdX bs=1M status=progress oflag=sync
exiftool -all= filename
```
