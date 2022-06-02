def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    chars = list(s)
    index = []
    vowels = []
    for i in range(len(chars)):
        if chars[i] in ['a','e','i','o','u','A','E','I','O','U']:
            vowels.append(chars[i])
            index.append(i)
            vowels = vowels[::-1]
            final = []
            ind = 0
    for i in range(len(chars)):
        if i in index:
            final.append(vowels[ind])
            ind += 1
        else:
            final.append(chars[i])
    str1 = ""
    return str1