import sys
import stdio

n = int(sys.argv[1])

v = 1
while v <= n // 2:
  v *= 2

# for each power of 2 in v | so for 16 we have 16 8 4 2 1
while v > 0:
  if n < v:
    stdio.write(0) # if the number is less than the the power of 2 write a 0
  else:
    stdio.write(1) # if the number is more than the power of 2 write a 1
    n -= v # subtract the power of 2 off of the value 
  v //= 2 # reduce the power of 2 by 1 power of 2. 
stdio.writeln()