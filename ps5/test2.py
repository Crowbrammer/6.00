def addVectors(v1, v2):

    if len(v1) > 0 and len(v2) > 0:
        return [v1[0] + v2[0]] + addVectors(v1[1:], v2[1:])
    # No more on either (on next round)
    elif len(v1) <= 0 and len(v2) <= 0:
        return []
    # No more on v1
    elif len(v1) <= 0 or len(v2) <= 0:
        if len(v1) > 0 and len(v2) <= 0:
            return [v1[0]] + addVectors(v1[1:], v2)
        elif len(v1) <= 0 and len(v2) > 0:
            return [v2[0]] + addVectors(v1, v2[1:])
        else:
            return []
    # No more on v2

    # if len(v1) <= 0 or len(v2) <= 0:
    #     try:
    #         print("vT on try:", vT)
    #         vT.append(v1[0])
    #         return vT
    #     except IndexError:
    #         try:
    #             if v1[0] != 0:
    #                 vT.append(v2[0])
    #             return vT
    #         except IndexError:
    #             return "Everything's all fucked up."
    else:
        sub_VT = v1[0] + v2[0]
        vT.append(sub_VT)
        return vT.append(addVectors(v1[1:],v2[1:]))

print("\nHYPOTHESES:\n")
print("...")

print("\nEXPERIMENT RESULTS:\n")
print(addVectors([1, 2, 3, 12, 13, 14], [4, 5, 6, 7]))
