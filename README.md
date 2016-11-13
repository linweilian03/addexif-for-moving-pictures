# addexif-for-moving-pictures
This is a very special repository. It is very simple and easy, and I just used it to solve the problem that pictures will not be order normally in copying the old picture to a new smartphone.
The problem is that many pictures had no exif informations, and when they is moved to the newphone. Their modification time is always the time you moving the picture.
So this script help me to solve problem. It will find all jpg files in the dir, then if the picture has no exif information, it will add the exif information by using the modification time in the computer. And my Mi smartphone use the GPS Date and GPS Time to conclude when this picture is taken. So this script will just add the GPSDate and GPSTime tags.

Usage:
If you want to use this script, my advice is that you should read the codes and know what they are doing.
You should edit the DIR name for your own case. Then, this script require the python moudle "piexif.py" and command line tool exiftool.

I use it only on my computer, Ubuntu 16.04, linux.
