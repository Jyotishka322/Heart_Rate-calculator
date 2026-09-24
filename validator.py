"""This module validates user input."""

def get_valid_name():

"""Prompt user to type a name that's not empty."""

while True:

name = input("enter your name: ").strip()

if name:

return name

print("invalid input! please enter your name.")

def get_valid_measurement():

"""Prompt user to type a heartbeat count that's a positive integer and a time that is a positive integer measured in seconds."""

while True:

try:

beats = int(input("enter the number of heartbeats counted : "))

time = int(input("enter the time in seconds: "))

if beats < 0:

print("\ninvalid input! number of beats cannot be negative.")

continue

if time <= 0:

input! time must be greater than zero.")

continue

return beats, time

except ValueError:

print(

"\ninvalid input! enter whole numbers "

"for beats and time, in seconds."

)