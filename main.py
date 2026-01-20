import flet as ft
import yt_dlp
import os

def main(page: ft.Page):
    page.title = "TikTok IDM"
    page.theme_mode = ft.ThemeMode.DARK
    
    url_input = ft.TextField(label="Lien TikTok", hint_text="Colle le lien ici...")
    status = ft.Text()

    def download_video(e):
        status.value = "⏳ Téléchargement..."
        page.update()
        try:
            ydl_opts = {'format': 'best', 'outtmpl': '/sdcard/Download/%(id)s.%(ext)s'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url_input.value])
            status.value = "✅ Terminé !"
        except Exception as ex:
            status.value = f"❌ Erreur : {str(ex)}"
        page.update()

    page.add(
        ft.Text("TikTok Downloader", size=25, weight="bold"),
        url_input,
        ft.ElevatedButton("Télécharger", on_click=download_video),
        status
    )

ft.app(target=main)
  
