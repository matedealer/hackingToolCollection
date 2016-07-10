#!/bin/bash
foo=$(sudo pacman -Sy 2> /dev/null)
count=$(pacman -Qu | wc -l)
printf "== Updatable Packages ======\n"
printf "There are "$count" Packages to update\n"
printf "============================\n\n"
