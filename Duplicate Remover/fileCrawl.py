from os import walk, remove, getcwd

music_List = set()
removedSong = open('removedSong', 'w')
badSong = open('badSong', 'w')
badchar = dict()
for (dirpath, dirnames, filenames) in walk('.', False):  
  for song in filenames:
    for char in song:
      if char not in badchar:
        badchar[char] = 1
      else:
        badchar[char] += 1
    if song in music_List:
      print("Deleting" + song + " from " + dirpath)
      remove(getcwd() + dirpath[1:]+"/"+song)
      removedSong.write("Removed: " + song + " from " + dirpath + '\n')      
    else:
      music_List.add(song)

for key in sorted(badchar.iterkeys()):
  badSong.write(key +"\t"+ str(badchar[key]) + "\n")
      
badSong.close()
removedSong.close()




