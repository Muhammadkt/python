expense=[1000,2000,3000,4000,5000]
total=0
for item in expense:
    total=total+item
print(total)    
for i in range(len(expense)):
    print("Month:",(i+1),"Expense:",expense[i])
    total=total+expense[i]
print("Total expense is:",total)

print("***************************************************************************")


key_location="chair"    
locations=["garage","living_room","chair","closet"]
for i in locations:
    if i== key_location:
        print("key is found in",i)
        break
    else:
        print("key is not found in ",i)

print("***************************************************************************")        

for i in range(1,6):
    if i%2==0:
        continue
    print(i*i)
print("***************************************************************************")    

i=0
while i<=5:
    print(i)
    i=i+1



