###
# Main program using the Thermometer class
#
import thermometer

def main():
    # 1. Create a thermometer
    device = thermometer.Thermometer()
    # 2. Turn thermometer on
    device.turn_on()
    # 3. Measure temperature
    device.measure()
    # 4. Display temperature
    device.display()
    # 5. Turn thermometer off
    device.turn_off()

if __name__ == "__main__":
    main()