import subprocess

 
ffmpeg_command = f" ffmpeg -re -i C:\\Users\\cagri\\Downloads\\OverLayedLinkPark.mp4 -f flv \"rtmp://127.0.0.1/live/stream1\""

process = subprocess.Popen(ffmpeg_command, shell=True)