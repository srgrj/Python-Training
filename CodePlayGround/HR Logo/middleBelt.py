
thickness = int(5) #This must be an odd number
c = 'H'
    
#Middle Belt
for i in range((thickness+1)//2):
    print ((c*thickness*5).center(thickness*6))
    
"""
0 - ('H'*5*5).center(5*6)
1 - ('H'*5*5).center(5*6)
2 - ('H'*5*5).center(5*6)

  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
012345678901234567890123456789 
"""