#!/bin/bash

PID=$(pgrep gnome-session-c)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ | cut -d= -f2- | tr -d '\0') 

PicDir="/home/fderoma/Pictures/wallpapers"

# Grab random photo from PicDir
function get_next_photo() {
    files=( "$PicDir"/* )
    echo "${files[RANDOM % ${#files[@]}]}"
}

function set_background() {
    bg="$*"
    gsettings set org.gnome.desktop.background picture-uri "file://$bg"
    gsettings set org.gnome.desktop.background picture-options "centered"
}

background=$(get_next_photo)
set_background $background
