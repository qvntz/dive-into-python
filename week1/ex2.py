import sys
steps = int(sys.argv[1])
for i in range(steps):
    print(" " * (steps - i - 1), "#" * (i + 1), sep="")