#!/usr/bin/env python
from calendar import TextCalendar

text_calendar = TextCalendar()  # <1>

my_calendar = text_calendar.formatmonth(2022, 4)
print(my_calendar)  # <2>

print()

