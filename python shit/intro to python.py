"""data type"""
#boolean
w = True
f = False
#int
x = 0
#string
y = "string"
#dab on java/list
z = [x,y]
shit = [[x,y],[w,f]]
print (shit)
print (shit[0][1])
#dictionary
a = {"chunk":"fat slob","Micheal Wirsing":"smart skinny pilot dude","Daniel Cutler":"skinny fuck that cant gain weight"}
print(a["chunk"])
#tuple / aka dumb list / aka list
b = (x,y)
#float / decimal number = automatic float
c = float(x)

"""function"""
def addition(x,y):
    return x+y

print (addition(3,5))

"""objects"""
class tank:
    def __init__(self):
        self.gun = None
        self.engine = None
        self.hp = 0
        self.speed = 14
class type5heavy(tank):
    def __init__(self):
        super().__init__()
x = type5heavy()

print (x.hp)

"""for loops"""
temp = []
for i in range(10):
    temp.append(type5heavy())

for item in temp:
    item.hp = 3200

"""while loops"""

asdf = 0
while asdf < 5:
    print(a["chunk"])
    asdf += 1

while True:
    asdf += 1
    if asdf > 20:
        break
print (asdf)

"""control flow"""
if w:
    print (w)
elif f:
    print (f)
else:
    print ("your fucked")

dab = ""
while dab != "e":
    dab = input("java haters")
    print (dab)


