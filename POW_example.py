from hashlib import sha256
x=34
y=0
while sha256(str(x*y).encode()).hexdigest()[-5:-1] != "0000":
    y+=1

print(y)