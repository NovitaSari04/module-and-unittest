def function(lower_limit, upper_limit, operation):

    if operation == "plus1":
        result = []
        for i in range(lower_limit-1, upper_limit):
            i = i+1
            result.append(i)
        return result
    
    elif operation == "fibonaci":
        result = [lower_limit, lower_limit+1]
        for i in range (2, upper_limit):
            result.append(result[i-1] + result[i-2])
            if result[-1] == upper_limit:
                break
            elif result[-1] > upper_limit:
                result.pop()
                break
        return result

    elif operation == "kuadrat":
        result = []
        for i in range (1, upper_limit):
            formula = lower_limit**i
            result.append(formula)
            if formula > upper_limit:
                result.pop()
                break
            elif formula == upper_limit:
                break
        return result





