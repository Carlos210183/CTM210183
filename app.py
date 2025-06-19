from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Servidor en producción con Gunicorn ✅'

@app.route('/generar_video', methods=['POST'])
def generar_video():
    data = request.get_json()
    idea = data.get("idea")
    texto = data.get("text")

    # Simulación de generación de video
    return jsonify({
        "status": "ok",
        "video_url": f"https://tuvideo.fake/{idea.replace(' ', '_')}.mp4"
    })

if __name__ == "__main__":
    app.run(debug=True)