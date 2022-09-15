# the solver of the 4 = 10 problem
"""four single dgits and available operators are given,
   creating a formula that results 10 is required"""
   
# MAINTENANCE IS NOT CONSIDERED

from operator import truediv
from itertools import permutations, product

brackPos = [(0, 4), (0, 6), (2, 6), (2, 8), (4, 8)]

def Solver(nums, opers, bracket = True) :
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
                        if eval(tmpform) == 10 : print(tmpform)
                    except ZeroDivisionError : continue
            else :
                try :
                    if eval(tmpform) == 10 : print(tmpform)
                except ZeroDivisionError : continue                     


############################################
############# MODIFY HERE ##################
############################################
                                        ####
numbers = [3, 3, 7, 1]                  ####
operators = ['+', '-', '*', '/']        ####
bracket = True                          ####
                                        ####
############################################
############################################
############################################

Solver(numbers, operators, bracket)
