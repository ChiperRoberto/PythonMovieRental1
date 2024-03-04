def greater(x, y):
    return x > y


def himself(x):
    return x


def getClientName(client):
    return client.getClientName()


def getNrFilme(client):
    return client.getNrFilme()


def bubbleSort(l, key=himself, reverse=False, cmp=greater):
    sortFinished = False
    while not sortFinished:
        sortFinished = True
        for i in range(len(l)-1):
            if cmp(key(l[i+1]), key(l[i])) == reverse:
                l[i], l[i+1] = l[i+1], l[i]
                sortFinished = False


def shellSort(l, key=himself, reverse=False, cmp=greater):
    n = len(l)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = l[i]
            j = i
            while j >= gap and cmp(key(temp), key(l[j - gap])) == reverse:
                l[j] = l[j - gap]
                j -= gap
            l[j] = temp
        gap //= 2
