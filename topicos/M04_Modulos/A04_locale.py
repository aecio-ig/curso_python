import locale
import calendar

locale.setlocale(locale.LC_ALL, '')

print(locale.getlocale())

print(calendar.calendar(2025))