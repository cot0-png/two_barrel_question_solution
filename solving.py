#python

#该代码非常没用:)


i=input('请指定两个桶各自的容量，用空格分开').split()
goal=eval(input('请指定目标水量'))



i1=[]
for j in i:
    i1.append(eval(j))
i1.sort()
a=i1[0]
b=i1[1]#较大的那个

if a<=0 or b<=0:
    print("请输入合理的容量")
    i=input('请再次指定两个桶各自的容量，用空格分开').split()
    i1=[]
    for j in i:
        i1.append(eval(j))
    i1.sort()
    a=i1[0]
    b=i1[1]#较大的那个



#判断目标水量是否比最大容量的桶大
while goal>b or goal<=0:
    print('目标水量应该比最大容量的桶的容量小！')
    goal=eval(input('请重新指定目标水量'))



def pan(goal):#判定目标是否完成
    if water[b]==goal:
        return 1
water={a:0,b:0}

def rn(a,wt=water):#把桶装满
    wt[a]=a
    print(f'把{a}升的桶装满')

#def ad(a,add,water=water):#加水
#    if water[a]+add>a:
#        return a
#    else:
#        return water[a]+add
#def mi(a,mi,wt=water):#减水
#    if wt[a]-mi<0:
#        return 0
#    else:
#        return wt[a]-mi
def z(a,wt=water):#清空
    wt[a]=0
    print(f'把{a}升的桶清空')

def turn(a,b,wt=water):#从a转移水到b
    if wt[a]>=b-wt[b]:
        wt[a]=wt[a]-b+wt[b];wt[b]=b
        
    elif wt[a]<b-wt[b]:
        wt[b]+=wt[a];wt[a]=0
    print(f'把{a}升桶里的水倒入{b}升桶里\n现在{a}升桶里有{wt[a]}升，{b}升桶里有{wt[b]}升')
    

def solve(a,b,wt=water):
    


    posi=1#判断是否是a与b-a的线性组合
    li=[]
    for y in range(int(b/a)+2):
        l=[]
        for x in range(int(b/(b-a))+2):
            if y*a+x*(b-a)<=b:
                l.append(y*a+x*(b-a))
                if y*a+x*(b-a)==goal:
                    posi=(y,x)
        li.append(l)
    #print(li)
    #print(posi)


    


    posi1=1
        
    if posi==1:
        li=[]
        for y in range(b):#判断是否是y*a-x*b的组合
            l=[]
            for x in range(b):#y:a,x:b
                k=y*a-x*b
                if 0<k<=b:
                    l.append(k)
                    if k==goal:
                        posi1=(y,x)
            li.append(l)
        #print(li)
        #print(posi1)
        if posi1==1:
            return 0
        
        else:
            while pan(goal)!=1:
                rn(a)
                turn(a,b)
                if pan(goal):
                    return 1
                

                if wt[b]==b:
                    z(b)
                    turn(a,b)

                if pan(goal):
                    return 1
     



    

    else:   
        if posi[1]==0:
            while pan(goal)!=1:
                rn(a)
                turn(a,b)
                if pan(goal):
                    return 1

        elif posi[0]==0:
            while pan(goal)!=1:
                rn(b)
                if pan(goal):
                    return 1
        #print(wt)
    
    
                turn(b,a)
                if pan(goal):
                    return 1
        #print(wt)
                if wt[a]==a:
                    z(a)
        #print(wt)
                turn(b,a)
                if pan(goal):
                    return 1
        #print(wt)
        else:
            for i in range(posi[1]):
                rn(b)
                if pan(goal):
                    return 1
        #print(wt)
    
    
                turn(b,a)
                if pan(goal):
                    return 1
            #print(wt)
                if wt[a]==a:
                    z(a)
        #print(wt)
                turn(b,a)
                if pan(goal):
                    return 1
        #print(wt)
            if wt[b]==posi[1]*(b-a):
                for j in range(posi[0]):
                    rn(a)
                    turn(a,b)
                    if pan(goal):
                        return 1
            else:
                turn(b,a)
                for j in range(posi[0]):
                    rn(a)
                    turn(a,b)
                    if pan(goal):
                        return 1
                
    




if solve(a,b):
    print('已完成')
else:
    print('无法完成')
