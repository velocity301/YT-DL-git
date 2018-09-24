#Python 3.7.0 version
import os

inputfilename = input('What is your list filename?')
numberofsongs = sum(1 for line in open(inputfilename))
for x in range(0, numberofsongs):
    print ("Now downloading file number",x+1,"of",numberofsongs)
    url=[line.rstrip('\n') for line in open(inputfilename)][x]
    print (url)
    YTID = url.rpartition('=')[2]
    print (YTID)
    os.system('youtube-dl.exe %s' %(url))
#convert to mp3
    contents = os.listdir('.')
    print (contents)
    nameoffile = [s for s in contents if YTID in s][0]
    print (nameoffile)
    os.system('ffmpeg.exe -i \"%s\" -f mp3 -ab 192000 -vn \"%s.mp3\"' %(nameoffile,nameoffile.rpartition('.')[0]))
    os.remove(nameoffile)
