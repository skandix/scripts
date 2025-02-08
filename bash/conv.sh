#!/usr/bin/env bash

files=$(ls *.webm | cut -d'.' -f1)

for k in $files; do
    ffmpeg -i "$k".webm "$k".mp4
done

mv *.mp4 mp4/
