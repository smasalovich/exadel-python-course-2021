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

    if isinstance(test, dict):
        for value in test.values():
                if isinstance(value, dict):
                    list_count(value)
                else:
                    result.extend(value)
        return (result)
    elif isinstance(test, list):
        return (test)

print(list_count(tree))
print(list_count([1,2,3]))

assert list_count([1,2,3]) == [1,2,3], "incorrect list count"
