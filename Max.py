import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from yt_dlp import YoutubeDL

def download_video(url, download_path):
    """
    Download a YouTube video from the given URL to the specified download path.

    Args:
        url (str): The URL of the YouTube video to download.
        download_path (str): The path where the video will be downloaded.

    Returns:
        None
    """
    try:
        ydl_opts = {
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Output template
            'format': 'bestvideo+bestaudio/best',  # Select the highest quality video and audio, and merge if needed
            'ffmpeg_location': r'C:\ProgramData\chocolatey\lib\ffmpeg\tools\ffmpeg\bin\ffmpeg.exe',  # Make sure this points to ffmpeg.exe
        }
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            messagebox.showinfo("Download Complete", f"Title: {info.get('title')}\nViews: {info.get('view_count')}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_folder():
    """
    Opens a file dialog to select the download folder.
    """
    folder = filedialog.askdirectory()
    if folder:
        download_path_var.set(folder)

def on_download_click():
    """
    Executes the download process when the "Download" button is clicked.
    """
    url = url_entry.get()
    download_path = download_path_var.get()

    if not url:
        messagebox.showwarning("Input Error", "Please enter a YouTube URL.")
        return

    if not download_path:
        messagebox.showwarning("Input Error", "Please select a download folder.")
        return

    download_video(url, download_path)

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x300")

# URL Entry Label and Field
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)

# Download Path Label and Folder Picker
download_path_var = tk.StringVar()
download_path_label = tk.Label(root, text="Select Download Folder:")
download_path_label.pack(pady=10)
download_path_button = tk.Button(root, text="Browse", command=select_folder)
download_path_button.pack(pady=5)
download_path_display = tk.Label(root, textvariable=download_path_var, width=60, anchor="w")
download_path_display.pack(pady=5)

# Download Button
download_button = tk.Button(root, text="Download", command=on_download_click)
download_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
