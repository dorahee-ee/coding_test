def solution(players, callings):
    player_dict = {player:idx for idx, player in enumerate(players)}

    for calling in callings:
        index = player_dict[calling]
        players[index], players[index-1] = players[index-1], players[index]

        player_dict[players[index]] = index
        player_dict[players[index-1]] = index -1

    return players


'''
dictionary를 사요하면 각 호출마다 시간 복잡도가 O(1)이 되기 때뭉네 훨씬 효육적으로 해결된다.
즉, calling 선수의 index를 리스트 연산의 .index()가 아닌 딕셔너리에서 선수의 등수를 가지고오면 해결이된다.
'''