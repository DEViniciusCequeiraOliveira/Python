def incomodam(n):
    if n == 1:
        return "incomodam "
    elif n > 1:
        return n * "incomodam "

def elefantes(n):
    if n < 1:
        return ""
    elif n == 1:
        return "Um elefante incomoda muita gente"
    elif n > 1:
        return elefantes(n-1) + f"\n{n} elefantes {incomodam(n)}muito mais\n{n} elefantes incomodam muita gente"
