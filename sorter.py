#!/usr/bin/env python3
import os
import shutil
from pathlib import Path
import platform

# Auto create directories

home_dir = Path.home()

if platform.system() == "Windows" or platform.system() == "Linux":
    downloads = home_dir / "Downloads"
    images_dir = home_dir / "Pictures" / "Downloads"
    videos_dir = home_dir / "Videos" / "Downloads"
    isos_dir = home_dir / "Downloads" / "ISOs"
    zips_dir = home_dir / "Downloads" / "Zips"
    music_dir = home_dir / "Music" / "Downloads"
    documents_dir = home_dir / "Documents" / "Downloads"
    installers_dir = home_dir / "Downloads" / "Installers"
elif platform.system() == "Darwin":
    downloads = home_dir / "Downloads"
    images_dir = home_dir / "Pictures" / "Downloads"
    videos_dir = home_dir / "Movies" / "Downloads"
    isos_dir = home_dir / "Downloads" / "ISOs"
    zips_dir = home_dir / "Downloads" / "Zips"
    music_dir = home_dir / "Music" / "Downloads"
    documents_dir = home_dir / "Documents" / "Downloads"
    installers_dir = home_dir / "Downloads" / "Installers"
else:
    # add paths manually
    downloads = "/path/to/downloads"
    images_dir = "/path/to/images"
    videos_dir = "/path/to/videos"
    isos_dir = "/path/to/isos"
    zips_dir = "/path/to/zips"
    music_dir = "/path/to/music"
    documents_dir = "/path/to/documents"
    installers_dir = "/path/to/installers"

os.chdir(downloads)

print(os.getcwd())

files = os.listdir()

os.makedirs(images_dir, exist_ok=True)
os.makedirs(videos_dir, exist_ok=True)
os.makedirs(isos_dir, exist_ok=True)
os.makedirs(zips_dir, exist_ok=True)
os.makedirs(music_dir, exist_ok=True)
os.makedirs(documents_dir, exist_ok=True)
os.makedirs(installers_dir, exist_ok=True)

images_exts = [".jpeg",".gif",".png",".jpg",".svg"]
videos_exts = [".webm",".mpg",".mp2",".mpeg",".mpe",".mpv",".ogg",".mp4",".m4p",".m4v",".avi",".mov",".qt",".flv",".swf",".avchd"]
isos_exts = [".iso"]
documents_exts = [".doc",".docx",".html",".htm",".odt",".pdf",".xls",".xlsx",".ods",".ppt",".pptx",".odp",".txt",".pages",".key"]
zips_exts = [".tar",".tar.gz",".tar.Z",".tar.xz","tar.bz2",".bz2",".gz",".7z",".zip",".rar"]
music_exts = [".wav",".m4a",".mp3",".wma"]
installer_exts = [".deb", ".rpm", ".exe", ".sh", ".dmg", ".app"]


for file in files:
    filename, file_ext = os.path.splitext(file)
    if(file_ext in images_exts):
        shutil.move(os.path.join(downloads,file),os.path.join(images_dir,file))
    elif(file_ext in videos_exts):
        shutil.move(os.path.join(downloads,file),os.path.join(videos_dir,file))
    elif(file_ext in isos_exts):
        shutil.move(os.path.join(downloads,file),os.path.join(isos_dir,file))
    elif(file_ext in documents_exts):
        shutil.move(os.path.join(downloads,file),os.path.join(documents_dir,file))
    elif(file_ext in zips_exts):
        shutil.move(os.path.join(downloads,file),os.path.join(zips_dir,file))
    elif(file_ext in music_exts):
        shutil.move(os.path.join(downloads,file),os.path.join(music_dir,file))
    elif(file_ext in installer_exts):
        shutil.move(os.path.join(downloads,file),os.path.join(installers_dir,file))
