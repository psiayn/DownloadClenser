# DownloadCleanser

Cleans up Download Folder and sorts the files based on extensions.

Uses default directories on Windows and Linux (the folder inside home directory). If you are on another platform or want to change directories, rename the folders in the python script.

## Features

 - Native support for Windows and Linux
 - Auto creates directories
 - Can be scheduled

# Instructions

Requires `python3` and `crontab` to run
 - Change paths if required (Windows and Linux are natively supported).
 - Run using `python3 sorter.py` or add appropriate shebang (`#!`) and run `./sorter.py`.
 - Use `crontab` to schedule the script to run.
