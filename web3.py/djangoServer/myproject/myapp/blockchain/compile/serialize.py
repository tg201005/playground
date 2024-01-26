def makePlayer(name, score):
    return {"name": name, "score": score}


def addGameLog(winner, loser, order, tournament):
    tournament.append({"game_id": order, "winner": winner, "loser": loser})


tournament = []
addGameLog(makePlayer("a", 1), makePlayer("b", 2), 1, tournament)
addGameLog(makePlayer("c", 3), makePlayer("d", 4), 2, tournament)
addGameLog(makePlayer("e", 5), makePlayer("f", 6), 3, tournament)

# print(tournament)
