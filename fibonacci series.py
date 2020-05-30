''' Efficient method '''

def calc_fib(n):
    if n<=1 :
        return n
    else:
        fib = [None]*n
        fib[0] = 0
        fib[1] = 1
        for i in range(2,n):
            fib[i] = fib[i-1] + fib[i-2]
    return fib[n-1]

n = int(input())
print(calc_fib(n))

''' can caluclate even the 100th fibonacci series in less time '''
