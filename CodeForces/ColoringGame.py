def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index+n]))
        index += n
        
        max_val = a[-1]
        count = 0
        
        # Since array is sorted, we only need to check combinations where a[i] + a[j] > max_val
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if a[i] + a[j] <= max_val:
                    continue
                # Find how many k > j
                count += (n - (j + 1))
        
        results.append(str(count))
    
    print('\n'.join(results))
solve()