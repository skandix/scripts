#!/bin/sh
xrandr --output DisplayPort-1 --off \
       --output DisplayPort-0 --primary --mode 1920x1080 --pos 1920x0 --rotate normal \
       --output DisplayPort-3 --mode 1920x1080 --pos 0x0 --rotate normal 
sleep 1

xrandr --output DisplayPort-1 --mode 1920x1080 --pos 3840x0 --rotate normal \
       --output DisplayPort-0 --off  
       --output DisplayPort-3 --mode 1920x1080 --pos 0x0 --rotate normal 
sleep 1

xrandr --output DisplayPort-1 --mode 1920x1080 --pos 3840x0 --rotate normal \
       --output DisplayPort-0 --primary --mode 1920x1080 --pos 1920x0 --rotate normal \
       --output DisplayPort-3 --off  
sleep 1

xrandr --output DisplayPort-1 --mode 1920x1080 --pos 3840x0 --rotate normal \
       --output DisplayPort-0 --primary --mode 1920x1080 --pos 1920x0 --rotate normal \
       --output DisplayPort-3 --mode 1920x1080 --pos 0x0 --rotate normal 
   
xset s off
xset -dpms
xset s noblank
