print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((x == (y<=z))and(y == (not(z<=w)))):
                    print(x, y, z, w, '0')
                if (x == (y<=z)and(y == (not(z<=w)))):
                    print(x, y, z, w, '1')

