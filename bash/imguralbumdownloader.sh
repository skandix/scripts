# Made this script to make my life easier.
# instead of using the default album downloader, this does things faster.
# and it makes me possible to downoad things directly to my server.
# -Skandix
#!/bin/bash
echo " "
echo "===IMGUR ALBUM DOWNLOADER==="
echo " "
echo "type in gallery_url"
read gallery_url
echo " "
echo "name of folder?"
read folder_name
mkdir $folder_name && cd $folder_name
wget --no-check-certificate -q "$gallery_url" -O - | \
grep 'data-src'|cut -d\" -f10|while read id
do
    hashid=`basename "$id" "s.jpg"`
    echo "Downloading $hashid.jpg"
    wget -q -c "http://i.imgur.com/$hashid.jpg"
done
