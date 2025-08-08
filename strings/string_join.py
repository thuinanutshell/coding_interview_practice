def join_string(arr, s):
    if arr == []:
        return ""

    final_string = ""
    for st in arr:
        if st != "":
            final_string += st
        if st != arr[-1]:
            final_string += s
    return final_string
