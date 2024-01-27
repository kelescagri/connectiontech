import subprocess

#kullanım için C:\\Users\\cagri\\Downloads\\LinkinPark.mp4 yerine sizin input video, C:\\Users\\cagri\\Downloads\\OverLayedLinkPark.mp4 yerine de
#istediğiniz bir isimde dizinde video,overlay.txt yerinede sizin oluşturuduğunuz overlay text gelecek. 
ffmpeg_command = f"ffmpeg -re -i C:\\Users\\cagri\\Downloads\\LinkinPark.mp4 -vf  \"drawtext=textfile='overlay.txt':reload=1:fontcolor=white:fontsize=24:fontfile=/Windows/Fonts/Calibri.ttf:box=1:boxcolor=black@0.5:boxborderw=5:x=(w-text_w)/2:y=(h-text_h)/2\" -y C:\\Users\\cagri\\Downloads\\OverLayedLinkPark.mp4"

process = subprocess.Popen(ffmpeg_command, shell=True)
