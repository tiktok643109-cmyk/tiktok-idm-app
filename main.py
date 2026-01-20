import flet as ft
import yt_dlp
import os

def main(page: ft.Page):
    page.title = "TikTok IDM"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    
    url_input = ft.TextField(label="Lien TikTok", hint_text="Colle le lien ici...")
    status = ft.Text()

    def download_video(e):
        if not url_input.value:
            status.value = "❌ Entre un lien !"
            page.update()
            return
            
        status.value = "⏳ Téléchargement en cours..."
        page.update()
        try:
            # Note: Sur Android, l'accès au stockage varie, 
            # yt-dlp téléchargera dans le dossier de l'app par défaut ici
            ydl_opts = {'format': 'best', 'outtmpl': '%(id)s.%(ext)s'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url_input.value])
            status.value = "✅ Vidéo téléchargée !"
        except Exception as ex:
            status.value = f"❌ Erreur : {str(ex)}"
        page.update()

    page.add(
        ft.SafeArea(
            ft.Column([
                ft.Text("🎵 TikTok Downloader", size=25, weight="bold"),
                url_input,
                ft.ElevatedButton("Télécharger", on_click=download_video, icon=ft.icons.DOWNLOAD),
                status
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
    )

ft.app(target=main)

