import array as arr

val=arr.array('i',[1,2,3,4,5,6])
print(val)

for i in range(0,6):
    print(val[i],end=" ")

print('\n')
for x in val:
    print(x,end=",")

