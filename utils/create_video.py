def create_video(image_path, audio_path):
    from moviepy.editor import ImageClip, AudioFileClip
    import os
    video_path = "/tmp/video.mp4"
    clip = ImageClip(image_path).set_duration(AudioFileClip(audio_path).duration)
    clip = clip.set_audio(AudioFileClip(audio_path)).resize(height=1280).resize(width=720)
    clip.write_videofile(video_path, fps=24)
    return video_path
