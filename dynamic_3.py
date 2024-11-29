#https://www.spoj.com/problems/ACODE/

def dynamic(inp):
    if inp == "0":
        return 0

    n = len(inp)
    
    dp = [0] * (n + 1)
    
    dp[0] = 1
    
    dp[1] = 1 if inp[0] != '0' else 0

    for i in range(2, n + 1):
        if inp[i - 1] != '0':
            dp[i] += dp[i - 1]
        
        if '10' <= inp[i - 2:i] <= '26' and inp[i - 2] != '0':
            dp[i] += dp[i - 2]

    return dp[n]


def main():
    while True:
        inp = input().strip()
        if inp == "0":
            break
        print(dynamic(inp))


if __name__ == "__main__":
    main()
