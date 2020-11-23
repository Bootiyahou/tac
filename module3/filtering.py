"""Filter out stopwords for word cloud"""

import sys
import nltk
try:
    from nltk.corpus import stopwords
except LookupError:
    nltk.download('stopwords')
    from nltk.corpus import stopwords

sw = stopwords.words("french")
sw += ["les", "plus", "cette", "fait", "faire", "être", "deux", "comme", "dont", "tout",
       "ils", "bien", "sans", "peut", "tous", "après", "ainsi", "donc", "cet", "sous",
       "celle", "entre", "encore", "toutes", "pendant", "moins", "dire", "cela", "non",
       "faut", "trois", "aussi", "dit", "avoir", "doit", "contre", "depuis", "autres",
<<<<<<< HEAD
       "van", "het", "autre", "jusqu", "elles", "assez", "ceux", "quelque", "parce", "que", 
       "aucun", "très", "rien", "peu", "laquelle", "etc", "chaque", "chez", "leurs", "aucune",
       "imp", "certain", "mal", "effet", "terme", "également", "crois", "quelques", "diverses", "déjà", "plusieurs",
       "faite", "celui", "savoir", "pourra", "trouve", "toute", "doivent", "avant", "près", "quant", "quand", "divers",
       "reste", "seul", "suivant"]
sw = set(sw)


def filtering(YEAR):
    path = f"{YEAR}.txt"
    output = open(f"{YEAR}_keywords.txt", "w")

    with open(path) as f:
=======
       "van", "het", "autre", "jusqu", "ville"]
sw = set(sw)


def filtering(year, folder=None):
    if folder is None:
        input_path = f"{year}.txt"
        output_path = f"{year}_keywords.txt"
    else:
        input_path = f"{folder}/{year}.txt"
        output_path = f"{folder}/{year}_keywords.txt"
    output = open(output_path, "w", encoding='utf-8')
    with open(input_path, encoding='utf-8') as f:
>>>>>>> upstream/master
        text = f.read()
        words = nltk.wordpunct_tokenize(text)
        kept = [w.lower() for w in words if len(
            w) > 2 and w.isalpha() and w.lower() not in sw]
        kept_string = " ".join(kept)
        output.write(kept_string)
    return f'Output has been written in {output_path}!'


if __name__ == '__main__':
    data_path = sys.argv[1]
    chosen_year = sys.argv[2]
    filtering(data_path, chosen_year)
