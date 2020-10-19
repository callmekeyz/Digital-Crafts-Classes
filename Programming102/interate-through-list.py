my_children = ["Lyric","Jordan"]

index = 0

while index < len(my_children):
    print(index,my_children[index])
    index += 1

    for child in my_children:
        print(index,child)
        index += 1