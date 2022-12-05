# tower of hanoi using statements
step = 0


def towerOfHanoi(n, source, intermediate, destination):
    global step
    if n == 1:
        print("moving disk " + str(n) + " from " + source + " to " + destination)
        step = step + 1
        return
    towerOfHanoi(n - 1, source, destination, intermediate)
    print("moving disk " + str(n) + " from " + source + " to " + destination)
    step = step + 1
    towerOfHanoi(n - 1, intermediate, source, destination)


if __name__ == '__main__':
    n = int(input("Enter the number of disks: "))
    towerOfHanoi(n, "Source", "Helper", "Destination")
    print("Number of steps =", step)
