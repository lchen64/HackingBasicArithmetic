#!/usr/bin/env python
# coding: utf-8

# In[33]:


class hand:
    def __init__(self,fingers):
    	self.fingers = fingers
        
def count(x,y):
	return x.fingers+y

def raise_hand(num, hand):
	hand.fingers = num

def sum(a1,a2):

    LeftHand = hand(0)
    RightHand = hand(0)
    raise_hand(a1, LeftHand)
    raise_hand(a2, RightHand)
    y = count(LeftHand, 0)
    s = count(RightHand,y)

    return s


# In[34]:


print(sum(2,5))


# In[39]:


def raiseCount(num1, hand, num2):
    hand.fingers = num1
    hand.fingers+=num2
    return hand.fingers

def shortcutSum(a1,a2):
    
    LeftHand = hand(0)
    RightHand = hand(0)
    y = raiseCount(a1, LeftHand, 0)
    s = raiseCount(a2, RightHand, a1)
    
    return s


# In[40]:


shortcutSum(2,5)


# In[44]:


def countFromFirst(a1,a2):
    LeftHand = hand(0)
    RightHand = hand(0)
    sum = raiseCount(a2,LeftHand,a1)
    return sum

print(countfromFirst(2,5))


# In[45]:


def min(a1,a2):
    if a1>a2:
        return countFromFirst(a2,a1)
    else:
        return countFromFirst(a1,a2)
print(min(2,5))

