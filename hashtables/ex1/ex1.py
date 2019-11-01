#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    # BRUTE FORCE
    # for i in range(len(weights) - 1):
    #     for j in range(i+1, len(weights)):
    #         print(weights[i] + weights[j])
    #         if weights[i] + weights[j] == limit:
    #             result = (i, j) if i > j else (j, i)
    #             return result

    # return None

    if len(weights) == 2 and weights[0] + weights[1] == limit:
        return (1, 0)
    for i in range(len(weights) - 1):
        hash_table_insert(ht, weights[i], i)

    for i in range(len(weights) - 1):
        key = hash_table_retrieve(ht, limit-weights[i])
        if key:
            val_1 = i
            val_2 = weights.index(limit - weights[i])
            result = (val_1, val_2) if val_1 > val_2 else (val_2, val_1)
            return result


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
