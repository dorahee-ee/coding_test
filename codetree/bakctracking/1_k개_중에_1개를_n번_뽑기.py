k, n = map(int, input().split())
selected_nums = []

def print_permutation():
    for num in selected_nums:
        print(num, end= ' ')
    print()

def find_permutation(cnt):
    if cnt == n:
        print_permutation()
        return
    
    for i in range(1, k+1):
        selected_nums.append(i)
        find_permutation(cnt+1)
        selected_nums.pop()

find_permutation(0)