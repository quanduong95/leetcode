def rotateString(self, s: str, goal: str) -> bool:
    s = list(s)
    goal = list(goal)
    for i in s:
        s.append(s[0])
        s.pop(0)
        if(s == goal):
            return True
