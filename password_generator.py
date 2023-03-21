import random

passlen = int(input("Enter your password length :"))
s = "jkgdrytlweghiuwehiweuhfdw740194-1<><??<?<<<<<?!@#$%^&*()(*&^%$#"
p = "".join(random.sample(s, passlen))
print(p)
