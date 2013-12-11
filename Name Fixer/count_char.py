from os import walk, remove, getcwd
import operator

music_List = set()
charFile = open('charFile', 'w')
charCount = dict()

badChars = ['#','@','!',']','[','+','&','_']

for (dirpath, dirnames, filenames) in walk('.', False):  
  for song in filenames:
    for char in song:
      if char not in charCount:
        charCount[char] = 1
      else:
        charCount[char] += 1
    for char in badChars:
      if (char in song) and ("AlbumArt" not in song):
        print(song+"\t"+dirpath)

    music_List.add((dirpath, song))

for key in sorted(charCount.iterkeys()):
  charFile.write(key +"\t"+ str(charCount[key]) + "\n")

charFile.write('\nSorted By value\n')

for pair in sorted(charCount.iteritems(), key=operator.itemgetter(1)):
  charFile.write(str(pair[0]) + "\t" + str(pair[1]) +"\n")

charFile.close()





