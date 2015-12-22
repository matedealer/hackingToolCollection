#!/bin/bash
foo=$(sudo pacman -Sy)
count=$(pacman -Qu | wc -l)
printf "== Updatable Packages ======\n"
printf "There are "$count" Packages to update\n"
printf "============================\n\n"
