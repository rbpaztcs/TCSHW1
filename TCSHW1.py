ones = ["", "isa", "dalawa", "tatlo", "apat", "lima", "anim", "pito", "walo", "siyam", "sampu"]
tens = ["","labing","dalawampu","tatlompu","apatnapu", "limampu","animnapu","pitompu","walompu","siyamnapu"]
millions =  = ["","libo","milyon", "bilyon"]

def numXXX(n):
    q = n % 10 # singles digit
    w = ((n % 100) - q) / 10 # tens digit
    e = ((n % 1000) - (b * 10) - q) / 100 # hundreds digit
    x = ""
    y = ""
     if e != 0 and w == 0 and q == 0:
        t = ones[e] + "ng daan"
    elif q != 0:
        t = ones[e] + "naraan"
    if w <= 1:
        y = ones[n%100]
    elif w > 1:
        y = twenties[w] + ones[q]
    st = x + y
    return st

def converter(n):
    if = num == 0: return 'zero'
