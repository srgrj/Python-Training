thickness = int(5) #This must be an odd number
c = 'H'
#Top Cone

for i in range(thickness):
    print ((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

print (''.rjust(4) + 'H' + ''.ljust(4))
print ('H'.rjust(4) + 'H' + 'H'.ljust(4))
print ('HH'.rjust(4) + 'H' + 'HH'.ljust(4))
print ('HHH'.rjust(4) + 'H' + 'HHH'.ljust(4))
print ('HHHH'.rjust(4) + 'H' + 'HHHH'.ljust(4))

"""
    H     
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
012345678901234567890123456789
"""