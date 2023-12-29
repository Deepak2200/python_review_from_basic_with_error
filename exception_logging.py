#!/usr/bin/env python
# coding: utf-8

# # Exception handling

# In[1]:


a=5
a/10


# In[3]:


a/0 ##after this code will not run that why we use exception handling
print('this is my code')


# In[6]:


f=open("text.txt","r")
f.write("shjbhdkjfdmlflkrfnjfm")


# In[7]:


### that type of error we resolve by exception 


# In[10]:


try:
    f=open("test.txt","r")
    f.write("cbchbcxbbc")
except:
    print("there was mistake")
print("this is my code")


# In[11]:


# this will not resolve your sytax problem

l=[4,5,6,7,8,9,0]
try:
    for i  range(len(l)):
        print(l)
except:
    print("this is my code")


# In[12]:


l=[4,5,6,7,8,9,0]
try:
    for i in range(len(l)):
        print(l)
except:
    print("this is my code")


# In[14]:


l=[4,5,6,7,8,9,0]
for i in range(len(l)+1):
    print(l[i])


# In[13]:


l=[4,5,6,7,8,9,0]
try:
    for i in range(len(l)+1):
        print(l[i])
except:
    print("this is my code") 

# here except block also written bcoz here got error in last value


# In[15]:


l=[4,5,6,7,8,9,0]
try:
    for i in range(len(l)+1):
        print(l[i])
except Exception as e:
    print(e)
    print("this is my code") 


# In[17]:


try:
    a=int(input())
    b=int(input())
    c=a/b
    print(b)
except Exception as e:
    print("there has happen some error " ,e)


# In[19]:


try:
    a=int(input())
    b=int(input())
except Exception as e:
    print(e)
print("fndfhbhdn")


# ### exception is the super class of the error

# ## subclass of exception

# In[20]:


try:
    d={"key1":"Deep","key2":[1,2,3,4,5],"key3":(4,5,6,7,8,9)}
    d["key4"]= int(input())
except Exception as e:
    print(e)


# In[22]:


# subclass:-error like same as they are
try:
    d={"key1":"Deep","key2":[1,2,3,4,5],"key3":(4,5,6,7,8,9)}
    d["key4"]= int(input())
except ValueError as e:
    print(e)


# In[23]:


# here we are not able to handle the error by except block why?
## because here i was give the command to except block only this type of
## error show into except that why Exception in catch block give us the proper handler
try:
    d={"key1":"Deep","key2":[1,2,3,4,5],"key3":(4,5,6,7,8,9)}
    d["key4"]= int(input())
    f=open("test","r")
except ValueError as e:
    print(e)


# In[24]:


try:
    d={"key1":"Deep","key2":[1,2,3,4,5],"key3":(4,5,6,7,8,9)}
    d["key4"]= int(input())
    f=open("test","r")
except ValueError as e:
    print(e)
    
#here not poblem


# In[25]:


#here they handle all look here same code will run
try:
    d={"key1":"Deep","key2":[1,2,3,4,5],"key3":(4,5,6,7,8,9)}
    d["key4"]= int(input())
    f=open("test","r")
except Exception as e:
    print(e)


# In[26]:


# multiple exception
try:
    d={"key1":"Deep","key2":[1,2,3,4,5],"key3":(4,5,6,7,8,9)}
    d["key4"]= int(input())
    f=open("test","r")
except Exception as e:
    print(e)
except FileNotFoundError as e:
    print(e)


# In[27]:


try:
    d={"key1":"Deep","key2":[1,2,3,4,5],"key3":(4,5,6,7,8,9)}
    d["key4"]= int(input())
    f=open("test","r")
except Exception as e:
    print(e)
except FileNotFoundError as e:
    print(e)
except ValueError as ee:
    print("here value error has happen",ee)


# In[29]:


## try --except --else

try:
    f=open("test1.txt","w")
    f.write("this is my code for try and catch")
except Exception as e:
    print("this will handle an error")
else:
    print("this will execute once my try block will be execute")
    f.close


# In[31]:


try:
    f=open("test1.txt","r")
    f.write("this is my code for try and catch")
except Exception as e:
    print("this will handle an error",e)
else:
    print("this will execute once my try block will be execute")
    f.close


# In[32]:


## try--except---else/finaly

try:
    f=open("test2","r")
except Exception as e:
    print("sdnfnhnfm",e)
finally:
    print("this will always execute")


# In[33]:


try:
    f=open("test2","r")
except Exception as e:
    print("sdnfnhnfm",e)
else:
    print("do this on sucessesfull exicution")
finally:
    print("this will always execute")


# In[34]:


try:
    f=open("test2","w")
except Exception as e:
    print("sdnfnhnfm",e)
else:
    print("do this on sucessesfull exicution")
finally:
    print("this will always execute")


# In[35]:


try:
    f=open("test2","w")
except Exception as e:
    print("sdnfnhnfm",e)
else:
    print("do this on sucessesfull exicution")
finally:
    print("this will always execute")
    f=open("dasnjdn","r")
#here we got error


# In[36]:


try:
    f=open("test2","w")
except Exception as e:
    print("sdnfnhnfm",e)
else:
    print("do this on sucessesfull exicution")
finally:
    print("this will always execute")
    try:
        f=open("dasnjdn","r")
    except:
        print("handle it")
    finally:
        print("it will execute this block")


# In[39]:


def askint():
    a=int(input())
    return a


# In[40]:


askint()


# In[43]:


def askint():
    try:
        a=int(input())
        return a
    except Exception as e:
        print("there will not int" ,e)


# In[44]:


askint()


# In[45]:


askint()


# In[ ]:


def intergers():
    try:
        a=int(input())
        return a
    except


# In[59]:


#written an code where we need to written integers only other that can ask other int

def ints():
    while True:
        try:
            a=int(input("please enter your int value"))
            if type(a) ==int:
                break
                return a
                
            
        except Exception as e:
            print(e)
    


# In[60]:


ints()


# In[61]:


ints()


# # raise :reseverd keyword for exception

# ### by raise the we can return your own custum error or message here

# In[62]:


def test(a):
    if a < 0:
        raise Exception(a)
    return a


# In[63]:


test(4)


# In[64]:


test(-2)


# In[66]:


g =open("hjdbdhf","r")
    


# In[67]:


def test(a):
    if a < 0:
        raise Exception("you have entered a negative value",a)
    return a


# In[68]:


test(-2)


# In[69]:


def test(a):
    if a < 0:
        raise Zerodivisionerror ("you have entered a negative value",a)
    return a


# In[70]:


test(-5)


# In[72]:


try:
    test("djnh")
except Exception as e:
    print("Calling my raise exception",e)


# # logging

# In[73]:


print("dhfhdj")
# print will not use at the real life standred procedure is logging


# ### logging will give us flexiblity  to understand what problem happing into the code it show us the messages regarding problem error,debug,and we can say that track our code,step by step that all time logging comes into picture

# In[2]:


import logging


# In[2]:


logging.basicConfig(filename ="test.log")


# In[3]:


pwd()

logs:-
DEBUG
INFO
WARNING
ERROR
CRITICAL
# In[9]:


logging.info("this is my info")
logging.warning("this is my warning log")
logging.error("this is error")


# In[13]:


#this wil shutdown the log file
logging.shutdown()


# In[7]:


logging.basicConfig(filename ="test.log",level=logging.INFO)
#this will not added because of jupyter notebook


# In[1]:


import logging
logging.basicConfig(filename="test2.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s ")


# In[2]:


logging.info("this is my info")
logging.warning("this is my warning log")
logging.debug("this is debug")


# In[ ]:


## in using log that time we need to do restart after many times


# In[1]:


import logging
logging.basicConfig(filename="test2.log",level=logging.ERROR,format="%(asctime)s %(levelname)s %(message)s ")


# In[2]:


logging.info("this is my info")
logging.warning("this is my warning log")
logging.debug("this is debug")
logging.error("this is my error log")


# In[3]:


import logging
logging.basicConfig(filename="test2.log",level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s ")


# In[5]:


logging.info("this is my info")
logging.warning("this is my warning log")
logging.debug("this is debug")
logging.error("this is my error log")


# In[1]:


import logging
logging.basicConfig(filename="test2.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s ")


# In[2]:


logging.info("this is my info")
logging.warning("this is my warning log")
logging.debug("this is debug")
logging.error("this is my error log")


# In[4]:


#actual use
import logging

logging.basicConfig(filename="test3.log",level=logging.DEBUG,format ="")


# In[9]:


def divbyzero(a,b):
    logging.info("this is start of my code and i am try to enter %s and %s" , a,b)
    try:
        div =a/b
        logging.info("exicuted sucessesfully")
        logging.add("we add this")
    except Exception as e:
        logging.error("error has happen")
        logging.exception("Exception occured "+str(e))
        


# In[10]:


divbyzero(4,5)


# In[7]:


divbyzero(4,0)


# In[8]:


4/0


# In[11]:


logging.shutdown()


# In[12]:


## module


# In[ ]:




