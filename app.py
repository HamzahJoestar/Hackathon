from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)
#hi
results = [
    "sigma:- you’re just a chill guy",
    "sigma:- you got that special something congratz",
    "walk proud alpha",
    "sigma:- yasss queen",
    "sigma:- pop off king",
    "chad:- peaking in highschool",
    "born to mew",
    "rizzler:- I want you",
    "rizzler:- You got pull more than a black hole",
    "npc:- this is you -> -_-",
    "npc:- stay in school",
    "beta:- maybe in the next life",
    "BETAAAAAAAAAAAAAAA"
]

loading_phrases = [
    "trying to leave ohio...",
    "calculating mew streak...",
    "assessing chad qualities...",
    "queen never cry...",
    "looksmaxing...",
    "is this a jojo reference?...",
    "gooning...",
    "rizzing up...",
    "baby gronk is stopping by...",
    "kai cenat says hello...",
    "chat is this real?...",
    "i like my cheese drippy bruh...",
    "you hear about mr beast?...",
    "from the screen to the ring to the pen to the king ...",
    "pipipipipipipipipipipipi..."
]

def get_random_phrases():
    """Return a list of 5 unique random phrases with percentages."""
    percentages = ["0%", "33%", "57%", "70%", "80%"]
    selected_phrases = random.sample(loading_phrases, len(percentages))
    return [f"{percentages[i]}... {selected_phrases[i]}" for i in range(len(percentages))]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    user_input = request.json.get("input", "")
    if not user_input:
        return jsonify({"error": "Input cannot be empty!"}), 400

    loading_messages = get_random_phrases()
    result = random.choice(results)

    return jsonify({
        "loading_messages": loading_messages,
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)
