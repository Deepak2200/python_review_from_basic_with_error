#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[3]:


## download text editor:- spider,notepad++,etc


# In[4]:


## modeules :- modules is a collection of code,piece of code or set of a code which we written into these files


# In[ ]:


#os.<tab> look all the fuction
os.


# In[7]:


###### jab hum koi code likhate or hame vo code baar baar use karana hai har jagah hum same code baar baar thode hi likhenge  ush time modular codding aata hai dimak me. ki ek file bana lo usame code likh ke rakha jay or "os" function dubara use kiya ja sake kis bhi jagah 
'jab hum koi code likhate or hame vo code baar baar use karana hai har jagah hum same code baar baar thode hi likhenge  ush time modular codding aata hai dimak me. ki ek file bana lo usame code likh ke rakha jay or "os" function dwara dubara use kiya ja sake kis bhi jagah '


# In[8]:


def test(a,b):
    return a+b


# In[9]:


test(10,20)


# In[12]:


pwd() # preent workig directory


# In[11]:


ls ## list of all the directory


# In[13]:


get_ipython().system('dir #')


# In[15]:


dir()  # it's show builtin method


# In[16]:


f=open("test2.py","w")


# In[18]:


f.close()


# ### modular coding hum ek .py file me likh ke save sar sakte hai baar baar use karane ke liye isase hame baar baar same code nahi likhana padega

# In[19]:


import test2


# In[20]:


test2.test(10,20)


# In[23]:


test2.test1({"a":10,"b":10})# SOME MISTAKE IN Code


# In[26]:


from test2 import test


# In[28]:


test2.test(10,20)


# In[31]:


# for importing all the modul from file than use

from test2 import *


# In[32]:


test2.test(10,20)


# In[33]:


test2.test1(10,2)

# here we can not update it


# In[36]:


test2.test2(5)

# it is not able to update it


# In[39]:


open("test1.py","w")


# In[40]:


import test1


# In[41]:


test1.test(10,12)


# In[42]:


test1.test1(10,12)


# In[44]:


test1.test2(5)


# In[49]:


import test2


# In[50]:


test2.test2()


# In[51]:


## tkinter python interface for  ui


# # OOP  :-Object Oriented Programing

# In[52]:


# when we work with the project that time we face many lines of code into the project we need to deal with them it is not easy task that time oobs comes into the picture


# In[ ]:


# 1.oops is going to give you the capicity of structure model for your different different type of task and subtask you are going to create
# 2.In this .ipynb file when we want to write code that is called scriping
# 3.without oops we also do all work by normal coding but it is not i structured way
# 4.python is language it's support scripting as well as oops exp:-scaala and java only support oops
# 5.without any strured thoes we are written that called scripting .
# car--which car -we can not predict that but some sense is there
# bird-- ""
# sports-- ""
# man :- ""


# ## class:- class is the kind of blue print
# 
# ## object:- object is the entity really exist  which we able to see ,touch etc 
# 
# when we say that :- touch the cup .which cup? ---class
# when we say that :- touch the milton cup ----object
# 
# where we know the specific thing that is called object where we not known about the specfic thing only know about thinghs (structure of that ,sense of that but not known exectly ) that is called class (blueprint of that)

# In[53]:


class car:
    pass


# In[ ]:


# when a function written by the __fuction__(double under score first and befor that) that called invild function
# __init__ :-invild function it is called as "constructer"



# In[ ]:


# constructer(__init__):- constructer is the kind of entity/method/fuction which is going to help us to pass a deta into the perticular class
# self :-self is know as the pointer (it may be any name not self only) or first variable of any class is called the pointer


# In[54]:


## GENERIC WAY
class car:
    def __init__(self,brand_name,fuel_type,body_type):
        
        self.brand_name=brand_name
        self.fuel_type = fuel_type
        self.body_type=body_type
        
        
    def descrp_car():
        print(self.brand_name,self.fuel_type,self.body_type)
    


# In[55]:


innova =car()


# In[56]:


innova =car("toyota","petrol","suv")


# In[59]:


innova.descrp_car()

## error is because of self is knot present it means pointer is not present


# In[61]:


innova.body_type


# In[62]:


innova.brand_name


# In[63]:


innova.fuel_type


# ####  for error look at here (self was missingb there)

# In[16]:


class car:
    def __init__(self,brand_name,fuel_type,body_type):
        
        self.brand_name1=brand_name
        self.fuel_type = fuel_type
        self.body_type=body_type
        
        
    def descrp_car(self):
        print(self.brand_name1,self.fuel_type,self.body_type)


# In[17]:


innova =car("BMW","Petrol","SUV")


# In[18]:


innova.descrp_car()


# In[21]:


innova.brand_name1


# In[ ]:





# In[19]:


nexon =car("TATA","Petrol","SUV")


# In[20]:


nexon.descrp_car()


# In[11]:


class car_brand:
    def __init__(self,brand_name,engin,fuel_type):
        
        self.brand_name=brand_name
        self.engin=engin
        self.fuel_type=fuel_type
        
    def car_des(self):
        return self.brand_name,self.engin,self.fuel_type


# In[12]:


innova=car_brand("toyota","bs6","petrol")


# In[14]:


innova.car_des()


# In[22]:


class car:
    def __init__(self,brand_name,fuel_type,body_type):
        
        self.a=brand_name
        self.b = fuel_type
        self.c=body_type
        
        
    def descrp_car(self):
        print("this is my first car")


# In[23]:


innova=car("innova","p","ggfc")


# In[24]:


innova.a


# In[25]:


innova.b


# In[27]:


innova.descrp_car()


# ### this is work without init methos also
# 
# only we also make as class  under that we create many fuction use it
# 
# 
# __init__ is only require when we want to create object it self otherwies its not required
# 
# but here is convention to create pointer to any kind of that are you are going to create so that it will going to bind the any object which is create with in the class and class

# In[28]:


class car:
    def descrp_car(self):
        print("this is my first car")


# In[29]:


innova=car()


# In[30]:


innova.descrp_car()


# In[35]:


class list_parser:
    
    def parser(self,a):
        if type(a)==list:
            for i in a:
                print(i)
                
    def reverse_list(self,z):
        if type(z)==list:
            return z[::-1]


# In[36]:


c=list_parser()


# In[34]:


c.parser([1,2,3,4,5,(3,4,5),"sudh"])


# In[37]:


c.reverse_list([1,2,3,4,8,5])


# In[51]:


class list_parser:
    def __init__(self,l):
        self.l=l
    
    def parser(self):
        if type(self.l)==list:
            for i in self.l:
                print(i)
                
    def reverse_list(self):
        if type(self.l)==list:
            return self.l[::-1]


# In[52]:


c=list_parser([1,2,3,4,5,6])


# In[53]:


c.l


# In[54]:


c.reverse_list()


# In[11]:


# Assignment

class dic_parser:
    
    def __init__(self,d):
        self.d=d
        
    def dic_keys(self):
        if type(self.d)==dict:
            return self.d.keys()
        
    def dic_values(self):
        if type(self.d)==dict:
            return self.d.values()
        
    def dec_value(self,b):
        try:
            if type(b)==dict:
                return b
        except Exception as e:
            print("error occure",e)
            
    def dec_create(self,a):
        
        if type(a)==dict:
            return a.keys(),a.values()
        
  
        


# In[12]:


d={"a":10,"b":12}


# In[13]:


dictionary=dic_parser(d)


# In[14]:


dictionary.dec_create({"a":35,"b":45})


# In[15]:


dictionary.dic_keys()


# In[16]:


dictionary.dic_value()


# In[17]:


dictionary.dec_value({"a":20,"b":10})


# In[21]:


l=[1,3,5,6]


# In[22]:


dictionary.dec_value(l)


# # Inheritance

# In[1]:


class xyz:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def test(self):
        print("this is my first test method of xyz class")
        
    def test1(self):
        print("this is the test1 method")
        
    def test2(self):
        print("this is the method of xyz class")
        


# In[2]:


p=xyz(1,2,3)


# In[3]:


p.a


# In[4]:


p.test2()


# In[5]:


# previous class to this class like a method its called inheritence
# they inheritate the previous class

class xyz1(xyz):
    pass


# In[6]:


q=xyz1()
# this is occured only by the inheritance property


# In[7]:


q=xyz1(3,3,4)


# In[8]:


q.a


# In[9]:


q.test()


# In[10]:


class xyz1(xyz):
    def test(self):
        print("this is the test method availbale in xyz1")
        


# In[11]:


g=xyz1(1,2,3)


# In[12]:


g.test()

# this overlap on the privious method


# In[14]:


## multiclass inheritance
class xyz():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def test(self):
        print("this is a math of xyz class")
        
        
class xyz1:
    
    def __init__(self,p,q,w):
        self.p=p
        self.q=q
        self.w=w
        
    def test1(self):
        print("this is a math of xyz1 class")
        
        
class child(xyz,xyz1):
    pass


# In[15]:


n=child()


# In[17]:


class child2(xyz1,xyz):
    pass

n1=child2() # VARIBL THEY HAVE P,Q,W

## bydefault they will take 1st varibale from 1st class
## BUT IT ABLE TO TAKE BOTH CLASSES FUNCTION


# In[16]:


n=child(1,2,3)# VARIBL THEY HAVE A,B,C


# In[ ]:


n.


# In[18]:


# WE WANT BOTH THE VARIBLE INTO THE SAME FUNCTION

class xyz():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def test(self):
        print("this is a math of xyz class")
        
        
class xyz1:
    
    def __init__(self,p,q,w):
        self.p=p
        self.q=q
        self.w=w
        
    def test1(self):
        print("this is a math of xyz1 class")
        
        
class child(xyz,xyz1):
     def __init__(self,*args):
            xyz.__init__(self,*args)
            xyz1.__init__(self,*args)
    


# In[19]:


n=child(4,5,6)


# In[20]:


n.a


# In[21]:


n.p


# In[23]:


n.test()


# In[24]:


n.test1()


# In[25]:


# WE WANT BOTH THE VARIBLE INTO THE SAME FUNCTION

class xyz():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def test(self):
        print("this is a math of xyz class")
        
        
class xyz1:
    
    def __init__(self,p,q,w):
        self.p=p
        self.q=q
        self.w=w
        
    def test1(self):
        print("this is a math of xyz1 class")
        
        
class child(xyz,xyz1):
     def __init__(self,*args,**kwargs):
            xyz.__init__(self,*args)
            xyz1.__init__(self,**kwargs)
    
    


# In[26]:


k=child(22,3,4)


# In[27]:


k=child(22,3,4,p=4,q=6,w=10)


# In[28]:


k.p


# In[31]:


## multi-level inheritance

class parent:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def check(parent):
        print("this is parent class")
        
class child1(parent):
    def check1(self):
        print("this is first child class")
        
class child2(child1):
    def check2(self):
        print("this is second child class")
        
    


# In[33]:


x=child2(1,3,2)


# In[35]:


x.check()


# In[37]:


# we also create 100 of class by maltilavel
class parent:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def check(parent):
        print("this is parent class")
        
class child1(parent):
    def check1(self):
        print("this is first child1 class")
        
class child2(child1):
    def check2(self):
        print("this is second child2 class")
        
        
class child3(child1):
    def check3(self):
        print("this is second child2 class")


# In[38]:


z=child3()
# same error we get


# ##  Incapsalation
# 
# #### private class
# #### public class

# In[44]:


class test:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

class test1(test):
    pass

u=test(1,2,2)
v=test1(4,56,8)


# In[43]:


u.a


# In[41]:


u.b


# In[45]:


v.a


# In[46]:


class test:
    def __init__(self):
        self.a=4
        

class test1(test):
    self.a=7
    pass


# In[47]:


class test:
    def __init__(self):
        self.a=4
        

class test1(test):
    def __init__(self):
        self.a=7


# In[48]:


d=test1()


# In[49]:


d.a


# In[50]:


s=test()


# In[51]:


s.a


# In[56]:


class test:
    def __init__(self):
        self.a=4
        

class test1(test):
    def __init__(self):
        test.__init__(self)
        self.a=7
        
u=test()
v=test1()


# In[55]:


u.a


# In[57]:


v.a


# In[62]:


class test:
    def __init__(self):
        self._a=4  
        

class test1(test):
    def __init__(self):
        test.__init__(self)
        self.__a=7 
        
u=test()
v=test1()


# In[61]:


u._a


# In[63]:


v.__a


# In[ ]:


# _a :-protected its means we use it inside the classes as well as subclasses but out of the sub class we not able to use that .

# __b:-it is  not allow to acess because it is private into the python


# In[74]:


class test:
    def __init__(self,a,b,c):
        self._a=a  ## protected
        self.__b=b   ## private
        self.c=c  ## public
        
V=test(4,5,6)


# In[75]:


V.a


# In[76]:


V._a


# In[78]:


V._test__b # for private call(._classname__)


# In[80]:


class test:
    def __init__(self,a,b,c):
        self._a=a  ## protected
        self.__b=b   ## private
        self.c=c  ## public
        
class test1(test):
    pass
        
V=test(4,5,6)
U=test1(1,2,3)


# In[81]:


V.c


# In[82]:


V._a


# In[83]:


V._test__b


# In[84]:


U.c


# In[85]:


U._a


# In[86]:


U._test1__b # here we not able use it because it is not use in subclasses


# In[87]:


U._test__b # but it is exicute


# In[91]:


class bonouscalculater:
    def __init__(self,empid,empidrating):
        self.empid=empid
        self.empidrating=empidrating
        self.__bonusforratingA="70%"
        self.__bonusforratingB="60%"
        self.__bonusforratingC="40%"
        
    def bonouscalculater(self):
        if self.empidrating== "A":
            bonous=self.__bonusforratingA
            return bonous
        elif self.empidrating == "B":
            bonous=self.__bonusforratingB
            return bonous
        else:
            bonous=self.__bonusforratingC
            return bonous


# In[92]:


emp1=bonouscalculater(101,"A")

emp2=bonouscalculater(102,"B")

emp3=bonouscalculater(103,"C")


# In[93]:


emp1.bonouscalculater()


# In[94]:


emp2.bonouscalculater()


# In[95]:


emp3.bonouscalculater()


# In[103]:


emp1.__bonusforratingB="90%"


# In[104]:


emp1.bonouscalculater()


# In[106]:


emp2.empidrating


# In[101]:


# modify way

class bonouscalculater:
    def __init__(self,empid,empidrating):
        self.empid=empid
        self.empidrating=empidrating
        self.__bonusforratingA="70%"
        self.__bonusforratingB="60%"
        self.__bonusforratingC="40%"
        
    def bonouscalculater(self):
        if self.empidrating== "A":
            bonous=self.__bonusforratingA
            return bonous
        elif self.empidrating == "B":
            bonous=self.__bonusforratingB
            return bonous
        else:
            bonous=self.__bonusforratingC
            return bonous
        
empid=int(input("Enter emlpoy id"))
empidrating=input("enter category of employ").capitalize()

emp_info=bonouscalculater(empid,empidrating)


# In[102]:


emp_info.bonouscalculater()


# In[109]:


"""python says that ,everyone the user of the each and every variable
must be mature inhalf to choose tha variable way must  be defined"""


# In[110]:


## it is able to change the variable the private also but that time we need to do variable with the name of classes


# In[ ]:


## in protected case we also be able to change the variable


# In[111]:


class bonouscalculater:
    def __init__(self,empid,empidrating):
        self.empid=empid
        self.empidrating=empidrating
        self.email="dkjnkjfdnjnfr@gmail.com"
        self.__bonusforratingA="70%"
        self.__bonusforratingB="60%"
        self.__bonusforratingC="40%"
        
    def bonouscalculater(self):
        if self.empidrating== "A":
            bonous=self.__bonusforratingA
            return bonous
        elif self.empidrating == "B":
            bonous=self.__bonusforratingB
            return bonous
        else:
            bonous=self.__bonusforratingC
            return bonous


# In[112]:


emp1=bonouscalculater(101,"A")

emp2=bonouscalculater(102,"B")

emp3=bonouscalculater(103,"C")


# In[113]:


emp1.email


# In[114]:


emp1.email="deepak@gmail.com"


# In[115]:


emp1.email


# # Polymorphism

# ####  Ploymoephism(multiple-form):-one single entity but its behevior going to change according to situation/sercumtancess.

# like:- a relation a persion have many relation according to the people like they one man have any one,s father,brother,uncle  etc

# In[1]:


def test(a,b):
    return a+b


# In[2]:


test(4,4)


# In[3]:


test("deep","ak")


# In[4]:


class insta:
    def share_story(self):
        print("this will share my insta story")
        
class facebook:
    def share_story(self):
        print("this will share my facebook story")


# In[7]:


def sharestory(app):
    app.share_story()


# In[8]:


i=insta()
j=facebook()


# In[10]:


sharestory(j)


# In[11]:


sharestory(i)


# In[13]:


class social_media:
    def share_story(self):
        print("share a stories")
    def upload_pic(self):
        print("this will help you to upload pic on social media")
        
        
class facebook(social_media):
    def share_story(self):
        print("thhis is a fin for sharing story")
        
class insta(social_media):
    def share_story(self):
        print("this will share my insta story")


# In[14]:


f=facebook()
i=insta()


# In[15]:


f.share_story()


# In[16]:


i.share_story()


# In[17]:


class test(Exception):
    def __init__(self,msg):
        self.msg=msg
        


# In[18]:


try:
    raise(test("this is my own exception class"))
except test as t:
    print(t)
    


# In[19]:


try:
    5/0
except test as t:
    print(t)
    


# In[20]:


try:
    raise(test("this is my own exception class"))
    5/0
except test as t:
    print(t)
    


# In[24]:


### staticmethods use

class parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
        
        
    @staticmethod
    def child():
        print("thuis is child class with static")


# In[25]:


p=parent(2,4)


# In[26]:


p.child()


# ### if you not want to do the self use many time than use static

# ## Decoretor("@methods"):-Decoretors as knothing but it specialily design function which is going to do help other function or instances to behave as per the defination 

# In[31]:


class parent:
    father="name" # this is called class variable /static variable
    def __init__(self,a,b):
        self.a=a    # this is called instance variable
        self.b=b
        
    @staticmethod
    def child():
        print("thuis is child class with static")
        
    def child1(self):
        print("thuis is child class with static")


# In[28]:


parent.father  #this object we take without variable


# In[30]:


parent.mro()


# In[32]:


parent.child()


# In[33]:


parent.child1() #here we need to create object

# this is not able to excess because it is not static fuction


# In[41]:


class accountdetails:
    account_no= int(input("enter account number"))
    
    def __init__(self,amount):
        self.amount=amount
        
    def show_balance(self,deduction):
        self.amount=self.amount -deduction
        return self.amount,account_no


# In[42]:


accountdetails.account_no


# In[43]:


account=accountdetails(50000)


# In[44]:


account.show_balance(10100)


# # Abstract  class
# 
# ### abstract means its a kind of blueprint/structure  of classes i will define a function but not like defination

# In[3]:


class abc:
    pass


# In[4]:


class data_project :
    
    
    def read_file(self):
        pass
    
    def validate_filename(self):
        pass
    
    def validate_datatype(self):
        pass
    
    
    def validate_db_conn(self):
        pass
    
    def create_connection(self):
        pass
    
    def insert_fuc(self):
        pass
    
    def dalete_fuc(self):
        pass
    
    def update_data(self):
        pass
    
    def perform_stats(self):
        pass
    
    
    


# In[ ]:


class db_opn(data_project)


# In[ ]:


## __init__ is the overload -we try to overload

## __str__ is also be overload .it is invalid function to represnt in the strring form


# In[11]:


class test:
    def fun(self):
        print("this is mu simple class")
        
        
   
        


# In[12]:


t=test()


# In[13]:


print(t)


# In[14]:


class test:
    def fun(self):
        print("this is mu simple class")
        
        
    def __str__(self):  # overloading of the messages
        return str("this is a fun called at a time of onject")


# In[15]:


t=test()


# In[16]:


print(t)


# In[17]:


t


# In[18]:


class test:
    def fun(self):
        print("this is mu simple class")
        
        
    def __str__(self):  # overloading of the messages
        return "this is a fun called at a time of onject"


# In[19]:


t=test()


# In[20]:


print(t)


# In[21]:


class test:
    def fun(self):
        print("this is mu simple class")
        
        
    def __str__(self):  # overloading of the messages
        return 656546464


# In[22]:


t=test()


# In[23]:


print(t)


# In[25]:


class Phones:
    def __init__(self,brand,model,price):
        
        self.brand=brand
        self.model=model
        self.price=price
        
    def specs(self):
        return ("brand",self.brand,"price",self.price)
    
    def typeofphones(self):
        if self.price < 5000:
            return "thus is budget phone"
        else:
            return "this is mid range phone"
        
class smartphones(Phones):
    def __init__(self,brand,model,price,ram,storage):
        super().__init__(brand,model,price)
        self.ram=ram
        self.storage=storage
        
        
class flashphoes(smartphones):
    
    def __init__(self,model,brand,price,ram,storage,display,backcamera,frountcamera):
        super.__init__(brand,price,model,ram,storage)
        self.display=display
        self.backcamera=backcamera
        self.frountcamera=frountcamera


# # super class

# ###  super() is basically use-- when we build classes(child class) that extend the functionality of priviously build class(parent class).
# 
# 
# ### super function in python is use to access method of immediete parent class 

# In[1]:


class company:
    def company_name(self):
        return "ineuron"
    
class employ(company):
    def info(self):
        c_name=super().company_name()
        print("i want to",c_name)


# In[2]:


emp=employ()


# In[3]:


emp.company_name()


# In[4]:


emp.info()


# ### when you initialize a child  in a python you can call "super().__init__() method"
# 
# ## This initialize the parent class object into child class object

# In[6]:


# example:-

class parent:
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2
        
class child(parent):
    def __init__(self,v1,v2,v3):
        super().__init__(v1,v2)
        self.v3=v3


# In[8]:


c1=child(23,45,67)


# In[9]:


c1.v1


# In[ ]:


class classname(parentclass):
    def method(self,arg):
        super([classname],[self]).method(args)


# In[14]:


class parent:
    def __init__(self):
        print("This is the parent class")
        
class parent2:
    def __init__(self):
        print("This is the parent2 class")
        
class parent3:
    def __init__(self):
        print("This is the parent3 class")
        
        
class child(parent,parent2,parent3):
    def __init__(self):
        super().__init__()
        
        
class child2(parent2,parent3,parent):
    def __init__(self):
        super().__init__()

        
class child3(parent3,parent2,parent):
    def __init__(self):
        super().__init__()
        
        
        
class child4(parent,parent2,parent3):
    def __init__(self):
        super(parent2,self).__init__()


# In[11]:


t1=child()


# In[15]:


t4=child4()


# In[16]:


class child4(parent,parent2,parent3):
    def __init__(self):
        super(parent,self).__init__()


# In[17]:


t4=child4()


# In[ ]:




