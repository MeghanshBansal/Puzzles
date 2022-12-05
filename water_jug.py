# There are two jugs of different capacities and an endless supply of water, Create the demanded amount of water by measuring only with the two jugs provided

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def waterjug(from_jug_capacity, to_jug_capacity, to_create):

    print('\tfrom_jug =', from_jug_capacity, 'to_jug =', to_jug_capacity)
    from_jug = from_jug_capacity
    to_jug = 0

    step = 1
    print('Step:', step, '-> (', from_jug, ',', to_jug, ')')

    while from_jug != to_create and to_jug != to_create:
        min_to_transfer = min(from_jug, to_jug_capacity - to_jug)

        to_jug += min_to_transfer
        from_jug -= min_to_transfer

        step += 1
        print('Step:', step, '-> (', from_jug, ',', to_jug, ')')
        if from_jug == to_create or to_jug == to_create:
            break

        if from_jug == 0:
            from_jug = from_jug_capacity
            print('Step:', step, '-> (', from_jug, ',', to_jug, ')')
            step += 1

        if to_jug == to_jug_capacity:
            to_jug = 0
            print('Step:', step, '-> (', from_jug, ',', to_jug, ')')
            step += 1

    print('\n\n')
    return step


def fill_the_jug(n, m, to_create):
    if m > n:
        n, m = m, n
    if to_create % gcd(n, m) != 0:
        return "Not possible"

    else:
        return f'Minimum Number of Steps: {min(waterjug(n, m, to_create), waterjug(m, n, to_create))}'


if __name__ == '__main__':
    print(fill_the_jug(4, 3, 2))
