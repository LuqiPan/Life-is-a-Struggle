def the_apocalypse(n):
    girl = 0.0
    boy = 0.0
    for i in range(n):
        girl += 0.5 ** (i + 1)
        boy += 0.5 ** (i + 1) * i

    return girl / boy

print the_apocalypse(10)
print the_apocalypse(100)
print the_apocalypse(1000)
