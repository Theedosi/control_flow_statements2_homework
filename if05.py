def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a1=n%10
    n = n//10
    a2= n%10
    n = n//10
    a3= n%10
    n = n//10
    a4= n%10
    a5= n/10
    
    max = a5
    if a4>max:
        max=a4
    if a3>max:
        max=a3
    if a2>max:
        max=a2
    if a1>max:
        max=a1
    return max
print(main(12345))
