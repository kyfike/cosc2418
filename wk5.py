## Ky Fike, 24 Sept 2022
## 
import string
fhand = open('swift_noRhyme.txt')
line_num = 0
d, d_lines = dict(), dict()
lines_list, longest = [], []
for line in fhand:
    line_num += 1
    line = line.translate(line.maketrans('', '', string.punctuation)) # Do I need the hyphen back? ... No.
    line = line.strip()
    line = line.lower()
    words = line.split()
    for item in words:
        w = item
        # print(item)
        if len(w) > 4:
            if (len(w), w) not in d:   # initialize item
                d[len(w),w] = 1
                d_lines[w] = ('line(s) ' + str(line_num))
                if len(w) > 11:
                    longest.append(w)
            else:
                d[len(w),w] += 1
                d_lines[w] += ', ' + str(line_num)
# print(d)
longest.sort(key=len, reverse=True)
# print(longest)

print('{0:<8} {1:<20} {2:<11} {3:<25}'.format('\nlength', ' word', ' frequency', ' lines\n'))
for item in longest:
    args = [len(item), item, d[len(item), item], d_lines[item]]
    print('{0:<8} {1:<20} {2:<11} {3:<25}'.format(*args))       # amazing formatting @ref: https://stackoverflow.com/questions/19103052/string-formatting-columns-in-line