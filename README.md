# CTM210183 - API Flask + Gunicorn

Servidor Flask preparado para desplegar en Render.com y generar videos vía endpoint POST.

## 📦 Estructura

```
.
├── app.py
├── requirements.txt
└── render.yaml
```

## 🚀 Despliegue en Render

1. Sube este repositorio a GitHub
2. Ve a [https://render.com](https://render.com)
3. Crea un nuevo Web Service → conecta con tu GitHub
4. Render detectará `render.yaml` y lo desplegará automáticamente

## 🧪 Endpoints

### `GET /`
Prueba si el servidor está activo.

**Respuesta:**
```
Servidor en producción con Gunicorn ✅
```

### `POST /generar_video`

Envía un JSON con los siguientes datos:

```json
{
  "idea": "Idea del video",
  "text": "Texto descriptivo del video"
}
```

**Respuesta de ejemplo:**

```json
{
  "status": "ok",
  "video_url": "https://tuvideo.fake/Idea_del_video.mp4"
}
```

---

CTM210183 - Proyecto de generación automática de contenido