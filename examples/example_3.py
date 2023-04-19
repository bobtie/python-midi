with open('example.mid',mode='rb') as f:
    s = f.read()
    c = 0
    for x in s:
        print("%02x" % x ,end=' ')
        c += 1
        if c % 16 == 0:
            print()
    print()