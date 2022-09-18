# the extension solver of the 4 = 10 problem
"""three or more numbers and operators, goal are given,
   this solver finds the formula that results goal"""
   
# MAINTENANCE IS CONSIDERED

from operator import truediv
from itertools import permutations, product             

############################################
############# MODIFY HERE ##################
############################################
                                        
numbers = [3, 4, 7, 8]                  
operators = ['+', '-', '*', '/']        
goal = 10                               
bracket = False                          
                                       
############################################
############################################
############################################


def FindBrackPos(n) :
    tmpPos = []
    for i in range(0, 2 * n - 3, 2) :
        for j in range(2, 2 * n + 1, 2) :
            if j - i > 2 and j - i != 2*n:
                tmpPos.append((i, j))
    return tmpPos


def Solver(nums, opers, goal, bracket=True) :
    n = len(nums)
    brackPos = FindBrackPos(n)
    numList = list(set(permutations(nums, n)))
    operitem = []
    for _ in range(n - 1) :
        operitem.append(opers)
    operitem.append([""])
    operList = list(product(*operitem))
    
    for i in numList :
        for j in operList :
            form = ""
            for k in range(n) : form += str(i[k]) + j[k]
            
            try :
                if abs(eval(form) - goal) < 0.01 : print(form)
            except ZeroDivisionError : continue
            
            if bracket :                
                for k in brackPos :
                    tmpform = form[0:k[0]] + "(" + form[k[0]:k[1]-1] + ")" + form[k[1]-1:2*n+1]  
                    try :
                        if abs(eval(tmpform) - goal) < 0.01 : print(tmpform)
                    except ZeroDivisionError : continue      

Solver(numbers, operators, goal, bracket)
