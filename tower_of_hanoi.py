from collections import deque

# Count the number of steps taken to complete the transfer
step = 1


# Function to show the current state of the towers
def show(a, b, c):
    global step
    stacks = list()
    stacks.append(a)
    stacks.append(b)
    stacks.append(c)
    print("    State" + " - " + str(sorted(stacks, key=lambda x: x[0])))
    print("\n")
    step = step + 1


def towerOfHanoi(n, source, intermediate, destination):
    if n == 1:
        '''
            To print the step, i.e. where we are moving the disk
        '''
        s = source.popleft()
        source.appendleft(s)
        d = destination.popleft()
        destination.appendleft(d)
        print(str(step) + " - " + "moving disk " + str(n) + " from " + s + " to " + d)

        '''
            Moving the disk
        ''' 
        destination.append(source.pop())
        show(source, intermediate, destination)
        return

    '''
        To print the step, i.e. where we are moving the disk
    '''
    towerOfHanoi(n - 1, source, destination, intermediate)
    s = source.popleft()
    source.appendleft(s)
    d = destination.popleft()
    destination.appendleft(d)
    print(str(step) + " - " + "moving disk " + str(n) + " from " + s + " to " + d)

    '''
        Moving the disk
    '''
    destination.append(source.pop())
    show(source, intermediate, destination)
    towerOfHanoi(n - 1, intermediate, source, destination)


if __name__ == '__main__':
    n = int(input("Enter the number of disks: "))
    print("\n")
    source = deque(['A'])
    for i in range(n, 0, -1):
        source.append(i)
    intermediate = deque(['B'])
    destination = deque('C')
    print("Initial: " + " - " + str(source), str(intermediate), str(destination))
    print("\n")
    towerOfHanoi(n, source, intermediate, destination)
    print()
    print("Number of steps =", step - 1)
    print("\n")
