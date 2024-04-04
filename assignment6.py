def compare_json(d1,d2):
    l1 = []
    l2 = []
    d3 = {}
    for key1 in d1:
        l1.append(key1)

    for key2 in d2:
        l2.append(key2)

    for el in l1:
        if d2.get(el):
            if d1[el] != d2[el]:
                print(d1[el],d2[el])
                if str(d1[el]).isalpha():
                    d3[el] = "Text change"
                else:
                    if d1[el] > d2[el]:
                        difference  = d1[el] - d2[el]
                    else:
                        difference = d2[el] - d1[el]
                        difference = "%.2f"%difference
                    d3[el] = difference        
        else:
            d3[el] = "Only in 1"
    set1 = set(l1)
    key_only_json2 = set(l1+l2)-set(l1)
    for key3 in key_only_json2:
        d3[key3] = "Only in 2"
    return d3

json1 = {
    "x" : 1.0,
    "name" : "ankita",
    "y" : "c",
    "a" : 7
}
json2 = {
    "x" : 1.1,
    "name" : "sri",
    "z" : 100
}
res = compare_json(json1,json2)
print(res)