for i in range(1,10):
    for j in range(1,10):
        if j > i:
            continue
        elif j < i:
            print("{} * {} = {}\t".format(j,i,i*j),end="")
        else:
            print('{} * {} = {}'.format(i , j, i * j))