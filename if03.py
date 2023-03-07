def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    max = a
    if b>max:
        max = b
    if c>max:
        max = c
    min = a
    if b<min:
        min = b
    if c<min :
        min = c
    return (a+b+c)-(min+max)
    
print(main(2,3,4))