def divide(dividend,divisor):
    count = 0
    temp1 = dividend
    temp2 = divisor
    while abs(dividend) >= abs(divisor):
        dividend = abs(dividend) - abs(divisor)
        count += 1

    if (temp1 < 0 or temp2 < 0):
        return -count
    return count

print(divide(1,1))
