thickness = int(5) #This must be an odd number
c = 'H'

#Bottom Pillars
for i in range(thickness+1):
    print ((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    
"""
0 - ('HHHHH').center(10) + ('HHHHH').center(30)
1 - ('HHHHH').center(10) + ('HHHHH').center(30)
2 - ('HHHHH').center(10) + ('HHHHH').center(30)
3 - ('HHHHH').center(10) + ('HHHHH').center(30)
4 - ('HHHHH').center(10) + ('HHHHH').center(30)
5 - ('HHHHH').center(10) + ('HHHHH').center(30)

  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH
  
  
  HHHHH   
  HHHHH   
  HHHHH   
  HHHHH   
  HHHHH   
  HHHHH   
0123456789

            HHHHH             
            HHHHH             
            HHHHH             
            HHHHH             
            HHHHH             
            HHHHH             
012345678901234567890123456789		
"""