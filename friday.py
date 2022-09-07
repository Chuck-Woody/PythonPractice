months =  {
  1: 31,
  2: 28,
  3: 31,
  4: 30,
  5: 31,
  6: 30,
  7: 31,
  8: 31,
  9: 30,
  10: 31,
  11: 30,
  12: 31
}

weekday_counter = {
  5: 0,
  6: 0,
  0: 0,
  1: 0,
  2: 0,
  3: 0,
  4: 0
}

START_DATE = {
  'month': 1,
  'day': 1,
  'year': 1900
}

file_in = open('friday.in','r')
N = int(file_in.readline())
file_out = open('friday.out', 'w')
END_DATE = {
  'month': 12,
  'day': 31,
  'year': 1900 + N 
}

curr_date = {
  'month': 1,
  'day': 1,
  'year': 1900
}

def stringDate(dateObject):
  date_string = str(dateObject['month']) + '/' + str(dateObject['day']) + '/' + str(dateObject['year'])

  return date_string

current = stringDate(curr_date)
end = stringDate(END_DATE)
rawdays = 1

while current != end:
  if (curr_date['day'] == 13):
    weekday_counter[rawdays % 7] += 1
    print(f"{stringDate(curr_date)} | {rawdays} | max_days:{months[curr_date['month']]}")
    print(weekday_counter)

  if ( curr_date['year'] % 4 == 0 and curr_date['year'] % 100 != 0):
    months[2] = 29
  elif ( curr_date['year'] % 400 == 0):
    months[2] = 29
  else:
    months[2] = 28

  # if the day exceeds month[days] then tick the month up by one
  if (curr_date['day'] > months[curr_date['month']]):
    curr_date['month'] += 1
    curr_date['day'] = 1

  if (curr_date['month'] > 12):
    curr_date['year'] += 1
    curr_date['month'] = 1
  
  curr_date['day'] += 1
  rawdays += 1

  current = stringDate(curr_date)

for key in weekday_counter:
  file_out.write(f'{weekday_counter[key]} ')