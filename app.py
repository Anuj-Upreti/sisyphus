from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Options data — edit these to change what appears on the page
OPTIONS = [
    {"number": "01", "title": "Option 1", "desc": "Select this path to proceed with the first choice."},
    {"number": "02", "title": "Option 2", "desc": "Select this path to proceed with the second choice."},
]

@app.route("/")
def index():
    return render_template("index.html", options=OPTIONS)

@app.route("/select", methods=["POST"])
def select():
    data = request.get_json()
    chosen = data.get("option")
    print(f"User selected: Option {chosen}")
    return jsonify({"status": "ok", "selected": chosen})

if __name__ == "__main__":
    app.run(debug=True)