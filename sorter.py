#!/usr/bin/env python3
import os
import shutil

#Doesn't auto create folder 

#rename paths

downloads = "/path/to/downloads"

os.chdir(downloads)

print(os.getcwd())

files = os.listdir()

images_dir = "/path/to/images"
videos_dir = "/path/to/videos"
isos_dir = "/path/to/isos"
zips_dir = "/path/to/zips"
music_dir = "/path/to/music"
documents_dir = "/path/to/documents"

images_exts = [".jpeg",".gif",".png",".jpg",".svg"]
videos_exts = [".webm",".mpg",".mp2",".mpeg",".mpe",".mpv",".ogg",".mp4",".m4p",".m4v",".avi",".mov",".qt",".flv",".swf",".avchd"]
isos_exts = [".iso"]
documents_exts = [".doc",".docx",".html",".htm",".odt",".pdf",".xls",".xlsx",".ods",".ppt",".pptx",".odp",".txt"]
zips_exts = [".tar",".tar.gz",".tar.Z",".tar.xz","tar.bz2",".bz2",".gz",".7z",".zip",".rar"]
music_exts = [".wav",".m4a",".mp3",".wma"]


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