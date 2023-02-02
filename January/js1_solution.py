"""
Strategy

Iteratively get better Ms and build solutions for M based on the solution for M-1

a = 0 for all minimum sums: there is no reason to make it bigger since if you
increase it you will have to increase all other terms by "a" to get
the same result

b is always equal to (d-c) of the minimum sum of M-3

c is equal to 2*(d-c) of M-1 every 3 optimizations and (d-c) of M-1 otherwise

d is the more complex pattern with the following repeating patterns by order:
    1) d_from_M-1 + c_from_M-2/2
    2) d_from_M-1*2 + c_from_M-2
    3) d_from_M-1 + c_from_M-2

This strategy is most useful to calculate M > 8 as the first few iterations do not
yield M+1:
    it1: (0, 0, 0, 0) - M = 1 | sum: 0
    it2: (0, 0, 0, 1) - M = 5 | sum: 1
    it3: (0, 0, 1, 3) - M = 7 | sum: 4

so for it to work properly you need to set b = 1 manually for M = 8 and program a
loop to quickly find d for these iterations

if we set a,b,c,d < n and n = 10e6, then the final solution is:
    (0, 1389537, 3945294, 8646064) - M = 44 | sum: 13980895

works for an n of at least up to 10e16 (with a M = 101)

"""

def f(a, b, c, d):
    i = 1
    while(a+b+c+d) > 0:
        new_a = abs(a - b)
        new_b = abs(b - c)
        new_c = abs(c - d)
        new_d = abs(a - d)
        a,b,c,d = new_a,new_b,new_c,new_d
        #print((a,b,c,d))
        i+=1
    return i


# Set the previous iterations a,b,c,d = 0
M_3 = [0,0,0,0]
M_2 = [0,0,0,0]
M_1 = [0,0,0,0]
M_max = 0

n = int(10e16)
ctr = 2
while True:
    a = 0
    
    b = M_3[3] - M_3[2]
    if M_max == 7:
        b = 1
    
    c = M_1[3] - M_1[2]
    if not ctr % 3:
        c *= 2
    
    if not (ctr+2) % 3:
        d = M_1[3] + M_2[2]
    elif not (ctr +1) % 3:
        d = M_1[3] + int(M_2[2]/2)
    elif not ctr % 3:
        d = M_1[3]*2 + M_2[2]
            
    
    if a > n or b > n or c > n or d > n:
        print('Done!')
        break
    
    M_c = f(a,b,c,d)
    
    if M_c > M_max:    
        print(''+str((a,b,c,d))+' - M = '+str(M_c) +' | sum: '+str(sum([a,b,c,d])))
        M_max = M_c
    else: # This is only needed for iterations of M < 8 
        initial_d = M_1[3]
        
        for d in range(initial_d,n):
            M_c = f(a,b,c,d)
            if M_c > M_max:
                print(''+str((a,b,c,d))+' - M = '+str(M_c) +' | sum: '+str(sum([a,b,c,d])))
                M_max = M_c
                break  
    
    M_3 = M_2
    M_2 = M_1
    M_1 = [a,b,c,d]
    ctr+=1