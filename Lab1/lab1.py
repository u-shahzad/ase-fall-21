# calculator.py

def sum(m,n):
    #TODO
    for x in range(n):
        m = m + 1
    return m

def divide(m,n):
    #TODO
    answer = 0
    while m > 0:
        if n > m:
            return 0
        
        else:
            m = m - n
            answer = answer + 1
    return answer

def main():
    print(sum(-7,-5))
    print(divide(12,2))

if __name__ == '__main__':

    main()