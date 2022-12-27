def arithmetic_arranger(problems, show_answer=False):
  arranged_problems = ""

  if len(problems) > 5:
    return "Error: Too many problems."

  r1 = []
  r2 = []
  r4 = []
  
  for problem in problems:
    data = problem.split()
    if data[1] not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    if not (data[0].isdigit() and data[2].isdigit()):
      return "Error: Numbers must only contain digits."

    if int(data[0]) > 9999 or int(data[2]) > 9999:
      return "Error: Numbers cannot be more than four digits."

    k = len(data[0]) - len(data[2])

    if k > 0:
      data[2] = ' '*k + data[2]
    elif k < 0:
      data[0] = ' '*abs(k) + data[0]

    r1.append('  ' + data[0])
    r2.append(data[1] + ' ' + data[2])

  arranged_problems += '    '.join(r1) + '\n'
  arranged_problems += '    '.join(r2) + '\n'
  arranged_problems += '    '.join(['-'*len(n) for n in r2])

  if show_answer:
    for i in range(len(r1)):
      s=str(int(r1[i]) + int(r2[i].replace(' ',''))).rjust(len(r2[i]))
      r4.append(s)
    
    arranged_problems += '\n' + '    '.join(r4)

  return arranged_problems