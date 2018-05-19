
# Create tests to check the correctness of your code
from poc_mancala_template import SolitaireMancala

WINNABLE_BOARDS = [[0, 0, 0, 0, 2, 4, 6],
                   [0, 0, 0, 2, 4, 0, 0],
                   [0, 0, 1, 1, 3, 5, 0],
                   [0, 0, 1, 3, 0, 0, 0],
                   [0, 0, 1, 3, 2, 4, 6],
                   [0, 0, 2, 0, 0, 0, 0],
                   [0, 0, 2, 0, 2, 4, 6],
                   [0, 0, 2, 2, 4, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 2, 4, 6],
                   [0, 1, 0, 2, 4, 0, 0],
                   [0, 1, 1, 1, 3, 5, 0],
                   [0, 1, 1, 3, 0, 0, 0],
                   [0, 1, 1, 3, 2, 4, 6],
                   [0, 1, 2, 0, 0, 0, 0],
                   [0, 1, 2, 0, 2, 4, 6],
                   [0, 1, 2, 2, 4, 0, 0]]

test_config = WINNABLE_BOARDS[11]


def test_init():
    my_game = SolitaireMancala()
    print("Testing init - Computed:", my_game, "Expected: [0]")
    assert (my_game.board.__eq__(list().append(0)))


def test_str():
    my_game = SolitaireMancala()
    # test_config = [0, 0, 1, 1, 3, 5, 0]
    my_game.set_board(test_config)

    print("Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0]))
    assert (str(my_game) == str([0, 5, 3, 1, 1, 1, 0]))


def test_set_board():
    my_game = SolitaireMancala()
    # test_config = [0, 0, 1, 1, 3, 5, 0]
    my_game.set_board(test_config)
    print("Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 1, 0]))
    assert (my_game.board.__eq__(test_config))


def test_get_num_seeds():
    my_game = SolitaireMancala()
    # test_config = [0, 0, 1, 1, 3, 5, 0]
    my_game.set_board(test_config)
    print("Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", test_config[1])
    assert (my_game.get_num_seeds(1).__eq__(test_config[1]))
    print("Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", test_config[3])
    assert (my_game.get_num_seeds(3).__eq__(test_config[3]))
    print("Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", test_config[5])
    assert (my_game.get_num_seeds(5).__eq__(test_config[5]))


def test_is_legal_move():
    print()
    my_game = SolitaireMancala()
    # test_config = [0, 0, 1, 1, 3, 5, 0]
    my_game.set_board(test_config)
    assert (my_game.is_legal_move(0) == False)
    assert (my_game.is_legal_move(5) == True)

def test_set_board():
    print("Test mutation: Board should not be able")
    my_game = SolitaireMancala()
    # test_config = [0, 0, 1, 1, 3, 5, 0]
    conf = [0, 0, 1, 1, 3, 5, 0]
    my_game.set_board(conf)
    conf.append(13)
    assert (my_game.board != conf)


def test_plan_moves():
    """
    Test code for Solitaire Mancala
    """
    my_game = SolitaireMancala()
    # test_config = [0, 0, 1, 1, 3, 5, 0]
    my_game.set_board(test_config)

    print("Testing perfect move sequence: ", my_game.plan_moves())
    perfect_moves = [1, 5, 1, 2, 1, 4, 1, 3, 1, 2, 1]
    assert(len(perfect_moves) == len(my_game.plan_moves()))
