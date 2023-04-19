import random


feet_in_miles = 5280
meters_in_kms = 1000

beatles = ["tom","harry","john","wick","sun"]

def get_file_ext(filename):
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1, num)