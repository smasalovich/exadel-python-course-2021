tree = {
   "node1": {
       "node11": {
           "node111": [1, 2, 3],
           "node112": [31, 5]
       },
       "node12": [31]
   },
   "node2": [7, 8, 9]
}

def list_count(test, result=[]):

    assert (isinstance(test, dict) or isinstance(test, list)), "incorrect input"

    if isinstance(test, dict):
        for value in test.values():
                if isinstance(value, dict):
                    list_count(value)
                else:
                    assert isinstance(value, list), "incorrect input"
                    result.extend(value)
                    # return (value)
        return (result)
    elif isinstance(test, list):
        return (test)

print(list_count(tree))
print(list_count([1,2,3]))

print(list_count(5))
