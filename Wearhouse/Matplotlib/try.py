def solution(n):
    # TODO convert int to roman string
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
    
    n.insert(0, "(")
    n.insert(4, ") ")
    n.insert(8, "-")

    return ''.join(map(str, n))

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # => returns "(123) 456-7890")