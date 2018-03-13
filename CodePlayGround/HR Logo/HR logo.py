#Replace all ______ with rjust, ljust or center. 

thickness = int(5) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print ((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
    #pass
    
#Top Pillars
for i in range(thickness+1): 
    print ((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    #pass
    
#Middle Belt
for i in range((thickness+1)//2):
    print ((c*thickness*5).center(thickness*6))
    #pass
    
#Bottom Pillars
for i in range(thickness+1):
    print ((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    #pass
    
#Bottom Cone
for i in range(thickness):
    print (((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
    
"""

    H     
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
012345678901234567890123456789
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH
0123456789012345678901234567890123456789
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
012345678901234567890123456789 
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH
0123456789012345678901234567890123456789
012345678901234567890123456789
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H
"""