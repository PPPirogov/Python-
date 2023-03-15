with open('test_append') as ta,open('test_write','a') as tw :
    for line in ta:
        tw.write(line)
        print(line)
    # for a in tw:
    #     print(a)