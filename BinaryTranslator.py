def textToBinary(text: str, sep: str=' '):
    list = []

    for i in text:
        asc = ord(i)
        list.append("{0:b}".format(asc))

    return(sep.join(list))

def binaryToText(text: str, sep: str=' '):
    list = text.split(sep)

    newList = []

    for i in list:
        bits = i
        n = int(bits, 2)
        newList.append(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())

    return (''.join(newList))