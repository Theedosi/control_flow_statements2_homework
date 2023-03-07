def main(n):
    """
    Find the index of the largest digit of the five-digit number.
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
    s = 5
    max = a5
   
    if a4>max:
        max=a4
        s = 4
    if a3>max:
        max=a3
        s=3
    if a2>max:
        max=a2
        s=2
    if a1>max:
        max=a1
        s=1
    return s
print(main(46517))
