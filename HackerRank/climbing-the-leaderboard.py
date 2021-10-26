def solution(ranked, player):
    answer = list()
    ranked = sorted(list(set(ranked)), reverse=True)
    len_ranked = len(ranked)
    initial_ranking = {score: idx + 1 for idx, score in enumerate(ranked)}

    ranked.reverse()
    ranking_idx = 0
    for score in player:
        while ranking_idx < len_ranked and score > ranked[ranking_idx]:
            ranking_idx += 1

        if ranking_idx == len_ranked:
            answer.append(1)
            continue

        if score != ranked[ranking_idx]:
            answer.append(initial_ranking[ranked[ranking_idx]] + 1)
        else:
            answer.append(initial_ranking[ranked[ranking_idx]])

    return answer


if __name__ == "__main__":
    n = int(input())
    ranked = list(map(int, input().split()))
    m = int(input())
    player = list(map(int, input().split()))

    result = solution(ranked, player)
    for value in result:
        print(value)