# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if not((x and not y) or (x == z) or not w):
#                     print(x, y, w, z)
print("x y z w F")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not((z == (x <= w)) and (x == (not(w <= y)))):
                    print(x, y, z, w, '0')

                if (z == (x <= w)) and (x == (not(w <= y))):
                    print(x, y, z, w, '1')
        print('----------')

