f = open("string.txt","r")
r = f.read()
l1 = r.split("\n")
n = l1[1]
l2 = []
for el in l1[0]:
    ascii_val = ord(el)
    ascii_val += int(n)
    if 97 <= ascii_val <= 122:
        character = chr(ascii_val)
        l2.append(character)
    else:
        ascii_val -= 97
        ascii_val %= 26
        encrypt = ascii_val + 97
        character = chr(encrypt)
        l2.append(character)

encrpt_string = "".join(l2)
f = open("string.txt","a")
w = f.write("\n")
_encrpt_string = ["Encrypted string : ",encrpt_string]
w = f.write("".join(_encrpt_string))
f.close()