# Script to help formalize the concept of
# "minaml expression"

import itertools

# Xn is target, Yn is distractor, Zn is distractor

X = {"chair", "green", "wooden", "large"}
Y = {"chair", "red", "wooden", "large"}
Z = {"chair", "blue", "wooden", "large"}

X1 = {"chair", "green", "wooden", "large"}
Y1 = {"chair", "green", "metal", "large"}
Z1 = {"chair", "blue", "wooden", "large"}

X2 = {"chair", "green", "wooden", "large"}
Y2 = {"chair", "green", "metal", "small"}
Z2 = {"table", "blue", "wooden", "large"}


# findout which subset of X uniquely identifies X in the set of all sets
# of attributes
def find_minal_expression(x, y, z):
    subsets_x = []  # all possible ways to refer to X
    subsets_y = []  # all possible ways to refer to Y
    subsets_z = []  # all possible ways to refer to Z
    for i in range(len(x) + 1):
        subsets_x.extend(itertools.combinations(x, i))
        subsets_y.extend(itertools.combinations(y, i))
        subsets_z.extend(itertools.combinations(z, i))
    subsets_x = [set(subset) for subset in subsets_x]
    subsets_y = [set(subset) for subset in subsets_y]
    subsets_z = [set(subset) for subset in subsets_z]

    subsets_x = sorted(subsets_x, key=len, reverse=True)
    subsets_y = sorted(subsets_y, key=len, reverse=True)
    subsets_z = sorted(subsets_z, key=len, reverse=True)

    RE_candidate = set()
    counter = 0
    for subset in subsets_x:
        if subset not in subsets_y and subset not in subsets_z:
            RE_candidate = subset
            counter += 1
            print(f"Candidate {counter}: {RE_candidate}")
        else:
            continue
    return RE_candidate


print(find_minal_expression(X, Y, Z))  # Output: {'green'}
print(find_minal_expression(X1, Y1, Z1))  # Output: {'wooden', 'green'}
print(find_minal_expression(X2, Y2, Z2))  # Output: {'green', 'large'}
