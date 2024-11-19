'''
1 - give an integer number;

2 - know if number is multiple of 3 and 5;
    Bacon with eggs

3 - know if number isnt multiple of 3 and 5;
    Poor

4 - know if number is only multiple of 3;
    Bacon

5 - know if number is only multiple of 5;
    Ovos



'''


def bacon_with_eggs(n):
    assert isinstance(n, (int, float)), 'the number wants to be a integer'

    if n % 3 == 0 and n % 5 == 0:
        return 'BACON WITH EGGS'

    if n % 3 == 0:
        return 'BACON'

    if n % 5 == 0:
        return 'EGGS'
    return 'POOR'
