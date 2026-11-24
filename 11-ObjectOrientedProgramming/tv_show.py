###
# Main program using the TV class (tasks 4-1 to 4-6)
#
import tv

# 4-1: turning the TV on and off
def task_1():
    my_tv = tv.TV()          # 1. Create TV set
    my_tv.show_status()      # 2. Show TV status
    my_tv.turn_on()          # 3. Turn TV on
    my_tv.show_status()      # 4. Show TV status
    my_tv.turn_off()         # 5. Turn TV off
    my_tv.show_status()      # 6. Show TV status

# 4-2: the channel number is printed only when the TV is on
def task_2():
    my_tv = tv.TV()
    my_tv.turn_on()
    my_tv.show_status()
    my_tv.turn_off()
    my_tv.show_status()

# 4-3: changing the channel
def task_3():
    my_tv = tv.TV()
    my_tv.show_status()
    my_tv.turn_on()
    my_tv.show_status()
    my_tv.set_channel(5)
    my_tv.show_status()
    my_tv.turn_off()
    my_tv.show_status()

# 4-4: the list of channels
def task_4():
    my_tv = tv.TV()
    my_tv.show_status()
    my_tv.turn_on()
    my_tv.show_status()
    my_tv.show_channels()
    my_tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery'])
    my_tv.show_channels()
    my_tv.show_status()
    my_tv.turn_off()

# 4-5: the channel name in the status
def task_5():
    my_tv = tv.TV()
    my_tv.turn_on()
    my_tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox',
                        'Discovery', 'Eurosport'])
    for channel in [4, 1, 7, 9, 2]:
        my_tv.set_channel(channel)
        my_tv.show_status()     # channel 9 is not on the list - no name

# 4-6: volume control in the range 0-10
def task_6():
    my_tv = tv.TV()
    my_tv.turn_on()
    my_tv.show_status()
    my_tv.volume_down()         # already 0 - stays 0
    my_tv.show_status()
    for i in range(12):         # 12 times up - stops at 10
        my_tv.volume_up()
    my_tv.show_status()
    my_tv.volume_down()
    my_tv.volume_down()
    my_tv.show_status()

def main():
    tasks = [task_1, task_2, task_3, task_4, task_5, task_6]
    for number, task in enumerate(tasks, start=1):
        print(f'=== Task 4-{number} ===')
        task()
        print()

if __name__ == "__main__":
    main()