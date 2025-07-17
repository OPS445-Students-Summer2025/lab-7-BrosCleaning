#!/usr/bin/env python3



class Time:

    """Simple object type for time of the day.

       data attributes: hour, minute, second

    """

    def __init__(self, hour=12, minute=0, second=0):

        self.hour = hour

        self.minute = minute

        self.second = second



def format_time(t):

    """Return time object (t) as a formatted string"""

    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'



def valid_time(t):

    """Check for validity of the time object attributes:

       0 <= hour < 24, 0 <= minute < 60, 0 <= second < 60

    """

    if t.hour < 0 or t.minute < 0 or t.second < 0:

        return False

    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:

        return False

    return True



def time_to_sec(time):

    """Convert a time object to total seconds from midnight"""

    total_minutes = time.hour * 60 + time.minute

    total_seconds = total_minutes * 60 + time.second

    return total_seconds



def sec_to_time(seconds):

    """Convert total seconds from midnight to a time object"""

    time = Time()

    minutes, time.second = divmod(seconds, 60)

    time.hour, time.minute = divmod(minutes, 60)

    return time



def sum_times(t1, t2):

    """Add two time objects and return the sum as a new Time object"""

    total_sec = time_to_sec(t1) + time_to_sec(t2)

    # Wrap around 24 hours (86400 seconds)

    total_sec = total_sec % 86400

    return sec_to_time(total_sec)



def change_time(time, seconds):

    """Modify the time object by adding seconds (can be negative)"""

    total_sec = time_to_sec(time) + seconds

    total_sec = total_sec % 86400

    new_time = sec_to_time(total_sec)

    time.hour = new_time.hour

    time.minute = new_time.minute

    time.second = new_time.second

    return None
