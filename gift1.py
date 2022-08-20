'''
ID: kcp7ea1
LANG: PYTHON3
PROG: gift1
'''
# we take in the first line of the input file
file_in = open('gift1.in','r')
file_out = open('gift1.out','w')
group_size = file_in.readline().strip()

# convert that line into an integer save it to a variable group_size
group_size = int(group_size)
group = {}

# loop through the file to get the group into a dictionary with their intial amounts set to 0
file_line = 0
while file_line < group_size :
    name = file_in.readline().strip()
    group[name]  = 0
    file_line += 1

# subtract the initial amount from the approriate group donator
while file_in:

    donater = file_in.readline().strip()
    print(donater)
    dono_info = file_in.readline().strip().split() # creates an array of the amount and how many folks are getting it
    if len(dono_info) < 1:
        break
    donation = int(dono_info[0])
    splits = int(dono_info[1])

    if splits != 0:
        group[donater] -= donation
        group[donater] += donation % splits
        # loop through the dono list
        for i in range(0, splits):
            recipient = file_in.readline().strip()
            group[recipient] += donation // splits
file_in.close()

for keys in group:
   file_out.write(f'{keys} {group[keys]} \n')

# subtract the initial amount from the approriate group member
# print(file_in.readline())
# print(file_in)
# for member in file
