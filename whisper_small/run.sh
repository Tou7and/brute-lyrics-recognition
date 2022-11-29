#!/bin/bash

python transcribe_music.py "/Users/mac/personal-collections/music/gare-zero/茅原実里-Paradise Lost.mp3" "exp/paradiselost"
cp exp/paradiselost/hyp.txt data/paradiselost/
python get_error_rate.py data/paradiselost/ref.txt data/paradiselost/hyp.txt
