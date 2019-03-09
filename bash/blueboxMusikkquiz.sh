#!/bin/bash

pip3 install --upgrade youtube-dl
docker run --rm -it -v $(pwd):/music ritiek/spotify-downloader:latest -p $1
list=$(ls | grep .txt | head -n 1)
FOLDERNAME="${list%%.*}"
mkdir "$FOLDERNAME"
docker run --rm -it -v $(pwd):/music ritiek/spotify-downloader:latest -l $list
rm $list -rf
find . -maxdepth 1 -iname "*.mp3" -exec mv {} "$FOLDERNAME" \;
zip -r "$FOLDERNAME".zip "$FOLDERNAME" 
rm "$FOLDERNAME" -rf 
