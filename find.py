def find(text, word):
    n = len(text)
    m = len(word)
    for i in range(0, n-m+1):
        if text[i:i+m] == word:
            return i
    return -1 #if we got here, word does not appear
              #as a subtext of text




def find2(text, word):
    n = len(text)
    m = len(word)
    for i in range(0, n-m+1):
        cnt = 0
        for j in range(i, i+m):
            if text[j] == word[j-i]:
                cnt = cnt+1
        if cnt == m:
            return i
    return -1 #if we got here, word does not appear
              #as a subtext of text


def find3(text, word):
    n = len(text)
    m = len(word)
    #for i in range(0, n-m+1):
    i = 0
    while i<=n-m:
        if text[i:i+m] == word:
            return i
        i = i+1
    return -1 #if we got here, word does not appear
              #as a subtext of text






