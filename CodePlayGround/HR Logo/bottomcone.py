thickness = int(5) #This must be an odd number
c = 'H'

#Bottom Cone
for i in range(thickness):
    print (((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
"""
0 - ( 'HHHH'.rjust(5) + H + 'HHHH'.ljust(5) ) . rjust(30)
1 - ( 'HHH'.rjust(5) + H + 'HHH'.ljust(5) ) . rjust(30)
2 - ( 'HH'.rjust(5) + H + 'HH'.ljust(5) ) . rjust(30)
3 - ( 'H'.rjust(5) + H + 'H'.ljust(5) ) . rjust(30)
4 - ( ''.rjust(5) + H + ''.ljust(5) ) . rjust(30)



012345678901234567890123 4 56789
                    HHHH H HHHH 
                     HHH H HHH  
                      HH H HH   
                       H H H    
                         H      

"""