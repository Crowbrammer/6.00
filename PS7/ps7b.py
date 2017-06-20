# ps7b.py

import pylab
import random

def YahtzeeTest():
    Yahtzees = 0
    print("Yahtzees:", Yahtzees)
    for roll in range(100000):
        all_curr_dice_values = []
        for each_die in range(5):
            if random.random() < 1/6:
                all_curr_dice_values.append(True)
            else:
                all_curr_dice_values.append(False)
                break
        if False in all_curr_dice_values:
            continue
        else: Yahtzees += 1
    print("Yahtzees:", Yahtzees)
    return Yahtzees

def plotYahtzeeResults(trials, Yahtzee_results):
    pylab.title('# of Yahtzee Rolls')
    pylab.xlabel('Sample')
    pylab.ylabel('# of Yahtzee Rolls')
    pylab.plot(range(trials), Yahtzee_results)
    pylab.figure()

    pylab.title('Percentage of Yahtzee Rolls / 100,000 Plays')
    pylab.xlabel('Sample')
    pylab.ylabel('Proportion of Yahtzee Rolls')
    print([x/1000 for x in Yahtzee_results])
    pylab.plot(range(trials), [x/1000 for x in Yahtzee_results])
    pylab.figure()

list_of_Yahtzees = []
for test in range(100):
    list_of_Yahtzees.append(YahtzeeTest())

plotYahtzeeResults(100, list_of_Yahtzees)
pylab.show()
