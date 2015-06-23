N = int(input())

space = (list(range(N-1,-1,-1)))
hash = (list(range(1,N+1)))

for a,b in(zip(space,hash)):
    answer = ' '*a + '#'*b
    print(answer)
    
