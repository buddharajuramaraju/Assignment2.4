
# coding: utf-8

# ### Problem Statement 1:
# Write a Python Program(with class concepts) to find the area of the triangle using the
# below formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the
# parent class and function to calculate the area should be defined in subclass.
# 
# 
# 
# 

# In[4]:


class TriangleInput():
    def __init__(self):
        pass
    def getTriangleSides(self):
        while True:
            self._a = int(input("Please enter length of triangle side-1 "))
            self._b = int(input("Please enter length of triangle side-2 "))
            self._c = int(input("Please enter length of triangle side-3 "))
            if self._a+self._b > self._c and self._b+self._c > self._a and self._c+self._a > self._b: # triangle validation
                break
            else:
                print("we cant form trianlge with given values")


# In[5]:


class TrianlgeArea(TriangleInput):
    def getArea(self):
        s = (self._a+self._b+self._c)/2
        area = (s*(s-self._a)*(s-self._b)*(s-self._c))**.5
        return area


# In[8]:


tarea = TrianlgeArea()
tarea.getTriangleSides()
print("Area of given trianlge is {AREA}".format(AREA = tarea.getArea()))


# ### Problem Statement 2:
# Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.

# In[9]:


def filter_long_words(wordlist,minlength):
    return [word for word in wordlist if len(word) > minlength ]


# In[10]:


filter_long_words(["Ramaraju","Buddharaju","venkata"],8)


# In[11]:


filter_long_words(["Ramaraju","Buddharaju","venkata"],5)

