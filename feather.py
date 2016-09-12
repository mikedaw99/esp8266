import time
import machine
import onewire


def initialiseForTemp():
    """
    Initialise the onewire interface
    """
    # the device is on GPIO14
    dat = machine.Pin(14)
    # create the onewire object
    ds = onewire.DS18B20(onewire.OneWire(dat))
    # scan for devices on the bus
    roms = ds.scan()
    print('found devices:', roms)
    return (ds, roms[0])

def readTemp(ds, rom):
    """
    Get the temperature now
    """
    ds.convert_temp()
    time.sleep_ms(750)
    temp = ds.read_temp(rom)
    return temp

def main():
    """
    main loop run forever
    """
    ds, rom = initialiseForTemp()
    while True:
        #keep running forever
        temp = readTemp(ds, rom)
        print('The temperature is {0}'.format(temp))
        time.sleep(10)

if __name__ == '__main__':
    main()



