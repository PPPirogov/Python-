dict_artist = {"aaa": 3, "aab": 2, "bbc": 4, "bbb": 4, "ddd": 1}
b = sorted(dict_artist.items(), key=lambda x: (x[1], x[0]))
for a in b:
    print(a)