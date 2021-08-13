def dec2bin(decimal, result):

    if decimal==0:
        return result

    result = str(decimal%2) + result
    return dec2bin(decimal//2, result)

decimal = int(input())
result = ""

print(dec2bin(decimal, result))
