def digitCount(self, num: str) -> bool:
    count = 0
    for i in num:
        if (num[count] != str(num.count(str(count)))):
            return False
        count += 1
    return True
