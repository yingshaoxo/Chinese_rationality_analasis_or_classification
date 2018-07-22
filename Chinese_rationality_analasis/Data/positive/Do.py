def handle_diary(filename):
    with open(filename, 'r') as f:
        text = f.read()

    list_ = text.split('\n\n——————————————\n\n')
    list_ = ['\n'.join(t.split('\n')[1:]).strip('\n ') for t in list_]

    result = '\n\n——————————————\n\n'.join(list_)
    print(result)
    input("Are you sure it is right?")

    with open(filename, 'w') as f:
        f.write(result)

# handle_diary("diary0.txt")


def handle_saying(filename):
    with open(filename, 'r') as f:
        text = f.read()

    list_ = text.split('\n\n——————————————\n\n')
    list_ = [t for t in list_ if (t.strip(" \n") != "") and ("发表图片" not in t) and ("Post Photo" not in t)]

    result = '\n\n——————————————\n\n'.join(list_)
    print(result)
    input("Are you sure it is right?")

    with open(filename, 'w') as f:
        f.write(result)

# handle_saying("saying.txt")


def reverse_txt(filename):
    with open(filename, 'r') as f:
        text = f.read()

    list_ = text.split('\n\n——————————————\n\n')
    list_ = list(reversed(list_))

    result = '\n\n——————————————\n\n'.join(list_)
    print(result)
    input("Are you sure it is right?")

    with open(filename, 'w') as f:
        f.write(result)

reverse_txt("saying.txt")
