
def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print("move disk from", fp, "to", tp)

if __name__ == '__main__':
    height = 3
    moveTower(3, "A", "B", "C")