i = 1
result = 1
while i <= 100:
    result *= i
    if i == 42:
        print(f" the magic number is reached {i}")
        break                    # stopping the loop 
    i += 1
print("i = ", i)
print("result = ", result)
