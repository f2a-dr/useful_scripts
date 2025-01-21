#!/bin/bash

PicDir='/home/f2a/Immagini/wallpapers'

# Grab random photo from PicDir
function get_next_photo() {
    files=( "$PicDir"/* )
    echo "${files[RANDOM % ${#files[@]}]}"
}

function set_background() {
    bg="$*"
    plasma-apply-wallpaperimage $bg
}

background=$(get_next_photo)
set_background ${background}
