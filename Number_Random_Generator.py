#Thia code generate n random numbers using a txt file as sourse of
# randomness 

import os
filename = "C:\\documents\\personal info\\Files for gitbub\\war-and-peace.txt"
file = open(filename,"r") 
data = file.read()
filelength = len(data) # get the number of character of the txt file
# print(filelength)
file.close()
B = 0



def readdata(cursor):
        """ This function will retieve the a charcater after reading a checking if different from bank or space."""
        with open(filename, "r") as file:
            file.seek(cursor, os.SEEK_SET)
            data = file.read(1)
            while data == '\n' or data == ' ':
                cursor +=1
                file.seek(cursor, os.SEEK_SET)
                data = file.read(1)
            data = data.lower()
        return data, cursor

def compare(character1,character2):
    """ This function retrieves 1 if character1 > character2, or 0 if opposite.""" 
    global B
        
    if character1 > character2:
        greater = 1
    if character1 < character2:
        greater = 0
    if character1 == character2:
        if B == 0:
            greater = B%2
            B = B+1
        else:
            greater = B%2
            B = B + 1
    
    return greater


def evallocation(previous,new, step):
    """ This function check in the postion or index of the read charcter is bigger than the length of the file.
    
    If so, it will make the algorithm start again.
    """
    
    
    if new > filelength:
        lefover = filelength - previous
        new = step - lefover
    return new


class WarAndPeacePseudoRandomNumberGenerator:
    
    def __init__(self, seed = 3500,initial = 0,bits = 32,pairs =[], step = 100, lastlocation = 0, totalprob = 0):
        """ Contructor __init__, will allow me to create some variables and set up defaul values."""
        self.bits = bits
        self.step = step
        self.pairs = pairs
        self.total_prob = totalprob
        self.location1 = seed
        self.location2 = lastlocation
        self.initial = initial
       
        

    def __repr__(self):
        return f"prng('{self.total_prob}')"



    def random(self):
            """I created my own method of my class that will allow me to get the random numbers."""
            
            for i in range (self.bits): # This loop generate 32 bits 
                if i == 0 and self.initial == 0:
                    location1 = self.location2 + self.location1 + self.step
                    #print(location1)
                    char1      = readdata(location1) # Get the charcater1 by calling the readdata function
                    character1 = char1[0]
                    location1 = char1[1]
                    #print(character1)
                    self.location2 = self.location2 + location1 + self.step  
                    #print(self.location2)
                    location2 = self.location2
                    char2 = readdata(self.location2)#  Get the charcater2 by calling the readdata function
                    #print(character2)
                    character2 = char2[0]
                    self.location2 = char2[1]
                    c = compare(character1,character2) # compare two charcaters by calling compare function
                    #print(c)
                    factor = 1/(2**(i+1))
                    self.pairs.append((character1,character2,c,factor,c*factor))
                    #print(self.pairs)
                else:
                    location1 = self.location2 + self.step
                    location1 = evallocation(self.location2,location1,self.step)
                    char1 = readdata(location1)
                    character1 = char1[0]
                    location1 = char1[1]
                    #print(character1)
                    self.location2 = location1 + self.step
                    location2 = evallocation(location1,self.location2, self.step)
                    char2 = readdata(self.location2)
                    character2 = char2[0]
                    self.location2 = char2[1]
                    c = compare(character1,character2)                                 
                    factor = 1/(2**(i+1))
                    self.pairs.append((character1,character2,c,factor,c*factor))
                    #print(self.pairs)
            #print(self.pairs)
            self.total_prob = 0
            for x in range (self.bits):   # this for loop will create a number betwwen 0 and 1 by adding the probability value of the 32 bits         
                self.total_prob = self.pairs[x][4] + self.total_prob
                self.total_prob = round(self.total_prob,6) # round to six decimals
            self.initial += 1
            self.pairs = []
            return self.total_prob

def Generator(n):
    """ Top level function that retrieves n random numbers."""
    numbers = [] # create the empty list that will receive my random numbers
    prng = WarAndPeacePseudoRandomNumberGenerator()
    for i in range(n):
        r = prng.random()
        numbers.append(r)
    a = min(numbers)
    b = max(numbers)
    #sum_numbers = 0
    #for i in range(n):
    #    sum_numbers = numbers[i] + sum_numbers
    sum_number = sum(numbers)
    average = sum_number/n
    print(numbers)
    print('Min = '+ str(a))
    print('Max = ' + str(b))
    print('Average = '+ str(average))

    return 

Generator(1000)
# prng = WarAndPeacePseudoRandomNumberGenerator(1000)
# r = prng.random()
# prng = WarAndPeacePseudoRandomNumberGenerator(1234)
# r = prng.random()
# r











