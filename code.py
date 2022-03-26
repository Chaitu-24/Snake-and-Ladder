def func(s):
    if s[2]=='E':
        return 100
    elif s[2]=='S':
        return 1
    a=''
    l=['0','1','2','3','4','5','6','7','8','9']
    if s[2] in l:
        a=a+s[2]
    if s[3] in l:
        a=a+s[3]
    a=int(a)
    return a
        
li=list()
j=0
for i in range(10):
    a=list(input().split())
    if j==0:
        li=li+a
        j=1
    else:
        a.reverse()
        li=li+a
        j=0
li.reverse()
#print(li)
di=list(map(int,input().split()))
#print(di)
pos=0
s=0
l=0
for i in di:
    if pos==100:
        break
    pos+=i
    if li[pos-1][0]=='S':
        pos=func(li[pos-1])
        s+=1
    elif li[pos-1][0]=='L':
        pos=func(li[pos-1])
        l+=1
    #print(pos)
if li[pos-1]=='End':
    print(f'Possible {s} {l}')
else:
    print(f"Not possible {s} {l} {pos}")
