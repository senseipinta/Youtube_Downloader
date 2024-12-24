import sys
from yt_dlp import YoutubeDL
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox, StringVar

def download_audio(url, download_path):
    """
    Download a YouTube video from the given URL to the specified download path.
    """
    try:
        ydl_opts = {
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',
            'format': 'bestaudio[ext=m4a]',  # Ensure we're downloading the best audio in m4a format
            'ffmpeg_location': r'C:\ProgramData\chocolatey\lib\ffmpeg\tools\ffmpeg\bin',  # Path to FFmpeg folder
        }
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            messagebox.showinfo("Success", f"Title: {info.get('title')}\nDownload completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_download_path():
    """
    Open a dialog for the user to select the download path.
    """
    path = filedialog.askdirectory()
    if path:
        download_path_var.set(path)

def start_download():
    """
    Start the download process using the URL and selected path.
    """
    url = url_entry.get()
    download_path = download_path_var.get()
    
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return
    if not download_path:
        messagebox.showerror("Error", "Please select a download path.")
        return
    
    download_audio(url, download_path)

def create_gui():
    """
    Create the GUI window for the application.
    """
    root = Tk()
    root.title("YouTube Audio Downloader")
    
    # URL input
    url_label = Label(root, text="Enter YouTube URL:")
    url_label.pack(padx=10, pady=5)
    
    global url_entry
    url_entry = Entry(root, width=50)
    url_entry.pack(padx=10, pady=5)
    
    # Download path input
    global download_path_var
    download_path_var = StringVar()
    
    download_path_label = Label(root, text="Select Download Path:")
    download_path_label.pack(padx=10, pady=5)
    
    download_path_entry = Entry(root, textvariable=download_path_var, width=50)
    download_path_entry.pack(padx=10, pady=5)
    
    browse_button = Button(root, text="Browse...", command=select_download_path)
    browse_button.pack(padx=10, pady=5)
    
    # Start download button
    download_button = Button(root, text="Download", command=start_download)
    download_button.pack(padx=10, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
