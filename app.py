from flask import Flask, jsonify

app = Flask(__name__)

VERSION = "1.4.0"


@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok", version=VERSION), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
