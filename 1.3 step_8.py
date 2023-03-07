def closest_mod_5(x):
    y = x
    for a in range(5):
        if y % 5 == 0:
            return y
        y+=1
print(closest_mod_5(91))