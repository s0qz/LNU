'''Problem:
Birthday  (VG)
Write a program birthday_candles.py that computes how many boxes of candles a person needs to buy each year for her\his birthday cake.
You can assume that the person reaches an age of 100, the number of candles used each year is the same as the age,
that you save non-used candles from one year to another, and that each box contains 24 candles.
Also, at the end, we want you to print the total number of boxes one has to buy, and how many candles that are available after having celebrated the 100th birthday.
'''
'''Desired output examples:
Before birthday 1, buy 1 box(es)
Before birthday 7, buy 1 box(es)
Before birthday 10, buy 1 box(es)
Before birthday 12, buy 1 box(es)
Before birthday 14, buy 1 box(es)

...

Before birthday 95, buy 3 box(es)
Before birthday 96, buy 4 box(es)
Before birthday 97, buy 5 box(es)
Before birthday 98, buy 4 box(es)
Before birthday 99, buy 4 box(es)
Before birthday 100, buy 4 box(es)

Total number of boxes: 211, Remaining candles: 14
'''

# birthday_candles.py
#
# Author: Samuel Berg
# Date: 05-Sep-2022

CANDLE_SIZE = 24
MAX_AGE = 100

total_boxes = 0
left_candles = 0
years = 0

for years in range(1, 101):
    amount_box = 0
    if years > left_candles:
        while years > left_candles:
            left_candles += CANDLE_SIZE
            total_boxes += 1
            amount_box += 1
        print(f'Before birthday {years}, buy {amount_box} box(es)')
        left_candles -= years
    else:
        left_candles -= years


print(
    f'\nTotal number of boxes: {total_boxes}, Remaining candles: {left_candles}')
