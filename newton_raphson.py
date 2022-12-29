import numpy as np

########################################################################

with open("input.txt", "r") as f:
    x_i = float(f.readline())
    epsilon_s = float(f.readline())
    max_itr = int(f.readline())
    m = int(f.readline())
    n = []
    for i in range(0, m + 1, 1):
        w = float(f.readline())
        n.append(w)


#######################################################################

def function(x):
    p1 = np.poly1d(n)
    return p1(x)

###########################################################################


def derivative(x):
    p2 = np.poly1d(n)
    p3 = np.polyder(p2, 1)
    return p3(x)

##########################################################################
out = open("output.txt", "w")

def newtonrephson(a):
    i = 1
    epsilon_a = 1000
    while epsilon_a >= epsilon_s and i <= max_itr:
        x = float(abs(a - (function(a)/derivative(a))))
        epsilon_a = float(abs((x - a)/x))

        print("Iteration number: ", i, " x(i) = ", round(a, 4), " x(i+1) = ", round(x, 4),
              " epsilon_a = ", round(epsilon_a, 4))
        out.write("Iteration number: %d  " % i)
        out.write("x_i = %.4f  " % a)
        out.write("x_i+1 =  %.4f  " % x)
        out.write("epsilon_a = %.4f  \n" % epsilon_a)
        a = x
        i = i+1
    return x

answer = newtonrephson(x_i)
print("The root is: ", round(answer, 4))
out.write("\nThe Final root is: %.4f " % answer)