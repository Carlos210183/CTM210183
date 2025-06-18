from flask import Flask, request, jsonify
from moviepy.editor import TextClip, CompositeVideoClip
import uuid
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🟢 Servidor funcionando correctamente."

@app.route("/generar_video", methods=["POST"])
def generar_video():
    data = request.json
    idea = data.get("idea", "video")
    text = data.get("text", "Texto de ejemplo")
    filename = f"{uuid.uuid4().hex[:8]}_{idea[:20].replace(' ', '_')}.mp4"

    try:
        clip = TextClip(text, fontsize=70, color='white', size=(720, 1280), method='caption').set_duration(5)
        video = CompositeVideoClip([clip])
        video.write_videofile(filename, fps=24)
        return jsonify({"video_url": f"https://example.com/videos/{filename}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)

