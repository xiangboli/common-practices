# /bin/bash

python transcode.py -i contents/oceans.mp4 -o contents/transcoded
python package.py -i contents/transcoded -o contents/fragmented -d 2000
python generate_manifest.py -i contents/fragmented -o manifests