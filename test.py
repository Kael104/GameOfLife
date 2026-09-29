from main import next_board_state, state, render_board

# TODO: there's a lot of repeated code here. Can
# you move some of into reusable functions to
# make it shorter and neater?

if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = state(3,3,[
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ])
    expected_next_state1 = state(3,3,[
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ])
    actual_next_state1 = next_board_state(init_state1)

    if expected_next_state1 == actual_next_state1:
        print ("PASSED 1")
    else:
        print ("FAILED 1!")
        print ("Expected:")
        render_board (expected_next_state1)
        print ("Actual:")
        render_board (actual_next_state1)

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = state(3,3,[
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ])
    expected_next_state2 = state(3,3,[
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ])
    actual_next_state2 = next_board_state(init_state2)

    if expected_next_state2 == actual_next_state2:
        print ("PASSED 2")
    else:
        print ("FAILED 2!")
        print ("Expected:")
        render_board (expected_next_state2)
        print ("Actual:")
        render_board (actual_next_state2)