"""
Tool for lev-distance computation:
    https://pypi.org/project/edit-distance/

Results Example:
    [['replace', 0, 1, 0, 1], ['equal', 1, 2, 1, 2], ['replace', 2, 3, 2, 3], ['replace', 3, 4, 3, 4]]
"""
import sys
import re
import edit_distance

def get_er(string1, string2, unit="word"):
    """
    Unit can be word or char.
    Default is word.
    """
    if unit == "char":
        ref = list(string1)
        hyp = list(string2)
    else:
        ref = string1.split(" ")
        hyp = string2.split(" ")

    sm = edit_distance.SequenceMatcher(a=ref, b=hyp)
    codes = sm.get_opcodes()

    counts = {"replace": 0, "insert": 0, "delete": 0, "equal": 0}
    for code in codes:
        counts[code[0]] +=1

    # Refer to WER definition: https://en.wikipedia.org/wiki/Word_error_rate
    n_error = counts["replace"] + counts["delete"] + counts["insert"]
    n_total = counts["replace"] + counts["delete"] + counts["equal"]
    return round(n_error/n_total, 4), counts

def load_text(text_path, unit="word"):
    with open(text_path, 'r') as reader:
        raw_text = reader.read()
    if unit == "char":
        text = re.sub("[\n ]", "", raw_text)
    else:
        text = re.sub("\n", " ", raw_text)
    return text

def norm_english(raw_text):
    """
    Lower and upper does not matter.
    Exclude special tokens.
    """
    text = raw_text.lower().strip()
    patt = re.compile("[a-z']+")
    word_list = patt.findall(text)
    return " ".join(word_list)

def compute_errors_jihad():
    y = load_text("data/jihad/ref.txt", "char")
    x = load_text("data/jihad/hyp.txt", "char")
    cer_jihad, counts_jihad = get_er(y, x, unit="char")
    print("CER: ", cer_jihad)
    print(counts_jihad)

def compute_errors_beatit():
    y = load_text("data/beatit/ref.txt")
    x = load_text("data/beatit/hyp.txt")

    y = norm_english(y)
    x = norm_english(x)

    cer, counts_beatit = get_er(y, x, unit="char")
    print("CER: ", cer)
    print(counts_beatit)
    wer, counts_beatit = get_er(y, x,)
    print("WER: ", wer)
    print(counts_beatit)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"usage: python {sys.argv[0]} [REF.txt] [HYP.txt]")
        sys.exit(0)
    ref = sys.argv[1]
    hyp = sys.argv[2]
    y = load_text(ref)
    x = load_text(hyp)
    cer, counts = get_er(y, x, unit="char")
    print("CER: ", cer, counts)
    wer, counts = get_er(y, x,)
    print("WER: ", wer, counts)
