# IronMan is ready for battle! He starts his battle at location 0 moves in 1-unit increments toward his 
# final showdown at location n−1. 
# Each location i has a power value, pi. If pi < 0, then there is an enemy at location i that he must lose pi power to beat;
# if pi ≥ 0, then he will restore pi power at location i. IronMan dies if his armor charge becomes < 1 at any point 
# either during or after a fight, so he needs a proper initial charge to survive all possible fights in his battle 
# traveling from location 0 to location n−1. Help him find the minimum charge needed to survive all fights in the battle!
# Complete the ironMan function in your editor. It has 1 parameter: an array of n integers, p, 
# where each index i (0 ≤ i < n) describes the power charge lost or gained at battle location i. If the value at some pi < 0, 
# it represents the amount of charge IronMan must deplete to defeat the enemy; otherwise, it represents the amount of charge that 
# he can restore at that location. Your function must return an integer denoting the minimum starting charge IronMan needs to 
# survive all fights.



def  ironMan(p):
    if len(p) == 0:
        return 1
    minPower = 0
    currPower = 0
    for val in p:
        currPower += val
        if currPower <= 0:
            shouldBeCurrPower = (currPower * -1) + 1
            currPower -= val
            minPower += shouldBeCurrPower
            currPower += shouldBeCurrPower + val
    return minPower