import sys
from datetime import date

birth = date(1989, 10, 29)
now = date.today()

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

age = now - birth

print age.days


