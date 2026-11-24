###
# Class describing a smartphone
#
# States (attributes): brand, battery level, is the screen on, volume
# Behaviors (methods): turn on the screen, turn off the screen,
#                      charge the battery, make a call, show status
#
class Phone():
    def __init__(self, brand, model):
        # states
        self.brand = brand
        self.model = model
        self.battery = 50        # battery level in %
        self.screen_on = False

    # behaviors - method names are verbs
    def turn_screen_on(self):
        self.screen_on = True
        print('Screen turned on.')

    def turn_screen_off(self):
        self.screen_on = False
        print('Screen turned off.')

    def charge(self, percent):
        # the battery level cannot exceed 100%
        self.battery = min(100, self.battery + percent)
        print(f'Charged by {percent}%.')

    def call(self, number):
        if not self.screen_on:
            print('Turn the screen on first.')
        elif self.battery < 5:
            print('Battery too low to make a call.')
        else:
            # every call uses 5% of the battery
            self.battery -= 5
            print(f'Calling {number}...')

    def show_status(self):
        screen = 'on' if self.screen_on else 'off'
        print(f'{self.brand} {self.model} | battery: {self.battery}% | screen: {screen}')


def main():
    phone = Phone('Samsung', 'Galaxy S24')
    phone.show_status()
    phone.call('555-123-456')     # screen is off
    phone.turn_screen_on()
    phone.call('555-123-456')
    phone.charge(70)
    phone.show_status()
    phone.turn_screen_off()
    phone.show_status()

if __name__ == "__main__":
    main()