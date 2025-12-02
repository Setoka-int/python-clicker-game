def f(s,m):
    if s<=30: return m%2==0
    if m == 0: return 0
    steps = [f(s-3, m-1), f(s-5, m-1), f(s//4, m-1)]
    return any(steps) if m%2!=0 else all(steps)

print([x for x in range(1,31) if not f(x,1) and f(x,2)])