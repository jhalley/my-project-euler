#matrix = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]
#leaf_sums = {((4,4),0): matrix[4][4]}

matrix = None
leaf_sums = None

def load_matrix():
    global matrix
    global leaf_sums

    with open('matrix.txt') as f:
        x = ''.join(f.readlines())
        matrix = [[int(j) for j in i.split(',')] for i in x.split('\n')[:-1]]
        leaf_sums = {((79, 79),0): matrix[79][79]}

# Our strategy is to build up the minimum sum from all possible leaves from the bottom up
def pe81():
    while True:
        #print leaf_sums
        if ((0,0),0) in leaf_sums:
            return leaf_sums[((0,0),0)]
        elif ((0,0),1) in leaf_sums:
            return leaf_sums[((0,0),1)]
        else:
            # Find the smallest number amongst the leaves
            curr_smallest_leaf = min(leaf_sums, key=leaf_sums.get)
            # Get the sum of the leaves above and to the left of the current smallest leaf, and add them to the leaves array
            if curr_smallest_leaf[0][0] > 0:
                up_leaf = (curr_smallest_leaf[0][0] - 1, curr_smallest_leaf[0][1])
                up_leaf_sum = leaf_sums[curr_smallest_leaf] + matrix[up_leaf[0]][up_leaf[1]]
                up_leaf_key = (up_leaf, 0) if (up_leaf, 0) not in leaf_sums else (up_leaf, 1)
                leaf_sums[up_leaf_key] = up_leaf_sum
            if curr_smallest_leaf[0][1] > 0:
                left_leaf = (curr_smallest_leaf[0][0], curr_smallest_leaf[0][1] - 1)
                left_leaf_sum = leaf_sums[curr_smallest_leaf] + matrix[left_leaf[0]][left_leaf[1]]
                left_leaf_key = (left_leaf, 0) if (left_leaf, 0) not in leaf_sums else (left_leaf, 1)
                leaf_sums[left_leaf_key] = left_leaf_sum
            # Remove current leaf from the leaves array
            del(leaf_sums[curr_smallest_leaf])

load_matrix()
print pe81()
