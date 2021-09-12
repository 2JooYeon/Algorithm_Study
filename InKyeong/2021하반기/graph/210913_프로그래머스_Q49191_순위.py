def solution(n, results):
    win, lose = {}, {}
    for i in range(1, n + 1):
        win[i], lose[i] = set(), set()

    for i in range(1, n + 1):
        for a, b in results:
            if a == i:
                win[i].add(b)
            if b == i:
                lose[i].add(a)

        # i를 이긴 사람(lose[i]) -> i에게 진 사람(win[i])을 이김
        for winner in lose[i]:
            win[winner].update(win[i])
        # i에게 진 사람(win[i]) -> i에게 이긴 사람(lose[i])에게 짐
        for loser in win[i]:
            lose[loser].update(lose[i])

    answer = 0
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer