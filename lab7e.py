#!/usr/bin/env python3



class Time:

    """Simple object type for time of the day.

       data attributes: hour, minute, second

    """



    def __init__(self, hour=12, minute=0, second=0):

        self.hour = hour

        self.minute = minute

        self.second = second



    def __str__(self):

        """Return string representation for print()"""

        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'



    def __repr__(self):

        """Return string representation in shell (interactive)"""

        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'



    def format_time(self):

        """Return time object as a formatted string"""

        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'



    def valid_time(self):

        """Check if time is valid"""

        if self.hour < 0 or self.minute < 0 or self.second < 0:

            return False

        if self.hour >= 24 or self.minute >= 60 or self.second >= 60:

            return False

        return true
def change_time(self, seconds):

        """Modify the time object by adding seconds (can be negative)"""

        total_sec = time_to_sec(self) + seconds

        total_sec %= 86400  # Wrap around 24 hours (1 day = 86400 seconds)

        updated = sec_to_time(total_sec)

        self.hour = updated.hour

        self.minute = updated.minute

        self.second = updated.second

        return None



    def sum_times(self, other_time):

        """Return a new Time object which is the sum of this time and another"""

        total_sec = time_to_sec(self) + time_to_sec(other_time)

        total_sec %= 86400

        return sec_to_time(total_sec)
# External helper functions

def time_to_sec(time):

    """Convert time object to total seconds"""

    return time.hour * 3600 + time.minute * 60 + time.second



def sec_to_time(seconds):

    """Convert total seconds to a Time object"""

    time = Time()

    minutes, time.second = divmod(seconds, 60)

    time.hour, time.minute = divmod(minutes, 60)

    return time
