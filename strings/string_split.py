def split_string(s, c):
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
