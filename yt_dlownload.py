import yt_dlp
import os
import sys

ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")


def download_yt_video(url, d_format, progress_callback=None):
    def progress_hook(d):
        if d['status'] == 'downloading':
            if 'total_bytes' in d and 'downloaded_bytes' in d:
                percent = int(d['downloaded_bytes'] / d['total_bytes'] * 100)
            elif 'total_bytes_estimate' in d and 'downloaded_bytes' in d:
                percent = int(d['downloaded_bytes'] / d['total_bytes_estimate'] * 100)
            else:
                percent = 0  # Falls keine Größe bekannt ist

            print(f"[DEBUG] Download-Fortschritt: {percent}%")  # Debugging
            if progress_callback:
                progress_callback(percent)

        elif d['status'] == 'finished':
            print("[DEBUG] Download abgeschlossen!")  # Debugging
            if progress_callback:
                progress_callback(100)

    ydl_opts = {
        'format': d_format,
        'noplaylist': True,
        'progress_hooks': [progress_hook],  # Fortschritts-Hook einbinden
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"[ERROR] Download fehlgeschlagen: {e}")

    # Bestimmen des Verzeichnisses, in dem sich die .exe befindet (auch wenn sie gepackt ist)
    if getattr(sys, 'frozen', False):
        # Wenn das Skript als .exe läuft, verwenden wir den Ordner der .exe
        current_directory = os.path.dirname(sys.executable)
    else:
        # Wenn das Skript als normales Python-Skript läuft, verwenden wir das Verzeichnis des Skripts
        current_directory = os.path.dirname(os.path.realpath(__file__))

    print(f"Aktueller Pfad: {current_directory}")

    # Alle .png-Dateien im Verzeichnis durchgehen
    for filename in os.listdir(current_directory):
        if filename.endswith(".webm"):
            old_path = os.path.join(current_directory, filename)
            new_filename = filename.replace(".webm", ".mp3")
            new_path = os.path.join(current_directory, new_filename)

            # Umbenennen der Datei
            try:
                os.rename(old_path, new_path)
                print(f"Die Datei {filename} wurde zu {new_filename} umbenannt.")
            except Exception as e:
                print(f"Fehler beim Umbenennen von {filename}: {e}")
