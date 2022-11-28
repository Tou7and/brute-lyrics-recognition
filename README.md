# Brute-Lyrics-Recognition
Transcribe lyrics with the brute force of Whisper (or maybe some other strong ASR models.) <br>

## Whisper Small
The results using Whisper are quite impressive, and have potentials to be improved with more pre-processing and post-processing. <br>
Currently use [wiseman/py-webrtcvad](https://github.com/wiseman/py-webrtcvad) and [ffmpeg-python](https://pypi.org/project/ffmpeg-python/) for pre-processing, and use Whisper small from [whisper](https://github.com/openai/whisper) to run the inference on audio segments.

Steps
```
cd whisper_small
python run.py [MUSIC.mp3] [OUTPUT-FOLDER]
python get_error_rate.py [REF.txt] [HYP.txt]
```

Results
- Jihad (KOTOKO, Japanese)
  - [Transcriptions](whisper_small/data/jihad/hyp.txt) <br>
  - [Ground-truth](whisper_small/data/jihad/ref.txt) <br>
  - CER:  0.3293 {'replace': 60, 'insert': 43, 'delete': 6, 'equal': 265}
- Beat It (MJ, English)
  - [Transcriptions](whisper_small/data/beatit/hyp.txt) <br>
  - [Ground-truth](whisper_small/data/beatit/ref.txt) <br>
  - CER:  0.479 {'replace': 495, 'insert': 301, 'delete': 210, 'equal': 1395}
  - WER:  0.7183 {'replace': 251, 'insert': 34, 'delete': 21, 'equal': 154}
  - After apply a text normalization for English:
    - CER:  0.4411 {'replace': 414, 'insert': 290, 'delete': 184, 'equal': 1415}
    - WER:  0.6306 {'replace': 211, 'insert': 35, 'delete': 22, 'equal': 192}
  - This song is tough, due to a lot of overlap and strong background music.
- Pop Stars (KDA, Korean and English)
  - [Transcriptions](whisper_small/data/popstars/hyp.txt) <br>
  - [Ground-truth](whisper_small/data/popstars/ref.txt) <br>
  - CER:  0.5344 {'replace': 229, 'insert': 49, 'delete': 948, 'equal': 1117}
  - WER:  0.6647 {'replace': 121, 'insert': 5, 'delete': 205, 'equal': 172}
