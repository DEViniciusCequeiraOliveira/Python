def maximo(n,n1,n2):
    if n>= n1:
        if n >= n2:
            return n
        elif n <= n2:
            return n2

    elif n <= n1:
        if n1 > n2:
            return n1

        elif n1 <= n2:
            return n2

