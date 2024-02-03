def caesarCipher(s, k):
    result = []
    for i in s:
        if i.isascii and i.isalpha():
            text = i
            i = i.lower()
            rotated = ord(i) + k
            sw_text = chr((rotated - ord('a')) % 26 + ord('a'))
            if text.isupper():
                result.append(sw_text.upper())
            else:
                result.append(sw_text)
        else:
            result.append(i)
            
    return ''.join(result)