if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        
        answer = [a&b for a in range(n+1) for b in range(n+1) if a&b < k and a != b]
        print(max(answer))
