import math

room_floor_length = 2000
floor_to_windowbase = 200
window_side_length = 30
window_upperside_length = 60


def input_military_time_converter(input_time):
    if len(input_time) <= 2:
        return float(input_time) * 100
    else:
        try:
            float(input_time[1:2])
            return float(input_time[:2] + input_time[3:])
        except Exception:
            return float(input_time[:1] + input_time[2:])


def sunlight_angle(time):
    if 2100 < time < 1500:
        return 0
    else:
        time -= 1500
        try:
            remainder = 15/(time % 100)
            time = int(time/100)
            return (time + remainder) * 15
        except ZeroDivisionError:
            return time * 0.15


def find_area_on_floor(angle, bottom, top):
    tan = math.tan(math.radians(angle))
    bottom_tan = bottom/tan
    top_tan = top/tan
    return (top_tan - bottom_tan) * window_upperside_length


first_input = input("Enter the time. Example: (x:xx)\n")
print(find_area_on_floor
    (sunlight_angle
    (input_military_time_converter
    (first_input)), floor_to_windowbase, floor_to_windowbase + window_side_length))
