# time formats

def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f'{hours:02d}:{minutes:02d}'
    else:                                  
        if hours < 12:                     
            suffix = 'AM'                 
        else:
            suffix = 'PM'
        hours_12 = hours % 12                  
        if hours_12 == 0:                  
            hours_12 = 12                 
        return f'{hours_12}:{minutes:02d} {suffix}'

print(time_string(13, 10, '12'))