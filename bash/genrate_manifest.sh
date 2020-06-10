#! /bin/bash

for file in *.mp4;
do
# encode
# mkdir "${file%.*}"
# ffmpeg -y -i "$file" -c:v libx264 -b:v 5200k -g 60 -pass 1 -f mp4 /dev/null && \
# ffmpeg -i "$file" -c:v libx264 -b:v 4500k -g 60 -pass 2 "${file%.*}/${file%.*}_1080p".mp4
# ffmpeg -i "$file" -s 1280x720 -c:v libx264 -b:v 3000k -g 60 -pass 2 "${file%.*}/${file%.*}_720p".mp4
# ffmpeg -i "$file" -s 640x360 -c:v libx264 -b:v 1400k -g 60 -pass 2 "${file%.*}/${file%.*}_360p".mp4
# ffmpeg -i "$file" -vn -c:a aac -b:a 128k -ac 2 -r 48k "${file%.*}/${file%.*}_audio".mp4

echo "finished encoding"
# fragment
# mp4fragment --fragment-duration 2000 --index "${file%.*}/${file%.*}_1080p".mp4 "${file%.*}/${file%.*}_1080p_frag".mp4
# mp4fragment --fragment-duration 2000 --index "${file%.*}/${file%.*}_720p".mp4 "${file%.*}/${file%.*}_720p_frag".mp4
# mp4fragment --fragment-duration 2000 --index "${file%.*}/${file%.*}_360p".mp4 "${file%.*}/${file%.*}_360p_frag".mp4
# mp4fragment --fragment-duration 2000 --index "${file%.*}/${file%.*}_audio".mp4 "${file%.*}/${file%.*}_audio_frag".mp4

echo "finished fragment"

#generate manifest
mp4dash --use-segment-timeline --no-split --profiles="on-demand" --output-dir="${file%.*}/${file%.*}_dash" "${file%.*}/${file%.*}_1080p_frag".mp4 "${file%.*}/${file%.*}_720p_frag".mp4 "${file%.*}/${file%.*}_360p_frag".mp4 "${file%.*}/${file%.*}_audio_frag".mp4
#mp4hls --hls-version 5 --segment-duration 10 --output-single-file --output-dir="${file%.*}/${file%.*}_hls" "${file%.*}/${file%.*}_1080p_frag".mp4 "${file%.*}/${file%.*}_720p_frag".mp4 "${file%.*}/${file%.*}_360p_frag".mp4 "${file%.*}/${file%.*}_audio_frag".mp4 
echo "finished generating manifest"

#mv "$file" "${file%.*}"
done
