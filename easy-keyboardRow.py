words = ["Hello","Alaska","Dad","Peace"]
def findWords(self, words: List[str]) -> List[str]:
    a,b,c,z = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm'), []

    for i in words:
        f=i.lower()
        if set(f).issubset(b) or set(f).issubset(a) or set(f).issubset(c):
            z.append(i)
    return z