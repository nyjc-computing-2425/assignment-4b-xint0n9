stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below

check = True
if check ==True:
  for i in range(len(stdform)):
      if stdform[i] not in ['E','x','.','-','^','0','1','2','3','4','5','6','7','8','9']:
            check = False
            break
  if stdform.count('.')!=1 or stdform.count('x')!=1 or stdform.count('^')!=1:
      check = False
  m,e = stdform.split('x10^')
  if e.strip('-').isnumeric() == False:
      check = False
if check == True:
      print('This number in E notation is', m+'E'+e+'.')
else:
      print('Error converting to scientific E notation.')