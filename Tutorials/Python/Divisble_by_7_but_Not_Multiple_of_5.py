result=[]

for num in range(2000, 3201):
    if num%7==0 and num%5!=0:
        result.append(num)
    
print(", ".join(map(str,result)))