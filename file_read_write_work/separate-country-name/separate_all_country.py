# Country File read and all counntry name separate alphabatic used append mode.

import requests

with open("country.txt", "r") as f:
    lines = f.readlines()
    print(lines)

    for line in lines:
        print(line[0], line)
        if line[0] == "A":
            with open("a.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "B":
            with open("b.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "C":
            with open("c.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "D":
            with open("d.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "E":
            with open("e.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "F":
            with open("f.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "G":
            with open("g.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "H":
            with open("h.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "I":
            with open("i.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "J":
            with open("j.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "K":
            with open("k.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "L":
            with open("l.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "M":
            with open("m.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "N":
            with open("n.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "O":
            with open("o.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "P":
            with open("p.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "Q":
            with open("q.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "R":
            with open("r.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "S":
            with open("s.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "T":
            with open("t.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "U":
            with open("u.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "V":
            with open("v.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "W":
            with open("w.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "X":
            with open("x.txt", "a") as fp:
                fp.write(line)
        elif line[0] == "Y":
            with open("y.txt", "a") as fp:
                fp.write(line)
        else:
            with open("z.txt", "a") as fp:
                fp.write(line)