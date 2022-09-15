# the extension solver of the 4 = 10 problem
"""three or more numbers and operators, goal are given,
   this solver finds the formula that results goal"""
   
# MAINTENANCE IS CONSIDERED

from operator import truediv
from itertools import permutations, combinations, product             

############################################
############# MODIFY HERE ##################
############################################
                                        
numbers = [8, 8, 6, 6]                  
operators = ['+', '-', '*', '/']        
goal = 10                               
bracket = True                          
                                       
############################################
############################################
############################################


brackPos = []
#for i in range(len(combinations(range(5), 2)) - 1) :
    


def Solver(nums, opers, goal, bracket = True) :
    numList = list(set(permutations(nums, 4)))
    operitem = [opers, opers, opers]
    operList = list(product(*operitem))
    
    for i in numList :
        for j in operList :
            form = str(i[0]) + j[0] + str(i[1]) + j[1] + str(i[2]) + j[2] + str(i[3])
            if bracket :
                for k in brackPos :
                    tmpform = form[0:k[0]] + "(" + form[k[0]:k[1]-1] + ")" + form[k[1]-1:9]  
                    try :
                        if abs(eval(tmpform) - goal) < 0.01 : print(tmpform)
                    except ZeroDivisionError : continue
            else :
                try :
                    if abs(eval(tmpform) - goal) < 0.01 : print(tmpform)
                except ZeroDivisionError : continue      

Solver(numbers, operators, goal, bracket)
