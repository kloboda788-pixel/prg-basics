###
# Module with a class describing a medical thermometer
#
import random

class Thermometer:
    MIN_TEMP = 34.0
    MAX_TEMP = 42.0

    def __init__(self):
        self.is_on = False
        self.temperature = None    # nothing measured yet

    def turn_on(self):
        self.is_on = True
        print('Thermometer on.')

    def turn_off(self):
        self.is_on = False
        print('Thermometer off.')

    # Measures the temperature: a random value 34.0-42.0 with 0.1 accuracy
    def measure(self):
        if not self.is_on:
            print('Turn the thermometer on first.')
            return
        # random.uniform() gives a real number from the range,
        # round(..., 1) keeps one decimal place (accuracy 0.1)
        self.temperature = round(random.uniform(Thermometer.MIN_TEMP,
                                                Thermometer.MAX_TEMP), 1)

    # Displays the measured temperature with fever / critical messages
    def display(self):
        if self.temperature is None:
            print('No measurement.')
            return
        message = f'Temperature: {self.temperature}C'
        if self.temperature >= 37.0:
            message += ' (fever)'
        print(message)
        if self.temperature >= 41.0:
            print('CRITICAL TEMPERATURE!!')