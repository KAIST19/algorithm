import sys
input = sys.stdin.readline


s = input().strip()
okay = False

for letter in s[1:]:
    if letter.islower():
        okay = True
        break

if okay:
    print(s)
else:
    print(s.swapcase())