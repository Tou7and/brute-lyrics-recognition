# Brute-Lyrics-Recognition
Transcribe lyrics with the brute force of Whisper (or maybe some other strong ASR models.) <br>

## Whisper Small
The results are impressive and have potential to be improved with more pre-processing and post-processing. <br>
The model size of whisper-small is 465M in disk storage. (/Users/mac/.cache/whisper/small.pt) <br>
Current vendors: 
- [wiseman/py-webrtcvad](https://github.com/wiseman/py-webrtcvad)
- [ffmpeg-python](https://pypi.org/project/ffmpeg-python/)
- [whisper](https://github.com/openai/whisper) to run the inference on audio segments.

### Steps
```
cd whisper_small
python transcribe_music.py [MUSIC.mp3] [OUTPUT-FOLDER]
python get_error_rate.py [REF.txt] [HYP.txt]
```

### Results
Choose some songs for a quick evaluation. <br>
The audio files can be downloaded from Youtube and the lyrics are the first results of Google search. <br>
Currently I do not do much text normalization like excluding special characters etc for both lyrics and transcriptions, <br>
And some of the transcription results with poor error rate are actually acceptable in my sense.
- Beat It (MJ, English)
  - WER:  0.7183 
    - {'replace': 251, 'insert': 34, 'delete': 21, 'equal': 154}
  - WER(text norm applied):  0.6306 
    - {'replace': 211, 'insert': 35, 'delete': 22, 'equal': 192}
  - This song is tough, due to a lot of overlap and strong background music.
- Phantom of the opera (English)
  - (Not sure if the reference lyric match the video clips I found)
  - CER:  0.5544 
    - {'replace': 104, 'insert': 325, 'delete': 45, 'equal': 706}
  - WER:  0.8547 
    - {'replace': 61, 'insert': 80, 'delete': 6, 'equal': 105}
- Jihad (KOTOKO, Japanese)
  - CER:  0.3293 
    - {'replace': 60, 'insert': 43, 'delete': 6, 'equal': 265}
- Paradise Lost (Japanese)
  - CER:  0.526 
    - {'replace': 159, 'insert': 57, 'delete': 88, 'equal': 331}
- Pop Stars (KDA, Korean and English)
  - CER:  0.5344 
    - {'replace': 229, 'insert': 49, 'delete': 948, 'equal': 1117}
