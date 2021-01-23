name_1 = list(input())
name_2 = list(input())
for i in range(len(name_1)-1, -1, -1):
    if name_1[i] in name_2:
        a = name_1.pop(i)
        name_2.remove(a)
no = len(name_1)+len(name_2)
magic = ["f", "l", "a", "m", "e", "s"]
while len(magic) > 1:
    if no > len(magic):
        cross = (no % len(magic))-1
        magic.pop(cross)
        magic = magic[cross:]+magic[:cross]
    elif len(magic) >= no:
        magic.pop(no-1)
        magic = magic[no-1:]+magic[:no-1]
else:
    if magic[0] == "f":
        print("friends")
    elif magic[0] == "l":
        print("love")
    elif magic[0] == "a":
        print("affection")
    elif magic[0] == "m":
        print("marry")
    elif magic[0] == "e":
        print("enemy")
    else:
        print("sibling")
