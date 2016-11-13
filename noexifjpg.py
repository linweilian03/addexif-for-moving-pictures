# -*- coding: utf-8 -*-
import os,fnmatch
import time
import exifread,piexif
def all_files(root,patterns='*',single_level=False,yield_folders=False):
    patterns = patterns.split(';')
    for path,subdirs,files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)
        files.sort()
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    yield os.path.join(path,name)
                    break
                if single_level:
                    break
                
def read_time(path):
    f=open(path,'rb')
    tags=exifread.process_file(f)
    eDTO=tags.has_key('EXIF DateTimeOriginal')
    #DTG=tags['EXIF DateTimeDigitized']
    #DTO=tags['EXIF DateTimeOriginal']
    # I read more than one EXIF value, but I think Mi only use DTO, so I will use only DTO.
    #IDT=tags['Image DateTime']
    return eDTO

def find_time(path):
    timeinfo=os.stat(path)
    t=time.gmtime(timeinfo.st_mtime)
    gpsdate=time.strftime("%Y:%m:%d",t)
    gpstime=time.strftime("%H:%M:%S",t)
    return gpsdate,gpstime
    
yourpath=input("Enter your path:")

for path in all_files(yourpath,'*.jpg'):
    if not read_time(path):
        print(path),
        print(read_time(path))
        #f=open(path,'rb')
        #image_data=f.read()
        #if image_data[0:2] != b"\xff\xd8":
            #print(path),
            #print(read_time(path))
            #gpsdate,gpstime=find_time(path)
            #os.system("exiftool -DateTimeOriginal='"+find_time(path)+"' -overwrite_original "+path)
            #os.system("exiftool -GPSDateStamp='"+gpsdate+"' -GPSTimeStamp='"+gpstime+"' -overwrite_original "+path)
        #print(read_time(path))
            
