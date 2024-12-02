from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

results_with_images = {
    "sigma:- you’re just a chill guy": "https://imgur.com/RyhEzAW",
    "sigma:- you got that special something congratz": "https://imgur.com/RyhEzAW",
    "walk proud alpha": "https://imgur.com/RyhEzAW",
    "sigma:- yasss queen": "https://imgur.com/RyhEzAW",
    "sigma:- pop off king": "https://imgur.com/RyhEzAW",
    "chad:- peaking in highschool": "https://imgur.com/RyhEzAW",
    "born to mew": "https://imgur.com/RyhEzAW",
    "rizzler:- I want you": "https://imgur.com/RyhEzAW",
    "rizzler:- You got pull more than a black hole": "https://imgur.com/RyhEzAW",
    "npc:- this is you -> -_-": "https://imgur.com/RyhEzAW",
    "npc:- stay in school": "https://imgur.com/RyhEzAW",
    "beta:- maybe in the next life": "https://imgur.com/RyhEzAW",
    "BETAAAAAAAAAAAAAAA": "https://imgur.com/RyhEzAW"
}

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
    result = random.choice(list(results_with_images.keys()))
        image = results_with_images[result]

    return jsonify({
        "loading_messages": loading_messages,
        "result_text": result,
        "result_image": image
    })

if __name__ == "__main__":
    app.run(debug=True)
