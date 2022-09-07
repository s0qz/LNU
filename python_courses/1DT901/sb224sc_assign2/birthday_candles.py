# birthday_candles.py
#
# Author: Samuel Berg
# Date: 05-Sep-2022

CANDLE_SIZE = 24
MAX_AGE = 100

total_boxes = 0
remain = 0
years = 0

for years in range(1, 101):
    amount_box = 0
    if years > remain:
        while years > remain:
            remain += CANDLE_SIZE
            total_boxes += 1
            amount_box += 1
        print(f'Before birthday {years}, buy {amount_box} box(es)')
        remain -= years
    else:
        remain -= years


print(
    f'\nTotal number of boxes: {total_boxes}, Remaining candles: {remain}')
