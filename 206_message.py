from random import randint as ri

f = open("KOI.txt","r")
a = 0
내용 = f.read()
for i in 내용.split():
    su = 0
    for j in i[:5]:
        su += int(j)**2
    if su%10 == int(i[5]):
        a += 1
print(a)

# f = open("KOI.txt","w")
# for i in range(50000):
#     a = ri(0,999999)
#     f.write(str(a).zfill(6)+"\n")