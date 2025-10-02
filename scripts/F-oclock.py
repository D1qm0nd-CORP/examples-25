#TODO: FIX 8/10
import math
def hours(minutes):
    return minutes // 60

def current_hours(hour):
    if hour >= 24:
        return (hour // 24) - 1 
    return hour

def currentMinutes(minutes):
    return minutes - (hours(minutes) * 60)

minutes = abs(int(input()))

print(f"{current_hours(hours(minutes))} {currentMinutes(minutes)}" )




