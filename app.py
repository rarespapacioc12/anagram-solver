from flask import Flask, render_template, request
import json

data = json.load(open("dictionary_compact.json"))

app = Flask(__name__, template_folder='.')

def find_anagrams(word):
    word = word.strip().lower()
    anagrams = []
    for w in data:
        if sorted(word) == sorted(w.lower()):
            anagrams.append(w)
    return anagrams


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        word = request.form["word"]
        anagrams = find_anagrams(word)
        return render_template("index.html", search=word, anagrams=anagrams)
    
    return render_template("index.html", search="", anagrams=[])


if __name__ == "__main__":
    app.run()