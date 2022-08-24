import sys
import stdio

n = int(sys.argv[1])

power = 1
i = 0
while i <= n:
  # Write the ith power of 2
  stdio.writeln(str(i) + ' ' + str(power) + ' ' + str( i < n))
  power = 2 * power
  i += 1
