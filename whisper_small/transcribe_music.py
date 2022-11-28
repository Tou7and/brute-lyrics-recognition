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
    print("loading whisper...")
    model = whisper.load_model("small")
    sent_list = []
    print("Start decoding...")
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
        sys.exit(0)
    mp3_file = sys.argv[1]
    output_folder = sys.argv[2]
    
    wav_list = glob(os.path.join(output_folder, "chunk-*.wav"))
    wav_list.sort()
    if len(wav_list) == 0:
        wav_list = preprocess(mp3_file, output_folder)
    print(f"Get {len(wav_list)} segments after preprocessing.")
    trans_loop(wav_list, output_folder)
