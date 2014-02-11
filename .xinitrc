#!/bin/sh
setxkbmap dvorak

xrdb ~/.Xresources
redshift -l 43.85:-75 &
feh --bg-scale ~/images/wallpaper/Hnng\ chitose\ bg.png 
xmobar &

sxhkd -f 100 &
exec bspwm

