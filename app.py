from flask import Flask, request, jsonify
from moviepy.editor import TextClip, CompositeVideoClip
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import uuid

app = Flask(__name__)

# Autenticación de Google Drive
def autenticar_drive():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("credentials.json")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()  # Solo funciona en local
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile("credentials.json")
    return GoogleDrive(gauth)

# Generar video simple desde texto
def generar_video(texto, nombre_archivo):
    clip = TextClip(texto, fontsize=70, color='white', size=(720, 1280))
    clip = clip.set_duration(5)
    video = CompositeVideoClip([clip])
    video.write_videofile(nombre_archivo, fps=24)

@app.route("/")
def home():
    return "Servidor en producción con subida a Google Drive ✅"

@app.route("/generar_video", methods=["POST"])
def generar_video_endpoint():
    data = request.get_json()
    idea = data.get("idea", "sin_idea")
    texto = data.get("text", "sin_texto")

    # Generar nombre único
    nombre_archivo = f"{uuid.uuid4().hex}_{idea.replace(' ', '_')}.mp4"

    # Generar video localmente
    generar_video(texto, nombre_archivo)

    # Subir a Google Drive
    drive = autenticar_drive()
    archivo_drive = drive.CreateFile({'title': nombre_archivo})
    archivo_drive.SetContentFile(nombre_archivo)
    archivo_drive.Upload()

    # Obtener enlace público
    archivo_drive['sharingUser'] = 'me'
    archivo_drive.InsertPermission({
        'type': 'anyone',
        'value': 'anyone',
        'role': 'reader'
    })
    video_url = archivo_drive['alternateLink']

    # Borrar video local
    os.remove(nombre_archivo)

    return jsonify({
        "status": "ok",
        "video_url": video_url
    })

if __name__ == "__main__":
    app.run(debug=True)