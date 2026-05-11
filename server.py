from flask import Flask, request, send_file
from rembg import remove
from io import BytesIO

app = Flask(__name__)

@app.route("/api/remove", methods=["POST"])
def remove_bg():
    input_data = request.get_data()
    if not input_data:
        return "No image data", 400
    output = remove(input_data)
    return send_file(BytesIO(output), mimetype="image/png")

@app.route("/", methods=["GET"])
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)