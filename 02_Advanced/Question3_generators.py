def new_range(start, stop, step):
    current = start

    while True:
        if step < 0 and current <= stop:
            break
        if step > 0 and current >= stop:
            break

        yield current
        current += step

r = new_range(-2, -5, -1)
for x in r:
    print(x)
