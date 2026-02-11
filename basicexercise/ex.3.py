def find_max(temperatures):
    max = 0
    for t in temperatures:
        if t >= max:
            max = t
    return max

def find_min(temperatures):
    min = None
    for t in temperatures:
        if min == None or t <= min :
            min = t
    return min
def days_above(temperatures):
    temp = 17
    count = 0
    for t in temperatures:
        if t > temp:
            count += 1
    return count

temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]


print("Wednesday", temperatures[2])
print ("Max:",  find_max(temperatures) )
print ("Min:",  find_min(temperatures) )
average = sum(temperatures) / len(temperatures)
print("Average:", round(average, 1))
print("Days above: ",days_above(temperatures))
print("Sorted:", sorted(temperatures))
