def notes(amount):
    d1 = {}
    l1 = [2000,500,200,100,50,20,10,5,2,1]
    for el in l1:
        count = 0
        while amount >= el :
            amount = amount - el
            count +=1
        if count > 0:
            d1[el] = count
        else:
            d1[el] = 0
    return d1

x = int(input("enter the amount :"))
num_note = notes(x)
print(num_note)