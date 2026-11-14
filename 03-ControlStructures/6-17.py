# Converts time in 24-hour format (hh:mm) to 12-hour format.
#
time_24 = input('Enter time (24-hour format): ').strip()
hours = int(time_24[0:time_24.find(':')])
minutes = time_24[time_24.find(':') + 1:]

if hours < 12:
    suffix = 'am'
else:
    suffix = 'pm'

hours_12 = hours % 12
if hours_12 == 0:
    hours_12 = 12

print(f'Time in 12-hour format: {hours_12}:{minutes}{suffix}')