from flask import Flask, request, jsonify
from utils.generate_image import generate_image
from utils.generate_audio import generate_audio
from utils.create_video import create_video
from utils.upload_drive import upload_to_drive

import os
from datetime import datetime

app = Flask(__name__)

@app.route("/generar_video", methods=["POST"])
def generar_video():
    data = request.get_json()
    idea = data.get("idea")
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Prompt faltante"}), 400

    try:
        image_path = generate_image(prompt)
        audio_path = generate_audio(prompt)
        video_path = create_video(image_path, audio_path)

        video_url = upload_to_drive(video_path)

        return jsonify({"video_url": video_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "Servidor activo - listo para generar videos"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
