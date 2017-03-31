def is_power_of_two(number):
    return (number & (number - 1)) == 0

for i in range(32):
    print is_power_of_two(2 ** i)
print '-----'
print is_power_of_two(38)
print is_power_of_two(39)
