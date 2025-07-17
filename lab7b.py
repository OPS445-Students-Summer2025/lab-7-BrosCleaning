#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum = Time(0, 0, 0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    # Carry over seconds to minutes if seconds >= 60
    if sum.second >= 60:
        sum.minute += sum.second // 60
        sum.second = sum.second % 60
    
    # Carry over minutes to hours if minutes >= 60
    if sum.minute >= 60:
        sum.hour += sum.minute // 60
        sum.minute = sum.minute % 60
    
    return sum

def change_time(time, seconds):

    time.second += seconds

    if valid_time(time) != True:

        while time.second >= 60:

             time.second -= 60

             time.minute +=1

        while time.minute >= 60:

             time.minute -= 60

             time.hour += 1

    return None
