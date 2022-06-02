def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1=str(num1)
    num2 = str(num2)
    frequency1 = {}
    frequency2 = {}
    for num in num1:
        frequency1[num]=num1.count(num)
    for num in num2:
        frequency2[num]=num2.count(num)
    if frequency1==frequency2:
        return True
    else: return False

