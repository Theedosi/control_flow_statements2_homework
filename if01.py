def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    mx = a
    if b>mx:
        mx = b
    if c>mx:
        mx = c
    return mx
print(main(1,2,3))