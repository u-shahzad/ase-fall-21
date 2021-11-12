# calculator.py

def sum(m, n):
    result = m
    if n < 0:
        for i in range(abs(n)):
            result -= 1
    else:
        for i in range(n):
            result += 1
    return result

# def divide(m,n):
#     result = 0
#     negativeResult = m > 0 and n < 0 or m < 0 and n > 0
#     n = abs(n)
#     m = abs(m)

#     while (m - n >= 0):
#         m -= n
#         result+=1

#     result = -result if negativeResult else result

#     return result

def divide(m,n):
    if n==0:
        raise ZeroDivisionError
    negative=(((m<0) and  not (n<0)) or (not (m<0) and (n<0)))
    i=-1
    m=abs(m)
    n=abs(n)
    while m>=0:
        m-=n
        i+=1
    if negative:
        return i*-1
    else:
        return i