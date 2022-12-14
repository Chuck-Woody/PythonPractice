import sys
import stdio

a = int(sys.argv[1])
b = int(sys.argv[2])

print(f'the argv attributes of sys are: {sys.argv}')

total = a + b
diff = a - b
prod = a * b
qout = a // b
rem = a % b
exp = a ** b

stdio.writeln(str(a) + ' + ' + str(b) + ' = ' + str(total))
stdio.writeln(str(a) + ' - ' + str(b) + ' = ' + str(diff))
stdio.writeln(str(a) + ' * ' + str(b) + ' = ' + str(prod))
stdio.writeln(str(a) + ' // ' + str(b) + ' = ' + str(qout))
stdio.writeln(str(a) + ' % ' + str(b) + ' = ' + str(rem))
stdio.writeln(str(a) + ' ** ' + str(b) + ' = ' + str(exp))