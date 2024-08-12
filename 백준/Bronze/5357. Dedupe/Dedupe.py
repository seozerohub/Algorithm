def remove_consecutive_duplicates(s):
    result = []
    
    for char in s:
        if not result or result[-1] != char:
            result.append(char)
    
    return ''.join(result)

def main():

    n = int(input())

    for _ in range(n):
        string = input().strip()
        print(remove_consecutive_duplicates(string))

main()