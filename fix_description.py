import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string
from pathlib import Path
import sys
import json
from tqdm import tqdm

# nltk.download("stopwords")
# stop_words = set(stopwords.words("english"))


def fix_description_old(sentence):
    filtered_sentence = [w for w in sentence.split(" ") if not w.lower() in stop_words]
    no_punct = [
        s.translate(str.maketrans("", "", string.punctuation))
        for s in filtered_sentence
    ]
    fdist = FreqDist(no_punct)
    top_ten = fdist.most_common(10)
    description = " ".join(x[0] for x in top_ten)
    return description


def fix_description(data):
    title = data["title"].replace("(FREE) Drake Type Beat - \"" , "").replace("\"", "")
    description = title + " " + data["artist"] + " " + data["genre"] + " " + data["instrument"]
    return description



if __name__ == "__main__":
    root = Path(sys.argv[1])
    metadata_files = list(root.rglob("**/*.json"))
    for f in tqdm(metadata_files):
        with open(f, "r") as json_file:
            data = json.load(json_file)
            data["description"] = fix_description(data)
            # description = data["description"]
            # data["description"] = fix_description_old(description)
        with open(f, "w") as json_file:
            json.dump(data, json_file, indent=4)
    print("DONE fixing descriptions")
