#!/usr/bin/env python
# coding: utf-8

# # 1 WRITE A LAMBDA EXPRESSION TO EXTRACT FIRST WORD OF A STRING.

# In[6]:


string=input("Ente a string:")
first_word=lambda string:string.split()[0]
first_word(string)


# # 2.WRITE A FUNCTION TO EXTRACT FIRST WORD OF S STRING(with many words seperated by space).

# In[2]:


def firstword(s):
    first_word=s.split()
    return first_word[0]
string=input("Enter a string : ")
print(firstword(string))


# # 3.EXTRACT THE FIRST WORD FROM EVERY STRING FROM A LIST OF STRINGS BY USING MAP FUNCTION.

# In[3]:


list1=["Regex Software Services","Summer Internship","ML and Deep Learning"]
words=lambda n:n.split()[0]
print(list(map(words,list1)))


# # 4.WRITE A FUNCTION TO RETURN A LIST OF PRIME FACTORS OF A GIVEN NUMBER.

# In[4]:


def isprime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
            break
    else:
        return True
def primefactors(n):
    l=[]
    for i in range(2,n+1):
        if(n%i==0):
            if(isprime(i)):
                l.append(i)
    print(l)
n=int(input('Enter a number:'))
primefactors(n)


# # 5.WRITE A FUNCTION THAT FINDS 2nd LARGEST AMONG 4 NUMBERS(Repetitions are allowed,without sorting).

# In[5]:


def second(l):
    l1=set(l)
    l1.remove(max(l1))
    print(max(l1))
l = [int(i) for i in input("Enter any four numbers : ").split()]
second(l)


# In[ ]:




