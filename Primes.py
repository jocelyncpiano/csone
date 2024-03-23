from math import ceil

def is_prime(num):
    if num==2:
        return True
    for x in range (2, ceil(num**(0.5))+1):
        if num%x==0:
            return False
        else:
            continue
    return True
    

for i in range(1, 100):
	if is_prime(i + 1):
			print(i + 1, end=" ")