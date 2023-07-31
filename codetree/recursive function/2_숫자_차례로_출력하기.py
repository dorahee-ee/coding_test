n = int(input())

def print_nums(n):
    if n == 0:
        return
    print_nums(n-1)
    print(n, end=' ')

def print_nums_backward(n):
    if n == 0:
        return
    print(n, end=' ')
    print_nums_backward(n-1)

print_nums(n)
print()
print_nums_backward(n)