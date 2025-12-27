rule = input()

passwords = [input() for _ in range(2)]

def check(last, word, rule):
    if len(word) == 0 and len(rule) == 0:
        return True
    if len(word) == 0 or len(rule) == 0: return False
    l = word.pop(0)
    r = rule[0]
    ans = False
    if r == "x":
        ans = ans or check(l, word, rule[1:])
    elif r == "u":
        if int(l) > int(last):
            ans = ans or check(l, word, rule[1:])
        else: return False
    elif r == "d":
        if int(l) < int(last):
            ans = ans or check(l, word, rule[1:])
        else: return False
    else:
        pass
    return ans

allRules = [rule]
if "?" in rule or "*" in rule:
    allRules = set()
    # replace rules so they don't have special characters
    pending = [("", rule)]
    while len(pending) > 0:
        item, r = pending.pop(0)
        if len(r) == 0:
            allRules.add(item)
        else:
            if r[0] in ["x", "d", "u"]:
                pending.append((item + r[0], r[1:]))
            elif r[0] == "?":
                pending.append((item[:-1], r[1:]))
                pending.append((item, r[1:]))
            elif r[0] == "*":
                # up to length 12
                w = str(item)
                pending.append((item[:-1], r[1:]))
                while len(w) < 12:
                    pending.append((w, r[1:]))
                    w += w[-1]
            elif r[0] == "(":
                extra = ""
                e = "*"
                c = 0
                while r[c] != ")":
                    c += 1
                    extra += r[c]
                c += 2
                e = r[c-1]
                extra = extra.replace(")", "")
                # up to length twelve
                if e == "?":
                    pending.append((item, r[c:]))
                    pending.append((item + extra, r[c:]))
                elif e == "*":
                    w = str(item)
                    while len(w) < 12:
                        pending.append((w, r[c:]))
                        w += extra

def bigCheck(word):
    ans = False
    q = "".join(word)
    for item in allRules:
#        print(word, item)
        ans = ans or check(0, list(q), item)
    return ans

for word in passwords:
    a = "Yes" if bigCheck(list(word)) else "No"
    print(a)
