#!/usr/bin/env bash
while true;
do
    echo "    $(mocp -i | grep File: | cut -d':' -f 2 | cut -d'/' -f6)    "  > "$HOME/now_play.txt"
    sleep 5
done
