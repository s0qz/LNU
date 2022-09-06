import random
'''Problem:
They say that if you roll a die enough times, you should get about the same number of ones, twos, threes and so on.
But is that true? Create a program called roll_the_die.py which rolls a die and stores how many times it comes up at one, two, three and so on.
It will do this many times, more on this a bit further down. You will notice that for few rolls, there is quite a difference between how many times the different faces will show up.
Calculate the difference between the face that turns up the most times and the face that shows up the least times. (most - least) / (most) ?
This should then be divided with the number of the face that was shown the most to give you a sort of ratio (in percent) of the difference.
This should then be done 20 times with increasing number of times to roll the die, from 10 to 20 to 40 and so on by doubling the number of rolls each time.
Present it like shown below:
'''
'''Desired output examples:
For 10 rolls, the difference is 100.0%
For 20 rolls, the difference is 100.0%
For 40 rolls, the difference is 70.59%
For 80 rolls, the difference is 58.97%
For 160 rolls, the difference is 27.87%
For 320 rolls, the difference is 16.96%
For 640 rolls, the difference is 13.54%
For 1280 rolls, the difference is 7.94%
For 2560 rolls, the difference is 4.82%
For 5120 rolls, the difference is 3.36%
For 10240 rolls, the difference is 3.97%
For 20480 rolls, the difference is 2.74%
For 40960 rolls, the difference is 2.18%
For 81920 rolls, the difference is 1.83%
For 163840 rolls, the difference is 1.36%
For 327680 rolls, the difference is 1.23%
For 655360 rolls, the difference is 0.9%
For 1310720 rolls, the difference is 0.4%
For 2621440 rolls, the difference is 0.18%
'''


def roll_the_die(N):
    stored_rolls = [0, 0, 0, 0, 0, 0]
    for i in range(N):
        die = random.randint(0, 5)
        stored_rolls[die] += 1

    most = max(stored_rolls)

    least = min(stored_rolls)

    difference = round(((most - least) / most) * 100, 2)

    print(f'For {N} rolls, the difference is {difference}%')


for i in [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480, 40960, 81920, 163840, 327680, 655360, 1310720, 2621440, 5242880]:
    roll_the_die(i)
