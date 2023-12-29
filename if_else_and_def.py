#!/usr/bin/env python
# coding: utf-8

# In[2]:


n= 5
for i in range(n):
    for j in range(0,i+1):
        print("*" , end="")
    print("\r")


# In[9]:


n= 5
for i in range(n):
    for j in range(0,i+1):
        print("Deepak " , end="")
    print("\r")


# In[10]:


n= 5
for i in range(n):
    for j in range(0,i+1):
        print("Deepak " , end="a")
    print("\r")


# In[13]:


n= 5
for i in range(n):
    for j in range(0,i+1):
        print("Deepak " , end="")
    print("\r\r\r") # more closer 


# In[14]:


n= 5
for i in range(n):
    for j in range(0,i+1):
        print("Deepak " , end="")
    print("\n\n\n")


# In[15]:


n= 5
for i in range(n):
    for j in range(0,i+1):
        print("Deepak " , end="")
        print("\r")


# In[16]:


l = [1,2,3,4,5,6,8,9]
for i in l:
    print(i)


# In[19]:


for i in range(len(l)):
    print(i, l[i])


# In[4]:


for i in range(1,5):
    print(i)


# In[20]:


t=(1,2,3,45,6,8)


# In[21]:


t[::-1]


# In[26]:


for i in range(len(t)-1,-1,-1):
    print(t[i])


# In[5]:


d = { "a":"nfjnvfn","b":"egrergyu","c":[1,2,3,4,5],"d":(4,5,6,7),"e":"sudh"}


# In[6]:


d["d"]


# In[12]:


for i in d:
    print(i,d.values())


# In[19]:


d.values()


# In[ ]:





# In[30]:


for i in d:
    print(i,d[i])


# In[32]:


s ={ 2,2,5,8,6,4,4854,5,54,5}


# In[33]:


s


# In[34]:


for i in s:
    print(i)


# In[1]:


# set is unordered elements into the set


# ## itreabale and generater lecture

# In[2]:


# How will able to cont the string


# In[27]:


s="this is the basic python class"
len(s)


# In[28]:


count =0
for i in s:
    #count = count +1
    count+=1
print(count)


# In[29]:


s[::-1]


# In[30]:


## can we return in reverce way? but ot by slicing operation
for i in range(len(s)-1,-1,-1):
    print(s[i])

    


# In[31]:


# but student
i = len(s)-1
while i >= 0:
    print(s[i],end= " ")
    i=i-1


# In[32]:


# we have string find out which is vowel
s= "ineuron"
v="AaEeIiOoUu"


# In[38]:


for i in s:
    print(i)
    if i == "A"or i=="a" or i == "E" or i == "e" or i =="O" or i =="o" or i =="U"  or i =="u":
        print("vowel")
    else :
        print("not vowel")


# In[42]:


s= "ineuron"
v="AaEeIiOoUu"

for i in s:
    if i in v:
        print("vowel",i)
    else :
        print("not voel",i)


# In[45]:


"u" in "sudh"


# In[46]:


# pelendrom strings :- both direction same
"tnent"
"malayalam"
"eye"


# In[62]:


#easy
s= input()
v =s[::-1]
if s == v:
    print("its pandroms")
else:
    print("not pandroms")


# In[63]:


# dictionary with us filter out wether we have lenth of key greter than 5 or less than 3 

d ={"india":"IN",
   "canada": "CA",
   "china":"CH",
   "united state":"US"
   }


# In[65]:


d.keys()


# In[71]:


list1=[]
list2 =[]

for i  in d:
    if len(i) <= 5:
        list1.append(i)
    else :
        list2.append(i)


# In[72]:


list1


# In[73]:


list2


# In[75]:


d1 = {"ineuron" : {
                        "a":14,
                        "b":10,
                        "c" : 4
                    },
      "course":{
                    "d":45,
                    "e":34,
                    "f":1
                    }
}


# In[82]:


for i  in d1.values():
    for j in i.values():
        print(j)


# ## Function part 1

# In[83]:


def  test():
    pass
    


# In[84]:


def test1():
    print("this my first function")


# In[87]:


test1()


# In[90]:


test1()+"sudh"


# In[91]:


# by default we got nonetype
str(test1())


# In[88]:


def test2(X,y):
    c=X**2 +y**2
    return c
    


# In[89]:


test2(5,4)


# In[96]:


type(test2(5,4))


# In[92]:


def test3():
    return "this my first function"


# In[93]:


test3()


# In[94]:


type(test3())


# In[97]:


def test4():
    k=5*2
    return k


# In[98]:


test4()


# In[99]:


type(k)


# In[100]:


test4 + "Deep"


# In[101]:


def test5():
    return 10


# In[104]:


type(test5())


# In[109]:


def test6():
    return 2,3,4,["sudh",1,3,5,7]
## bydefault it give us the tuples


# In[110]:


test6()


# In[111]:


type(test6())


# In[112]:


#  we want hold all object into other other varible
a,b,c,d = test6()


# In[113]:


a


# In[114]:


b


# In[115]:


c


# In[116]:


d


# In[117]:


def test7():
    a =6*7/6
    return a


# In[119]:


test7()


# In[121]:


type(test7())


# In[1]:


l =[1,2,3,45,7,8,"deep",[1,2,3,4]]


# In[2]:


def test8(a):
    n = []
    if type(a) == list:
        for i in a:
            if type (i) == int:
                n.append(i)
    return n
    


# In[3]:


test8(l)


# In[5]:


type(test8(l))


# In[7]:


test8([2,3,4,5,56,6,[1,4,5,7,9],"Deepak",4.3])


# In[9]:


a= {"a":4,"b":5}


# In[10]:


type(a)


# In[11]:


X= input("Enetr your key")
y =input("Enter your values")
k ={X:y}


# In[18]:


def dicfuction(c):
    if type(c) ==dict:
        k =c.keys()
        
    return k


# In[19]:


d ={"a":45,"b":45}


# In[20]:


dicfuction(d)


# In[21]:


def triagle(row):
    if type(row) == int:
        for i in range(1 ,row):
            for j in range(i-1 , row):
                print("*",end=" ")
            print("\n")
            
                


# In[22]:


triagle(6)


# In[22]:


def triagle1(row):
    if type(row) == int:
        for i in range(1 ,row):
            for j in range(i ):
                print("*",end=" ")
            print("\n")
            


# In[23]:


triagle1(6)


# # fuction 2

# In[48]:


def test1(a,b,c,d):
    return a,b,c,d


# In[49]:


test1(2,3,5,5)


# ### when we want pass more arguments into fuction than use
# - *args - any number of arguments or n number of variable we pass it

# In[50]:


def test2(*args):
    return args


# In[51]:


test2(45,35,"Deepak",1.3)


# In[53]:


test2([1,2,4,5],"deepak","sshbhbfdh",1,4,5,7,{1,4,6,8,4})


# In[54]:


def test3(*args,a): #any varible + any specific variable
    return args,a


# In[57]:


test3(34,58,95)


# In[58]:


test3(34,58,95,a=5)


# In[59]:


def test5(*args , a,b,c,d):
    return args,a,b,c,d


# In[60]:


test5("Deepak",1,4,5,6 ,a=45,b="kumar",c=45,d=1.3)


# In[1]:


def test6(a,*args):
    return args ,a
## this is not working


# In[2]:


test6("deepka","kumar",1,4, a=2)


# ### when you give any varible in the starting of the fuction that time it will consider first element by defalut and other will be args

# In[3]:


test6("deepak",1,23,4,5,[1,3,5,6,7])


# In[6]:


test6("deepak",1,23,4,5,[1,3,5,6,7])


# In[7]:


def test(a,*args,b,c):
    return a,b,args,c


# In[8]:


test(1,2,3,4,5)


# In[9]:


test(1,2,3,4,5,b=2,c="Deepak")


# In[10]:


## argument always goes to take tuples


# In[11]:


def listcheck(*args):
    for i in args:
        if type(i) == list:
            return i
        continue


# In[12]:


listcheck(1,2,3,3,[1,3,4,5,6,6])


# In[13]:


listcheck(1,2,3,3,[1,3,4,5,6,6],[3,5,6,79])


# In[23]:


def listcheck(*args):
    l1 = []
    for i in args:
        if type(i) == list:
            l1.append(i)
    return l1


# In[24]:


listcheck(1,2,3,3,[1,3,4,5,6,6],[3,5,6,79])


# ## kwargs - key word arguments
# ### when we need to make key value pair fuction that time we use double staric key word arguments(**kwargs) its not reserve key work we take any name in place of kwargs

# In[33]:


def test1(**kwargs):
    return kwargs
    


# In[34]:


test1(325,2,5,15,1,5,4)


# In[35]:


test1(a= 345, b= [1,3,4])


# In[36]:


def test3(**Deep):
    return Deep


# In[37]:


test3(a=1,v=3,f=[1,3,5,8])


# In[38]:


test3("a"=1'v'=3)


# In[39]:


# here we doen't need to do into sting or any other form


# In[40]:


test3(3 = "hbhd")


# In[1]:


def info(**kwargs):
    return kwargs


# In[2]:


info(name=input("Enter your name"),age = input("age"),number = input("number"),email = input("emial"))


# In[4]:


def test(a ,**k):
    return a,k


# In[6]:


test(45,a=3,b=4,c=9)
#why error because of the a use first elements by default


# In[8]:


def test1(a,*args, **kwargs):
    return a,args,kwargs


# In[9]:


test1(2,445,35,56,34,35,f=34,g=34)
# it will work 


# In[11]:


def test2(a,**kwargs,*args):
    return a,args,kwargs

## it will give us the error because of the arrangements of arguments


# ### here we can say that arrangements also be big factor

# In[12]:


def test3(a,b):
    return a*b


# In[13]:


test3(2,6)


# ## lambda :- lambda is the anomanous fuction

# In[15]:


# can you create fuction without the name or function


# In[17]:


a=lambda a,b : a * b


# In[18]:


a(6,2)


# In[19]:


b =lambda a,b,c,d : a*b+c -d


# In[20]:


b(2,25,10,10)


# In[25]:


a=lambda *a :a


# In[26]:


a(2,5,8)


# ## when we try to create function or lembda function both are same
# 
# #### but when we want to written one line code function that time we use lambda other than that we use def

# In[2]:


a=lambda *a :a*10
# in this case it will using a as the tuples that why they not work like to multiplication


# In[5]:


a(10,20)  


# In[16]:


a = lambda *a : (a+a )


# In[17]:


a(5,3)


# In[18]:


x =lambda x:print(i) for i in x


# In[35]:


x =lambda x: [print(i) for i in x]


# In[36]:


x([1,2,3,4])


# In[37]:


x =lambda *x: [i for i in x]


# In[38]:


x([1,2,3,4],(2,3,38))


# In[39]:


y =lambda *x: [print(i) for i in x ]


# In[42]:


y([1,2,3,4],(2,3,38),{1,2,34,3})


# In[43]:


a= 10
def test1(c,d):
    return c*d


# In[45]:


test1(a,5)


# In[52]:


a= 10
def test2(c,d):
    c=5  # local variable
    return c*d


# In[49]:


test2(10,10)


# In[51]:


a


# ## Comprihension operation

# In[55]:


l =[1,3,4,5,6,7,89,9]
l1=[]
for i in  l:
    i=i+2
    l1.append(i)
print(l1)


# In[62]:


def test2(a):
    l1= []
    for i in a:
        l1.append(i+2)
    return l1
            


# In[63]:


test2([1,2,3])


# In[65]:


a =lambda a : [i+2 for i in a]


# In[66]:


a(l)


# In[67]:


[(i**2,i+i) for i in l if i<4]


# In[69]:


[(i**2,i+i) for i in l if i<8 if i>6]


# In[72]:


[{i:i**2} for i in range(10)]


# In[77]:


{i:i**2 for i in range(10)}


# In[75]:


d1= {}
for i in range(10):
    d1[i] = i**2
   


# In[76]:


d1


# # iterables iterattres and generator

# In[2]:


a= 56
for i in a:
    print(a)


# In[5]:


a="sudh"
for i in a:
    print(i)
## its means string is iterable


# In[4]:


next(a) #but here


# In[ ]:


## Difference betwen iterable and itretor

#string is a iterable but string is not iterator


# #### if an object is holding a values with the help of some short of indexes and if you are able to excess it one by one with the help of indexes that type of object is called iterable object 
# iterable object is a kind of object which you will be able to process with the help of some squares and some statement in any languages which i will be excess but it does'nt mean it doesn't means it is iteretor its look like iteretor but no string is iterable and for loop is some thing which is trying to create this string as iterator
# 

# In[1]:


## next :-will always give you the one one value of the iterator but string is not iteretor


# In[8]:


a=iter(a) # iter fuction be able to convert iterable to iteretor


# In[9]:


next(a)


# In[11]:


next(a)


# In[12]:


s ="fdfmfjn"
for i in s:
    print(i)


# In[42]:


def for_loop(a):
    while type(a) == str:
        
        a=iter(a)
        
        print(next(a))
        
        continue
       
        
        


# In[43]:


for_loop("Deep")


# In[28]:


l = [1,3,4,6,7]


# In[29]:


next(l)


# ### only iterable elemenst we are going to convert into the iteretor

# In[31]:


l


# In[32]:


l=iter(l)


# In[33]:


next(l)


# In[34]:


next(l)


# In[44]:


## all iterable are iterator we are able to convert


# # Generator:

# ### generator a kind of object which allows you to hold a information about the precious dataset that you have generated and logic which you generated in previous dataset  based on that you will able to generated next data 

# In[45]:


range(45)


# In[46]:


list(range(0,45,3))


# In[ ]:


## generator need to undersatand only the previous data they make next


# In[56]:


# gerenate a cube
def gencube(n):
    for i in range(n):
        return i**3
       
          


# In[57]:


gencube(3)


# In[64]:


def gencube(n):
    l = []
    for i in range(n):
        l.append(i**3)
    return l


# In[65]:


gencube(10)


# In[24]:


# other way :- "yield" :-yield is use as the function  convert into generator
def gencube1(n):
    for i in range(n):
        yield i**3


# In[25]:


gencube1(10) ##tell us the generator


# In[70]:


for i in gencube1(10):
    print(i)


# In[71]:


# yield is able to help you to does not use complete memory that time we use yield.
# yield is able to work like range function


# In[ ]:


## 0,1,1,2,3,5,8,13,21....(fibonacci sequence)


# In[75]:


def fib(n):
    a=1
    b=1
    for i in range(n):
        yield a,i
        a,b = b,a+b


# In[79]:


for i in fib(10):
    print(i)
   


# In[92]:


def fuc(n):
    k=4
    for i in range(n):
        print(i)
    return i


# In[91]:


fuc(5)


# In[93]:


def feb1(n):
    a=1
    b=1
    output = []
    for i in range(n):
        print(i)
        output.append(a)
        a,b = b,a+b
    return output
        
        


# In[94]:


feb1(10)


# In[100]:


def fuc(n):
    for a in range(n):
        print(a)
        a=a+1
        for b  in range(n):
            print(b)
            b= b+1
            
    return a,b = b,a+b
        
    


# In[101]:


def fuct(n):
    a=0
    b=[]
    for i in range(n):
        b.append(a)
    return b


# In[102]:


fuct(10)


# In[105]:


def feb1(n):
    a=1
    b=1
    output = []
    for output i range(n):
        output.append(a)
        a,b = b,a+b
    return output
        


# In[104]:


feb1(5)


# In[ ]:


## look onece yield any other place


# ## File system - basic

# In[2]:


print("Something in console")


# In[3]:


# if we want to store some thing in file for permanents


# In[4]:


f=open("test.txt","w")


# In[9]:


ls


# In[7]:


pwd()


# In[10]:


get_ipython().run_line_magic('ls', '')


# In[11]:


f.write("this is first operation diectory i used to do python practical revision")


# In[13]:


f.close()


# In[14]:


get_ipython().run_cell_magic('writefile', 'test1.txt', 'this is the data i would like to store code\n')


# In[16]:


# here it use bydefault as close


# In[15]:


get_ipython().run_line_magic('ls', '')


# In[17]:


f = open("test.txt")


# In[18]:


f.read()


# In[19]:


f.write("hbhdbhbdskjnfdhbfd")


# In[21]:


f.read() # we got empty because our curser on last place of the written file


# In[22]:


#if we  want to reset our curser than we use below fuction

f.seek(5) # fift position


# In[23]:


f.read()


# In[24]:


f.read()


# In[25]:


f.seek(0)


# In[26]:


f.read()


# In[27]:


# check cursur where has 

f.tell() #at 71 position


# In[28]:


f.seek(5)


# In[29]:


f.tell()


# In[30]:


f.close()


# In[34]:


f =open("test.txt","r+") # r+ mode:-


# In[35]:


f.read()


# In[36]:


f.read()


# In[37]:


f.readlines()


# In[38]:


f.tell()


# In[39]:


f.seek(0)


# In[40]:


f.readlines()


# In[41]:


f.read()


# In[42]:


f.seek(0)


# In[43]:


f.read() ## this is use for hole data


# In[48]:


f.seek(0)


# In[49]:


f.readlines() ## this is use for line by line data


# In[50]:


f.close()


# In[51]:


f=open("test.txt","r+")
for line in f:
    print(line,end = " ")
    
#we are able to see clearly line by line


# In[53]:


f.write("sabhdbdbas")  # here we able to write somthing because of "r+" mode


# In[54]:


f.close()


# In[56]:


## can we find an word and replace with that word


# In[57]:


f=open("test.txt","r+")


# In[58]:


f.readlines()


# In[64]:


f.seek(0)


# In[61]:


len(f.readlines())


# In[65]:


l = f.readlines()


# In[69]:


l[0].split()


# In[70]:


## for first correcter of all the words
l1 =[]
for i in l[0].split():
    l1.append(i[0])


# In[71]:


l1


# In[72]:


f.close()


# In[73]:


get_ipython().run_line_magic('ls', '')


# In[76]:


f=open("test.txt","r+")
f.name


# In[77]:


l =["line 1","line 2","line 3","line 4"]


# In[78]:


f.write("i can write line in current cursor")


# In[79]:


f.writelines(l)


# In[80]:


f.close()


# In[81]:


f=open("test.txt","r+")
f.fileno()


# In[83]:


f.close()


# In[82]:


get_ipython().run_line_magic('ls', '')


# In[84]:


# when we want to delete or remove that time

import os

os.remove("test1.txt")


# In[85]:


get_ipython().run_line_magic('ls', '')


# In[87]:


os.getcwd()
#current working directory


# In[90]:


pwd()


# In[89]:


os.listdir()


# In[ ]:




