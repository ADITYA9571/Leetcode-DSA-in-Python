or i, ch in enumerate(pattern):
            if ch in dict1 and dict1[ch] != list1[i]:
                return False
            else:
                dict1[ch] = list1[i]
        dict1 = {}
        for i, ch in enumerate(list1):
            if ch in dict1 and dict1[ch] != pattern[i]:
                return False
            else:
                dict1[ch] = pattern[i]
        return True 