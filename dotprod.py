## TODO: Fill in the dotproduct() function to calculate the
## dot product of two vectors.
##

## Here are the inputs and outputs of the dotproduct() function:
##     INPUTS: vector, vector
##     OUTPUT: dot product of the two vectors
##
##
## The dot product involves mutliplying the vectors element
## by element and then taking the sum of the results
##
## For example, the dot product of [9, 7, 5] and [2, 3, 4] is
## 9*2+7*3 +5*4 = 59
##
## Hint: You can use a for loop. You will also need to accumulate
## the sum as you iterate through the vectors. In Python, you can accumulate
## sums with syntax like w = w + 1

x2 = []

def dotproduct(vectora, vectorb):

    # variable for accumulating the sum
    result = 0

    # TODO: Use a for loop to multiply the two vectors
    # element by element. Accumulate the sum in the result variable
    v3 = 0
    lenx0 = len(vectora)
    lenx1 = len(vectorb)

    for x in range(lenx0):
        #for y in range(lenx1):
        v1 = vectora[x]
        v2 = vectorb[x]
        v3 += v1 * v2

    print(v3)
    return v3

vectora = [7,2,3]
vectorb =  [1, 10, 4]
dotproduct(vectora, vectorb)
# should be 39 (7*1 + 2*10 + 3*4)
v1_dot_v2 = dotproduct(vectora, vectorb)

print(vectora, "dot", vectorb, "equals", v1_dot_v2)
