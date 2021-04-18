class Monitors:

    name = 'Samsung'
    matrix = 'VA'
    res = 'WQHD'
    freq = 60


class Headphones:
    name = 'Sony'
    sensitivity = 108
    micro = True


monitor_1 = Monitors()
monitor_2 = Monitors()
monitor_2.freq = 144
monitor_3 = Monitors()
monitor_3.freq = 70
monitor_4 = Monitors()

headphone_1 = Headphones()
headphone_1.micro = False
headphone_2 = Headphones()
headphone_3 = Headphones()

print(monitor_1.freq, monitor_2.freq, monitor_3.freq, monitor_4.freq)
print(headphone_1.micro, headphone_2.micro, headphone_2.micro,)
