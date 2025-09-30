def hours(k):
    return k // 3600

def minutes(k):
    return (k - (hours(k)*3600)) / 60

k = int(input())

print(f"It is {hours(k)} hours {int(minutes(k))} minutes.")