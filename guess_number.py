from itertools import permutations
from random import shuffle
 
try:
    raw_input
except:
    raw_input = input
try:
    from itertools import izip
except:
    izip = zip
 
digits = '123456789'
size = 4
 
def p_x(x):
    x = x.strip().split(',')
    return tuple(int(s.strip()) for s in x)
 
def xcalc(guess, chosen):
    A = B = 0
    for a,b in izip(guess, chosen):
        if a == b:
            A += 1
        elif a in chosen:
            B += 1
    return A, B
 
possiblities = list(permutations(digits, size))
shuffle(possiblities)
answers = []
xs  = []
 
print ("Playing 猜數字 xAyB  %i 位數字\n" % size)
 
while True:
    ans = possiblities[0]
    answers.append(ans)
    print ("(還有 %i 個可能)" % len(possiblities))
    x = raw_input("第一次猜測是 %2i is %*s. Answer (A, B)? "
                      % (len(answers), size, ''.join(ans)))
    x = p_x(x)
    xs.append(x)
    print("A: %i, B: %i" % x)
    found =  x == (size, 0)
    if found:
        print ("耶終於答對了")
        break
    possiblities = [c for c in possiblities if xcalc(c, ans) == x]
    if not possiblities:
        print ("你的答案沒有在可能的數字之中,應該算錯A跟B了:")
        print ('  ' +
               '\n  '.join("%s -> %s" % (''.join(an),sc)
                           for an,sc in izip(answers, xs)))
        break