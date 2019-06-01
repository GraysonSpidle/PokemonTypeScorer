import matplotlib.pyplot as plt
from numpy import arange, vectorize

def offensiveWeightFunc(multiplier:float) -> float:
    equation1 = lambda mult: (mult - 1.5)**(2) + 1
    equation2 = lambda mult: -(2.2*(1.5-mult)**0.5)-(0.5*mult)-0.25
    return equation2(multiplier) if multiplier < 1.5 else equation1(multiplier)

def defensiveWeightFunc(multiplier:float) -> float:
    equation1 = lambda mult: -(mult - 1)**(3/2) - 1
    equation2 = lambda mult: (-mult + 1)**(2/3) + 1
    return equation2(multiplier) if multiplier < 1 else equation1(multiplier)

def display():
    x = arange(0,1.5,0.1)
    y = vectorize(offensiveWeightFunc)(x)
    offensive_lines = plt.plot(x,y,'b',label="Offensive")

    x = arange(1.5,6,0.1)
    y = vectorize(offensiveWeightFunc)(x)
    plt.plot(x,y,'b',label="Offensive")

    x = arange(0,1,0.1)
    y = vectorize(defensiveWeightFunc)(x)
    defensive_lines = plt.plot(x,y,'g',label="Defensive")

    x = arange(1,6,0.1)
    y = vectorize(defensiveWeightFunc)(x)
    plt.plot(x,y,'g',label="Defensive")

    plt.axhline(0,0,6)
    plt.axvline(0,-100,100)
    plt.legend(offensive_lines+defensive_lines, ["Offensive", "Defensive"])
    plt.title("Offensive and Defensive Weight Functions")
    plt.xlabel("Multiplier")
    plt.ylabel("Weighted Multiplier")

    plt.show()
