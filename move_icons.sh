#!/bin/bash
mkdir "/Users/alora/Maktab/sending projects/hw7/untitled folder/MaktabsharifMiniProject3/front/Icons"
file="Icons.txt"
while read -r line; do
    mv "$line" "/Users/alora/Maktab/sending projects/hw7/untitled folder/MaktabsharifMiniProject3/front/Icons/"
done <$file
