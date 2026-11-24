###
# Class describing a TV set (final version - tasks 4-1 to 4-6)
#
class TV:
    # volume limits - the same for every TV, so they are class attributes
    MIN_VOLUME = 0
    MAX_VOLUME = 10

    def __init__(self):
        self.is_on = False      # initially the TV is turned off
        self.channel_no = 1     # initially channel 1
        self.channels = []      # TV not programmed - no channels yet
        self.volume = 0         # initial volume level

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    # Sets the number of the current channel
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    # Sets the list of available channel names
    def set_channels(self, channels_list):
        self.channels = channels_list

    # Prints the numbered list of available channels
    def show_channels(self):
        print('Channel list:')
        if len(self.channels) == 0:
            print('No channels available.')
        for number, name in enumerate(self.channels, start=1):
            print(f'{number}. {name}')

    # Increases the volume by 1, but not above the maximum
    def volume_up(self):
        if self.volume < TV.MAX_VOLUME:
            self.volume += 1

    # Decreases the volume by 1, but not below the minimum
    def volume_down(self):
        if self.volume > TV.MIN_VOLUME:
            self.volume -= 1

    # Prints the TV status; channel and volume only when the TV is on
    def show_status(self):
        if self.is_on:
            status = f'TV is on, channel {self.channel_no}'
            # the channel name only if this number is on the list
            # (channel numbers start at 1, list indexes at 0)
            if 1 <= self.channel_no <= len(self.channels):
                status += f' ({self.channels[self.channel_no - 1]})'
            status += f', volume {self.volume}'
            print(status)
        else:
            print('TV is off')