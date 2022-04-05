import array as arr

def rotate_list(arr,d,n):
    arr[:] = arr[d:n]+arr[:d]
    return arr

name_1 = input("Enter Your Name: ").lower()
name_2 = input("Enter Your Crush Name: ").lower()
name_1_arr = arr.array('i', [0]*26)
name_2_arr = arr.array('i', [0]*26)
flames = ['Friends','Love','Affection','Marriage','Enemy','Sister']
count = 0

for i in name_1:
    name_1_arr[ord(i)-ord('a')]+=1
for i in name_2:
    name_2_arr[ord(i)-ord('a')]+=1

for i in range(26):
    diff = name_1_arr[i]-name_2_arr[i]
    if diff == 0:
        continue
    else:
        count+=abs(diff)

for i in range(5):
    pos = count%len(flames)
    flames = rotate_list(flames,pos,len(flames))
    flames.pop()
    
result = "".join(flames)
print(result)