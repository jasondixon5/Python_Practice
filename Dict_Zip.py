#! usr/bin/env python
# Dict_Zip.py

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
more_answers = ['arthur', 'bunnies', 'gold']

for q, a, m in zip(questions, answers, more_answers):
    print 'What is your {0}? It is {1} and {2}.'.format(q, a, m)
print(zip(questions, answers, more_answers))