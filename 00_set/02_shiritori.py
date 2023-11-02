def shiritori() :
    n = int(input())
    word = set()
    prev = None

    for i in range(n):
        w = input()
        if prev is not None:
            if prev[-1] != w[0] :
                print(f"Player {i % 2 + 1} lost")
                return
        
        if w in word :
            print(f"Player {i % 2 + 1} lost")
            return
        word.add(w)
        prev = w
    print("Fair Game")

shiritori()