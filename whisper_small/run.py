import os
import sys
import warnings
warnings.filterwarnings('ignore')
from glob import glob
from wave_convert import any_to_wave
import whisper

def preprocess(mp3_path, segment_path):
    # mp3_path = "/Users/mac/personal-collections/music/baldr-sky/Jihad.mp3"
    if os.path.isdir(segment_path) is False:
        os.makedirs(segment_path)
    any_to_wave(mp3_path, output_dir=segment_path)
    wav_list = glob(os.path.join(segment_path, "chunk-*.wav"))
    wav_list.sort()
    return wav_list

def trans_loop(segments, output_path):
    model = whisper.load_model("small")
    sent_list = []
    for seg_path in segments:
        print(seg_path)
        result = model.transcribe(seg_path)
        sent = result['text']
        sent_list.append(sent)
        print(sent)

    with open(os.path.join(output_path, "hyp.txt"), 'w') as writer:
        writer.write("\n".join(sent_list))
    return sent_list

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"usage: python {sys.argv[0]} [MUSIC.mp3] [OUTPUT-FOLDER]")
    # wav_list = preprocess("/Users/mac/personal-collections/music/league-of-legends/kda/star_lol.mp3", "exp/popstars")
    wav_list = preprocess("/Users/mac/personal-collections/music/league-of-legends/kda/star_lol.mp3", "exp/popstars")
    trans_loop(wav_list)
