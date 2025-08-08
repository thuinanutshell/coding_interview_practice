def split_string(s, c):
    """Method to split a string s at each occurrence of c

    1. If the string is empty then just return an empty array
    2. Create an empty list to hold separated strings (new_string)
    3. Create an empty string to build up each individual string (st)
    4. Loop through each character in the input string s
    5. If the character is not equal to character c, add that to st until we reaches the first occurrence of c
    6. Then, append st to the array and reset it to be empty to build up the next individual string
    7. After the loop, add the remaining st to the list of strings

    Args:
        s (string): The input string
        c (string): A character c

    Returns:
       list: a list of strings
    """
    if not s:
        return []

    new_string = []
    st = ""

    for i in range(len(s)):
        if s[i] != c:
            st += s[i]
        elif s[i] == c:
            new_string.append(st)
            st = ""

    new_string.append(st)

    return new_string
