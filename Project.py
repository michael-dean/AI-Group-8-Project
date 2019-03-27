# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:45:45 2019

@author: marcc
"""

#this will be used as the object inside the matix to hold all of the data in each position
class contents:
    def __init__(self):
        
        #list of weights for the drop off model
        #initalizing as 0 to represent has not visited
        self.dropoffweights = [0,0,0,0] #order is north, south, east, west
        
        #list of weights for the pickup model
        #initalizing as "-" to represent has not visited
        self.pickupweighrs = [0,0,0,0] #order is north, south, east, west
        
        #identifyers if the block is special
        self.dropoff = False
        self.pickup = False
        
    def __str__(self):
        if(self.isdropoff()):
            return "2"
        elif(self.ispickup()):
            return "1"
        else:
            return "0"
        
    #toggle dropoff
    def tdropoff(self):
        if(self.dropoff == True):
            self.dropoff = False
        else:
            self.dropoff = True
    
    #toggle pickup
    def tpickup(self):
        if(self.pickup == True):
            self.pickup = False
        else:
            self.pickup = True
        
    #returns if it is drop off
    def isdropoff(self):
        return self.dropoff
        
    #returns if it is pickup
    def ispickup(self):
        return self.pickup
        
    #using d as dropoff and p as pickup for function names
    #using N as North, S as South, E as East, W as West for function names
    
    #dropoffweight functions
    def dsetN(self,value): #give a new value to set north to
        self.dropoffweights[0] = value
    
    def dsetS(self, value): #give a new value to set south to
        self.dropoffweights[1] = value
        
    def dsetE(self,value): #give a new value to set east to
        self.dropoffweights[2] = value
    
    def dsetW(self, value): #give a new value to set west to
        self.dropoffweights[3] = value
        
    #used to increment and decrement weights a certain ammount
    
    #incrementing functions
    def dincN(self,value): #give a new value to increment north to
        self.dropoffweights[0] += value
    
    def dincS(self, value): #give a new value to increment south to
        self.dropoffweights[1] += value
        
    def dincE(self,value): #give a new value to increment east to
        self.dropoffweights[2] += value
    
    def dincW(self, value): #give a new value to increment west to
        self.dropoffweights[3] += value
        
    #decrementing functions
    def ddecN(self,value): #give a new value to increment north to
        self.dropoffweights[0] -= value
    
    def ddecS(self, value): #give a new value to increment south to
        self.dropoffweights[1] -= value
        
    def ddecE(self,value): #give a new value to increment east to
        self.dropoffweights[2] -= value
    
    def ddecW(self, value): #give a new value to increment west to
        self.dropoffweights[3] -= value
    
    
    
    #pickup weight functions
    def psetN(self,value): #give a new value to set north to
        self.pickupweights[0] = value
    
    def psetS(self, value): #give a new value to set south to
        self.pickupweights[1] = value
        
    def psetE(self,value): #give a new value to set east to
        self.pickupweights[2] = value
    
    def psetW(self, value): #give a new value to set west to
        self.pickupweights[3] = value
        
    #used to increment and decrement weights a certain ammount
    
    #incrementing functions
    def pincN(self,value): #give a new value to increment north to
        self.pickupweights[0] += value
    
    def pincS(self, value): #give a new value to increment south to
        self.pickupweights[1] += value
        
    def pincE(self,value): #give a new value to increment east to
        self.pickupweights[2] += value
    
    def pincW(self, value): #give a new value to increment west to
        self.pickupweights[3] += value
        
    #decrementing functions
    def pdecN(self,value): #give a new value to increment north to
        self.pickupweights[0] -= value
    
    def pdecS(self, value): #give a new value to increment south to
        self.pickupweights[1] -= value
        
    def pdecE(self,value): #give a new value to increment east to
        self.pickupweights[2] -= value
    
    def pdecW(self, value): #give a new value to increment west to
        self.pickupweights[3] -= value
    
        

#used to check if cordinate is out of bounds aka a wall
def isvalidcord(mat,x,y):#pass in the matrix to ensure correctness
    #if col cord is within range
    if (x >=0 and x < len(mat[0])):
        #if row cord is within range
        if(y >= 0 and y< len(mat)):
            return True
    return False;




#used to "move" and determine the weights in the matix
class avatar:
    def __init__(self):
        #cordinates
        self.x=4
        self.y=0
        #carrying block
        self.carrying = False
        
    def __str__(self):
        return ("("+str(self.x)+","+str(self.y)+") carrying = "+ str(self.iscarrying()))
    
    #returns x cordinate
    def getX(self):
        return self.x

    #returns y cordinate
    def getY(self):
        return self.y
        
    #"moves" avatar north ###NEEDS SOME FORM OF CHECK TO SEE IF IT IS A VALID POSITION!!!! as in isvalidcord(matrix,x,y)
    def moveN(self):
        self.y += 1
    
    ##"moves" avatar south ###NEEDS SOME FORM OF CHECK TO SEE IF IT IS A VALID POSITION!!!!
    def moveS(self):
        self.y -= 1
        
    #"moves" avatar east ###NEEDS SOME FORM OF CHECK TO SEE IF IT IS A VALID POSITION!!!!
    def moveE(self):
        self.x +=1
        
    #"moves" avatar west ###NEEDS SOME FORM OF CHECK TO SEE IF IT IS A VALID POSITION!!!!
    def moveW(self):
        self.x -=1
    
    #use when starts carrying block
    def startcarrying(self):
        self.carrying = True
    
    #use when drops block off
    def stopcarrying(self):
        self.carrying = False
        
    #use to check if it is currently carrying anything
    def iscarrying(self):
        return self.carrying


###############################################################################
#matrix code

class matrix:
     
    def __init__(self):
        self.matrix = []
        
    #used to fill in a matrix with a default value for a certain number of rows and columns
    def initialize(self,data, nrows, ncols): #data is default values in matrix , nrows is number of rows, ncols is number of columns
        for i in range(nrows):
            #reset row to put in each col value
            row = []
            for i in range(ncols):
                #append default data for amount of columns
                #using use case due to shadowcopy
                row.append(contents())
                
            #put the row into the matrix
            (self.matrix).append(row)

    def getdataat(self,x,y):
        #print("data at (" +str(x)+ ","+str(y)+") is:"+str((self.matrix[y])[x]))
        return (self.matrix[y])[x]
    
    #used to create a string form of the matrix
    #data inside must be able to convert to string
    def sprint(self):
        temp = ""
        
        for i in range(len(self.matrix)):
            for j in self.matrix[i]:
                temp += str(j)+ " "
                
            temp+="\n"
            
        return temp
    
    #how the matrix will be represented when used as a string
    def __str__(self):
        return self.sprint()

    def __repr__(self):
        return self.matrix



#Test matrix (TO LEARN)
testmatrix = matrix()
testmatrix.initialize(contents(),5,5)

print("Inital Matrix:")
print(testmatrix)

(testmatrix.getdataat(0,4)).tdropoff()
(testmatrix.getdataat(2,4)).tdropoff()
(testmatrix.getdataat(4,1)).tdropoff()

(testmatrix.getdataat(0,0)).tpickup()
(testmatrix.getdataat(2,2)).tpickup()
(testmatrix.getdataat(4,4)).tpickup()

print("Matrix with one pickup(1) and dropoff(2)")
print(testmatrix)

#avatar creation
ava = avatar()
print(ava)

#test for avatar movement
print(ava)


