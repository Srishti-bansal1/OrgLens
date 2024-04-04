f = open("student.csv","r")
r = f.read()
l1 = r.split("\n")
l2 = []
sum_num = 0
sum_all = 0
for idx in range(1,len(l1)):
    row = l1[idx]
    marks = row.split(',')
    l2.append(marks[1])
for el in l2:
    el = float(el)
    sum_num += el

f = open("student.csv","a")

mean = sum_num / len(l2)
f.write("\n")
_mean = ["mean ,",str(mean)]
w = f.write(" ".join(_mean))
#difference = [lambda std_mark = el1: std_mark - mean for el1 in l2 ]
for el1 in l2:
    el1 = float(el1)
    difference = el1 - mean
    square = difference * difference
    sum_all += square

variance = sum_all / (len(l2)-1)
f.write("\n")
_variance = ["variance ,",str(variance)]
w = f.write(" ".join(_variance))

standard_deviation = variance ** 0.5
f.write("\n")
_standard_deviation = ["standard_deviation ,",str(standard_deviation)]
w = f.write(" ".join(_standard_deviation))

f.close()