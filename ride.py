"""
ID: kcp7ea1
LANG: PYTHON3
PROG: ride
"""
from curses.ascii import isalpha


file_in = open('ride.in','r')
file_out = open ('ride.out', 'w')

alphabet = {
  'A': 1,
  'B': 2,
  'C': 3,
  'D': 4,
  'E': 5,
  'F': 6,
  'G': 7,
  'H': 8,
  'I': 9,
  'J': 10,
  'K': 11,
  'L': 12,
  'M': 13,
  'N': 14,
  'O': 15,
  'P': 16,
  'Q': 17,
  'R': 18,
  'S': 19,
  'T': 20,
  'U': 21,
  'V': 22,
  'W': 23,
  'X': 24,
  'Y': 25,
  'Z': 26
}
comet_product = 1
ride_product = 1
count = 0 
for line in file_in:
  print(line)
  for char in line:
    if char.isalpha():
      if count > 0 :
        ride_product *= alphabet.get(char)
      else:
        comet_product *= alphabet.get(char)
  count += 1

if comet_product % 47 == ride_product % 47:
  file_out.write("GO" +'\n')
else:
  file_out.write("STAY" + '\n')



# file_out.write(x +'\n')
# file_out.write('hello' + '\n')