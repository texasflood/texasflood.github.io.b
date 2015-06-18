#!/usr/bin/env python
while True:
  people = raw_input('Enter people split by a comma:\n')
  people = [x.strip() for x in people.split(',')]
  if len(people) != len(set(people)):
    print 'There are duplicates in the list'
  else:
    break

#print 'People array:'
#print people
peopleDict = {}
for person in people:
  idx = 1
  peopleDict[person] = []
  while True:
    finished = raw_input('Did ' + person + ' pay for anything? (y/n)\n')
    if finished in ['y', 'n']:
      break
    else:
      print 'Enter either y or n!'
  if finished != 'n':
    while True:
      print 'Entering expense number ' + str(idx) + ' for ' + person
      expense = {}
      expense['name'] = raw_input('For ' + person + ' enter expense name\n')
      while True:
        try:
          expense['amount'] = float(raw_input('For expense ' + expense['name'] + ' incurred by ' + person + ', enter amount\n'))
        except ValueError:
          print 'Invalid number'
          continue
        break

      while True:
        expense['responsibles'] = raw_input('Enter people responsible split by a comma:\n')
        expense['responsibles'] = [x.strip() for x in expense['responsibles'].split(',')]
        if set(expense['responsibles']) <= set(people):
          break
        else:
          print 'Some people you entered as responsible for the bill are not in the original list, try again'

      peopleDict[person].append(expense)
      idx += 1
      while True:
        finished = raw_input('Finished with ' + person + '\'s expenses? (y/n)\n')
        if finished in ['y', 'n']:
          break
        else:
          print 'Enter either y or n!'
      if finished == 'y':
        break

#print peopleDict

owedArray = []
for i in people:
  owedArray.append([0]*len(people))

for person in people:
  for expense in peopleDict[person]:
    for debtor in expense['responsibles']:
      if person != debtor:
        owedArray[people.index(person)][people.index(debtor)] += float(expense['amount'])/len(expense['responsibles'])
        owedArray[people.index(debtor)][people.index(person)] -= float(expense['amount'])/len(expense['responsibles'])

print
for idx, debtors in enumerate(owedArray):
  printed = False
  for jdx, debtor in enumerate(debtors):
    if debtor > 0:
      if not printed:
        print people[idx] + ' is owed:'
        printed = True

      print '  ' + people[jdx] + u' \xA3%.2f' % debtor
  print

for idx, debtees in enumerate(owedArray):
  printed = False
  for jdx, debtee in enumerate(debtees):
    if debtee < 0:
      if not printed:
        print people[idx] + ' owes:'
        printed = True

      print '  ' + people[jdx] + u' \xA3%.2f' % -debtee

#print owedArray
