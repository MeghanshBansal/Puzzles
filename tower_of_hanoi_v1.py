# tower of hanoi using stacks

from collections import deque

step = 1


def show(a, b, c):
    global step
    stacks = list()
    stacks.append(a)
    stacks.append(b)
    stacks.append(c)
    print(str(step) + " - " + str(sorted(stacks, key=lambda x: x[0])))
    step = step + 1


def towerOfHanoi(n, source, intermediate, destination):
    if n == 1:
        destination.append(source.pop())
        show(source, intermediate, destination)
        return
    towerOfHanoi(n - 1, source, destination, intermediate)
    destination.append(source.pop())
    show(source, intermediate, destination)
    towerOfHanoi(n - 1, intermediate, source, destination)


if __name__ == '__main__':
    n = int(input("Enter the number of disks: "))
    source = deque(['A'])
    for i in range(n, 0, -1):
        source.append(i)
    intermediate = deque(['B'])
    destination = deque('C')
    print("Initial: " + " - " + str(source), str(intermediate), str(destination))
    towerOfHanoi(n, source, intermediate, destination)
    print()
    print("Number of steps =", step - 1)
