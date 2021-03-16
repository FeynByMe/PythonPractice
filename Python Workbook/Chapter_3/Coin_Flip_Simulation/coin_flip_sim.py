import random as random

# Initialize the iterations
iter = 1
while (iter <= 1000):
    Bool = True
    seq = []
    stop = []
    while (Bool):
        coin_val = random.random()
        seq.append(coin_val)
        if (len(seq) < 3):
            Bool = True
        else:
            last = seq[-3:]
            a, b, c = last[-3], last[-2], last[-1]
            if ( ((a > 0.5) and (b > 0.5) and (c > 0.5)) or ((a < 0.5) and (b < 0.5) and (c < 0.5)) ):
                Bool = False
            else:
                Bool = True
    string = ''
    for val in seq:
        if (val > 0.5):
            string += ' H '
        else:
            string += ' T '
    #print( "\n" + string + "(" + str(len(seq)) + " flips)")
    stop.append(len(seq))
    iter += 1
                  
print("\n On average, it took " + str(sum(stop)/len(stop)) + " flips.")

