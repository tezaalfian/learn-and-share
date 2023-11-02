import sys
while True:
    jack_cds, jill_cds = map(int, sys.stdin.readline().split())
    if jack_cds == 0 and jill_cds == 0:
        break

    jack_catalog = set()

    for _ in range(jack_cds):
        jack_catalog.add(int(sys.stdin.readline()))

    common_cds = 0
    for _ in range(jill_cds):
        m = int(int(sys.stdin.readline()))
        if m in jack_catalog :
            common_cds += 1

    print(common_cds)