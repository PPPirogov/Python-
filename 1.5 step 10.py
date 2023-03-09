class Song:


    def __init__(self,artist,song):
        self.artist = artist
        self.song=song
        self.tags=[]
    def add_tags(self,*args):
        self.tags.extend(args)

song1 = Song("Shakey Graves","Roll the Bones")
song1.add_tags("Americana","Country")
song1.add_tags("DE","DE")

song2 = Song("Neuromonah Feofan","Holodno v lesu")
song2.add_tags("Russian","Drum 'n'base")

song3 = Song("dfds","Bab")
song3.add_tags("Americana","Country")

print(song1.tags)
print(song2.tags)

print