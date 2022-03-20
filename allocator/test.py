import hw3

def test_bb(expected, allocator):
    if len(expected) != len(allocator.bb):
        print("Basic Blocks Failed", list(map(lambda b: b[1], allocator.bb)), "\n                   ",  expected)
        return
    for index, bb in enumerate(allocator.bb):
        if bb[1] != expected[index]:
            print("Basic Blocks Failed", list(map(lambda b: b[1], allocator.bb)), "\n                   ",  expected)
            return

def test_cfg(expected, allocator):
    expected.sort()
    allocator.cfg.sort()
    if len(expected) != len(allocator.cfg):
        print("CFG Failed", allocator.cfg, "\n          ", expected)
        return
    for index, edge in enumerate(allocator.cfg):
        if edge != expected[index]:
            print("CFG Failed", allocator.cfg, "\n          ", expected)
            return

def test_defs(expected, allocator):
    if len(expected) != len(allocator.defs):
        print("Defs Failed", list(map(lambda b: b[1], allocator.defs)), "\n           ", expected)
        return
    for index, d in enumerate(allocator.defs):
        if d[1] != expected[index]:
            print("Defs Failed", list(map(lambda b: b[1], allocator.defs)), "\n           ", expected)
            return

def test_uses(expected, allocator):
    if len(expected) != len(allocator.uses):
        print("Uses Failed", list(map(lambda b: b[1], allocator.uses)), "\n           ", expected)
        return
    for index, uses in enumerate(allocator.uses):
        a = uses[1].copy()
        b = expected[index].copy()
        a.sort()
        b.sort()
        if a != b:
            print("Uses Failed", list(map(lambda b: b[1], allocator.uses)), "\n           ", expected)
            return

def test_livein(expected, allocator):
    if len(expected) != len(allocator.live_in):
        print("Live In Failed", list(map(lambda b: b[1], allocator.live_in)), "\n             ", expected)
        return
    for index, live in enumerate(allocator.live_in):
        a = live[1].copy()
        b = expected[index].copy()
        a.sort()
        b.sort()
        if a != b:
            print("Live In Failed", list(map(lambda b: b[1], allocator.live_in)), "\n              ", expected)
            return

def test_liveout(expected, allocator):
    if len(expected) != len(allocator.live_out):
        print("Live Out Failed", list(map(lambda b: b[1], allocator.live_out)), "\n              ",  expected)
        return
    for index, live in enumerate(allocator.live_out):
            a = live[1].copy()
            b = expected[index].copy()
            a.sort()
            b.sort()
            if a != b:
                print("Live Out Failed", list(map(lambda b: b[1], allocator.live_out)), "\n              ",  expected)
                return

def test_web(expected, allocator):
    if len(expected) != len(allocator.webs):
        print("Web Failed", allocator.webs, "\n          ",  expected)
        return
    for index, web_key in enumerate(allocator.webs):
        a = allocator.webs[web_key].copy()
        b = expected[web_key].copy()
        a.sort()
        b.sort()
        if a != b:
            print("Web Failed", allocator.webs, "\n          ",  expected)
            return

def test_ig(expected, allocator):
    if len(expected) != len(allocator.ig):
        print("IG Failed", allocator.ig, "\n         ",  expected)
        return
    for index, edge in enumerate(allocator.ig):
        if edge != expected[index]:
            print("IG Failed", allocator.ig, "\n         ",  expected)
            return

def test_colored_graph(expected, allocator):
    if len(expected) != len(allocator.coloring):
        print("Coloring Failed", allocator.coloring, "\n               ",  expected)
        return
    for index, color in enumerate(allocator.coloring):
        if allocator.coloring[color] != expected[color]:
            print("Coloring Failed", allocator.coloring, "\n               ",  expected)
            return

# Simple sanity check. if this is failing, fix it first.
def test_three_variables():
    ir = [
        "Main:",
        "assign, x, 10.0,",
        "assign, y, x,",
        "assign, z, 12.0,",
        "add, w, x, y,",
        "add, w, z, y,",
        "goto, End, ,",
        "End:",
        "return, , ,"
        ]

    allocator = hw3.Allocator(ir)
    allocator.apply_functions()

    expected_block_numbers = ["None", "1", "1", "1", "1", "1", "1", "None", "2"]
    test_bb(expected_block_numbers, allocator)

    expected_cfg = ["1 -> 2"]
    test_cfg(expected_cfg, allocator)

    expected_defs = ['', 'x', 'y', 'z', '', '', '', '', '']
    test_defs(expected_defs, allocator)

    expected_uses = [[],[],['x'],[],['x', 'y'], ['z','y'],[],[],[]]
    test_uses(expected_uses, allocator)

    expected_live_in = [[], [], ['x'], ['x', 'y'], ['x', 'y', 'z'], ['y', 'z'], [], [], []]
    test_livein(expected_live_in, allocator)
    
    expected_live_out = [[], ['x'], ['x', 'y'], ['x', 'y', 'z'], ['y', 'z'], [], [], [], []] 
    test_liveout(expected_live_out, allocator)
    
    expected_web = {'x1': ['1', '2', '3', '4'], 'y1': ['2', '3', '4', '5'], 'z1': ['3', '4', '5']}
    test_web(expected_web, allocator)

    expected_ig = ['x1 -- y1', 'x1 -- z1', 'y1 -- z1']
    test_ig(expected_ig, allocator)

    expected_colors = {'z1': '3', 'y1': '2', 'x1': '1'}
    test_colored_graph(expected_colors, allocator)

# Simple sanity check. if this is failing, fix it first.
def only_fallthrough_usage():
    ir = [
        "Main:",
        "assign, x, 10.0,",
        "brgt, x, 10.0, Jump,",
        "add, w, x, 10.0,",
        "return, , ,",
        "Jump:",
        "return, , ,"
        ]

    allocator = hw3.Allocator(ir)
    allocator.apply_functions()

    expected_block_numbers = ['None', '1', '1', '2', '2', 'None', '3'] 
    test_bb(expected_block_numbers, allocator)

    expected_cfg = ['1 -> 2', '1 -> 3'] 
    test_cfg(expected_cfg, allocator)

    expected_defs = ['', 'x', '', '', '', '', ''] 
    test_defs(expected_defs, allocator)

    expected_uses = [[], [], ['x'], ['x'], [], [], []] 
    test_uses(expected_uses, allocator)

    expected_live_in = [[], [], ['x'], ['x'], [], [], []] 
    test_livein(expected_live_in, allocator)
    
    expected_live_out = [[], ['x'], ['x'], [], [], [], []]
    test_liveout(expected_live_out, allocator)
    
    expected_web = {'x1': ['1', '2', '3']}
    test_web(expected_web, allocator)

    expected_ig = []
    test_ig(expected_ig, allocator)

    expected_colors = {'x1': '1'}
    test_colored_graph(expected_colors, allocator)

def only_branch_usage():
    ir = [
        "Main:",
        "assign, x, 10.0,",
        "brgt, x, 10.0, Jump,",
        "return, , ,",
        "Jump:",
        "add, w, x, 10.0,",
        "return, , ,"
        ]

    allocator = hw3.Allocator(ir)
    allocator.apply_functions()

    expected_block_numbers = ['None', '1', '1', '2', 'None', '3', '3']
    test_bb(expected_block_numbers, allocator)

    expected_cfg = ['1 -> 2', '1 -> 3'] 
    test_cfg(expected_cfg, allocator)

    expected_defs = ['', 'x', '', '', '', '', '']
    test_defs(expected_defs, allocator)

    expected_uses = [[], [], ['x'], [], [], ['x'], []]
    test_uses(expected_uses, allocator)

    expected_live_in = [[], [], ['x'], [], [], ['x'], []]
    test_livein(expected_live_in, allocator)
    
    expected_live_out = [[], ['x'], ['x'], [], [], [], []] 
    test_liveout(expected_live_out, allocator)
    
    expected_web = {'x1': ['1', '2', '5']} 
    test_web(expected_web, allocator)

    expected_ig = []
    test_ig(expected_ig, allocator)

    expected_colors = {'x1': '1'}
    test_colored_graph(expected_colors, allocator)


# Diamond shaped graph where all uses for the top node are in the bottom node.
def test_unused_diamond_sides():
    ir = [
        "Main:",
        "assign, x, 10.0,",
        "assign, y, x,",
        "assign, z, 12.0,",
        "brgt, x, y, Left,",
        "assign, w, 13.0,", # Right
        "assign, w, 13.0,",
        "goto, End, ,",
        "Left:",
        "assign, w, 13.0,", # Left
        "assign, w, 13.0,",
        "goto, End, ,",
        "End:",
        "add, v, z, z,",
        "add, v, y, y,",
        "add, v, x, x,",
        "return, , ,"
        ]

    allocator = hw3.Allocator(ir)
    allocator.apply_functions()

    expected_block_numbers = ['None', '1', '1', '1', '1', '2', '2', '2', 'None', '3', '3', '3', 'None', '4', '4', '4', '4']
    test_bb(expected_block_numbers, allocator)

    expected_cfg = ['1 -> 3', '1 -> 2', '2 -> 4', '3 -> 4']
    test_cfg(expected_cfg, allocator)

    expected_defs = ['', 'x', 'y', 'z', '', '', '', '', '', '', '', '', '', '', '', '', '']
    test_defs(expected_defs, allocator)

    expected_uses = [[], [], ['x'], [], ['x', 'y'], [], [], [], [], [], [], [], [], ['z'], ['y'], ['x'], []]
    test_uses(expected_uses, allocator)

    expected_live_in = [[], [], ['x'], ['x', 'y'], ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'], [], ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'], [], ['x', 'y', 'z'], ['x', 'y'], ['x'], []]
    test_livein(expected_live_in, allocator)
    
    expected_live_out = [[], ['x'], ['x', 'y'], ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'], [], ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'], [], ['x', 'y'], ['x'], [], []]
    test_liveout(expected_live_out, allocator)
    
    expected_web = {'x1': ['1', '2', '3', '4', '9', '10', '11', '13', '14', '15'], 'y1': ['2', '3', '4', '9', '10', '11', '13', '14'], 'z1': ['3', '4', '9', '10', '11', '13']}
    test_web(expected_web, allocator)

    expected_ig = ['x1 -- y1', 'x1 -- z1', 'y1 -- z1']
    test_ig(expected_ig, allocator)
    
    expected_colors = {'x1': '1', 'y1': '2', 'z1': '3'} 
    test_colored_graph(expected_colors, allocator)

# two unconnected legs of graph
# X is defined at the top node and used on the left side
# The right defines Y and uses it in the bottom node.
def non_overlapping_left_and_right():
    ir = [
        "Main:",
        "assign, x, 10.0,",
        "brgt, x, 10.0, Left,",
        "assign, x, 13.0,", # Right
        "goto, End, ,",
        "Left:",
        "add, x, x, 13.0,", # Left
        "return, , ,",
        "End:",
        "add, x, x, x,",
        "return, , ,"
        ]

    allocator = hw3.Allocator(ir)
    allocator.apply_functions()

    expected_block_numbers = ['None', '1', '1', '2', '2', 'None', '3', '3', 'None', '4', '4'] 
    test_bb(expected_block_numbers, allocator)

    expected_cfg = ['1 -> 2', '1 -> 3', '2 -> 4'] 
    test_cfg(expected_cfg, allocator)

    expected_defs = ['', 'x', '', 'x', '', '', 'x', '', '', 'x', '']
    test_defs(expected_defs, allocator)

    expected_uses = [[], [], ['x'], [], [], [], ['x'], [], [], ['x'], []] 
    test_uses(expected_uses, allocator)

    expected_live_in = [[], [], ['x'], [], ['x'], [], ['x'], [], [], ['x'], []] 
    test_livein(expected_live_in, allocator)
    
    expected_live_out = [[], ['x'], ['x'], ['x'], ['x'], [], [], [], [], [], []] 
    test_liveout(expected_live_out, allocator)
    
    expected_web = {'x1': ['1', '2', '6'], 'x2': ['3', '4', '9']}
    test_web(expected_web, allocator)

    expected_ig = []
    test_ig(expected_ig, allocator)

    expected_colors = {'x1': '1', 'x2': '1'} 
    test_colored_graph(expected_colors, allocator)

# test that a loop will keep a use alive through the end of the block
# even if the block after it does not use it.
def loop_extra_liveness():
    ir = [
        "Main:",
        "assign, x, 10.0,",
        "assign, w, 3.0,",
        "Loop:",
        "assign, p, 2.0,",
        "assign, p, 2.0,",
        "add, w, w, x,",
        "assign, p, 2.0,", 
        "assign, p, 2.0,", 
        "brgeq, w, 100.0, Loop,", 
        "return, , ,"
        ]

    allocator = hw3.Allocator(ir)
    allocator.apply_functions()

    expected_block_numbers = ['None', '1', '1', 'None', '2', '2', '2', '2', '2', '2', '3']  
    test_bb(expected_block_numbers, allocator)

    expected_cfg = ['1 -> 2', '2 -> 2', '2 -> 3']
    test_cfg(expected_cfg, allocator)

    expected_defs = ['', 'x', 'w', '', '', '', 'w', '', '', '', '']
    test_defs(expected_defs, allocator)

    expected_uses = [[], [], [], [], [], [], ['w', 'x'], [], [], ['w'], []] 
    test_uses(expected_uses, allocator)

    expected_live_in = [[], [], ['x'], [], ['w', 'x'], ['w', 'x'], ['w', 'x'], ['w', 'x'], ['w', 'x'], ['w', 'x'], []]
    test_livein(expected_live_in, allocator)
    
    expected_live_out = [[], ['x'], ['w', 'x'], [], ['w', 'x'], ['w', 'x'], ['w', 'x'], ['w', 'x'], ['w', 'x'], ['w', 'x'], []]
    test_liveout(expected_live_out, allocator)
    
    expected_web = {'x1': ['1', '2', '4', '5', '6'], 'w1': ['2', '4', '5', '6', '7', '8', '9']} 
    test_web(expected_web, allocator)

    expected_ig = ['w1 -- x1']
    test_ig(expected_ig, allocator)

    expected_colors = {'x1': '2', 'w1': '1'} 
    test_colored_graph(expected_colors, allocator)


# make sure that unreachable uses act the same as not having them int he program.
# X is defined at the top node and used on the left side
# The right defines Y and uses it in the bottom node.
def unreachable_uses():
    ir = [
        "Main:",
        "assign, x, 10.0,",
        "assign, y, 10.0,",
        "assign, z, 10.0,",
        "goto, End, ,",
        "NeverHit:",
        "add, p, y, x,",
        "add, p, z, x,",
        "return, , ,",
        "End:",
        "add, p, x, x,",
        "return, , ,"
        ]

    allocator = hw3.Allocator(ir)
    allocator.apply_functions()

    expected_block_numbers = ['None', '1', '1', '1', '1', 'None', '2', '2', '2', 'None', '3', '3']  
    test_bb(expected_block_numbers, allocator)

    expected_cfg = ['1 -> 3'] 
    test_cfg(expected_cfg, allocator)

    expected_defs = ['', 'x', '', '', '', '', '', '', '', '', '', '']
    test_defs(expected_defs, allocator)

    expected_uses = [[], [], [], [], [], [], [], [], [], [], ['x'], []]
    test_uses(expected_uses, allocator)

    expected_live_in = [[], [], ['x'], ['x'], ['x'], [], [], [], [], [], ['x'], []] 
    test_livein(expected_live_in, allocator)
    
    expected_live_out = [[], ['x'], ['x'], ['x'], ['x'], [], [], [], [], [], [], []]
    test_liveout(expected_live_out, allocator)
    
    expected_web = {'x1': ['1', '2', '3', '4', '10']} 
    test_web(expected_web, allocator)

    expected_ig = []
    test_ig(expected_ig, allocator)

    expected_colors = {'x1': '1'} 
    test_colored_graph(expected_colors, allocator)

# jump and fallthrough are the same
def jump_fallthrough_match():
    ir = [
        "Main:",
        "assign, x, 10.0,",
        "goto, Loop, ,",
        "Loop:",
        "add, x, x, 1,",
        "brgeq, x, 100.0, Loop,", 
        "return, , ,"
        ]

    allocator = hw3.Allocator(ir)
    allocator.apply_functions()

    expected_block_numbers = ['None', '1', '1', 'None', '2', '2', '3'] 
    test_bb(expected_block_numbers, allocator)

    expected_cfg = ['1 -> 2', '2 -> 2', '2 -> 3']
    test_cfg(expected_cfg, allocator)

    expected_defs = ['', 'x', '', '', 'x', '', ''] 
    test_defs(expected_defs, allocator)

    expected_uses = [[], [], [], [], ['x'], ['x'], []] 
    test_uses(expected_uses, allocator)

    expected_live_in = [[], [], ['x'], [], ['x'], ['x'], []] 
    test_livein(expected_live_in, allocator)
    
    expected_live_out = [[], ['x'], ['x'], [], ['x'], ['x'], []]
    test_liveout(expected_live_out, allocator)
    
    expected_web = {'x1': ['1', '2', '4', '5']}
    test_web(expected_web, allocator)

    expected_ig = []
    test_ig(expected_ig, allocator)

    expected_colors = {'x1': '1'} 
    test_colored_graph(expected_colors, allocator)

def only_used_after_redefinition():
    ir = [
        "Main:",
        "assign, x, 10.0,",
        "assign, p, 0.0",
        "assign, x, 10.0,",
        "add, p, x, 1,",
        "add, p, x, 1,",
        "add, p, x, 1,",
        "return, , ,"
        ]

    allocator = hw3.Allocator(ir)
    allocator.apply_functions()

    expected_block_numbers = ['None', '1', '1', '1', '1', '1', '1', '1'] 
    test_bb(expected_block_numbers, allocator)

    expected_cfg = [] 
    test_cfg(expected_cfg, allocator)

    expected_defs = ['', '', '', 'x', '', '', '', ''] 
    test_defs(expected_defs, allocator)

    expected_uses = [[], [], [], [], ['x'], ['x'], ['x'], []] 
    test_uses(expected_uses, allocator)

    expected_live_in = [[], [], [], [], ['x'], ['x'], ['x'], []]
    test_livein(expected_live_in, allocator)
    
    expected_live_out = [[], [], [], ['x'], ['x'], ['x'], [], []]
    test_liveout(expected_live_out, allocator)
    
    expected_web = {'x1': ['3', '4', '5', '6']} 
    test_web(expected_web, allocator)

    expected_ig = []
    test_ig(expected_ig, allocator)

    expected_colors = {'x1': '1'}
    test_colored_graph(expected_colors, allocator)


def only_used_after_redefinition_jumps():
    ir = [
        "Main:",
        "assign, x, 10.0,",
        "assign, p, 0.0",
        "assign, x, 10.0,",
        "goto, after, ,",
        "add, p, x, 1,",
        "add, p, x, 1,",
        "add, p, x, 1,",
        "after:",
        "add, p, x, 1,",
        "add, p, x, 1,",
        "add, p, x, 1,",
        "return, , ,"
        ]

    allocator = hw3.Allocator(ir)
    allocator.apply_functions()

    expected_block_numbers = ['None', '1', '1', '1', '1', '2', '2', '2', 'None', '3', '3', '3', '3']
    test_bb(expected_block_numbers, allocator)

    expected_cfg = ['1 -> 3', '2 -> 3'] 
    test_cfg(expected_cfg, allocator)

    expected_defs = ['', '', '', 'x', '', '', '', '', '', '', '', '', ''] 
    test_defs(expected_defs, allocator)

    expected_uses = [[], [], [], [], [], [], [], [], [], ['x'], ['x'], ['x'], []] 
    test_uses(expected_uses, allocator)

    expected_live_in = [[], [], [], [], ['x'], ['x'], ['x'], ['x'], [], ['x'], ['x'], ['x'], []] 
    test_livein(expected_live_in, allocator)
    
    expected_live_out = [[], [], [], ['x'], ['x'], ['x'], ['x'], ['x'], [], ['x'], ['x'], [], []] 
    test_liveout(expected_live_out, allocator)
    
    expected_web = {'x1': ['3', '4', '9', '10', '11']} 
    test_web(expected_web, allocator)

    expected_ig = []
    test_ig(expected_ig, allocator)

    expected_colors = {'x1': '1'}
    test_colored_graph(expected_colors, allocator)

def ig_partial_overlap():
    ir = [
        "Main:",
        "assign, x, 10.0,",
        "assign, y, 0.0",
        "add, p, x, 10.0,",
        "assign, z, 10.0,",
        "add, p, y, 10.0,",
        "add, p, z, 10.0,",
        "return, , ,"
        ]

    allocator = hw3.Allocator(ir)
    allocator.apply_functions()

    expected_block_numbers = ['None', '1', '1', '1', '1', '1', '1', '1'] 
    test_bb(expected_block_numbers, allocator)

    expected_cfg = [] 
    test_cfg(expected_cfg, allocator)

    expected_defs = ['', 'x', 'y', '', 'z', '', '', '']
    test_defs(expected_defs, allocator)

    expected_uses = [[], [], [], ['x'], [], ['y'], ['z'], []] 
    test_uses(expected_uses, allocator)

    expected_live_in = [[], [], ['x'], ['x', 'y'], ['y'], ['y', 'z'], ['z'], []]
    test_livein(expected_live_in, allocator)
    
    expected_live_out = [[], ['x'], ['x', 'y'], ['y'], ['y', 'z'], ['z'], [], []] 
    test_liveout(expected_live_out, allocator)
    
    expected_web = {'x1': ['1', '2', '3'], 'y1': ['2', '3', '4', '5'], 'z1': ['4', '5', '6']} 
    test_web(expected_web, allocator)

    expected_ig = ['x1 -- y1', 'y1 -- z1'] 
    test_ig(expected_ig, allocator)

    expected_colors = {'z1': '1', 'y1': '2', 'x1': '1'} # x and Z share since they don't overlap!
    test_colored_graph(expected_colors, allocator)


def spills_first_if_usage_ties():
    ir = [
        "Main:",
        "assign, w, 10.0,",
        "assign, x, 10.0,",
        "assign, y, 0.0,",
        "assign, z, 0.0,",

        "add, p, w, 10.0,",
        "add, p, x, 10.0,",
        "add, p, y, 10.0,",
        "add, p, z, 10.0,",
        "return, , ,"
        ]

    allocator = hw3.Allocator(ir)
    allocator.apply_functions()

    expected_block_numbers = ['None', '1', '1', '1', '1', '1', '1', '1', '1', '1'] 
    test_bb(expected_block_numbers, allocator)

    expected_cfg = [] 
    test_cfg(expected_cfg, allocator)

    expected_defs = ['', 'w', 'x', 'y', 'z', '', '', '', '', '']  
    test_defs(expected_defs, allocator)

    expected_uses =  [[], [], [], [], [], ['w'], ['x'], ['y'], ['z'], []]
    test_uses(expected_uses, allocator)

    expected_live_in = [[], [], ['w'], ['w', 'x'], ['w', 'x', 'y'], ['w', 'x', 'y', 'z'], ['x', 'y', 'z'], ['y', 'z'], ['z'], []]
    test_livein(expected_live_in, allocator)
    
    expected_live_out = [[], ['w'], ['w', 'x'], ['w', 'x', 'y'], ['w', 'x', 'y', 'z'], ['x', 'y', 'z'], ['y', 'z'], ['z'], [], []] 
    test_liveout(expected_live_out, allocator)
    
    expected_web = {'w1': ['1', '2', '3', '4', '5'], 'x1': ['2', '3', '4', '5', '6'], 'y1': ['3', '4', '5', '6', '7'], 'z1': ['4', '5', '6', '7', '8']}
    test_web(expected_web, allocator)

    expected_ig = ['w1 -- x1', 'w1 -- y1', 'w1 -- z1', 'x1 -- y1', 'x1 -- z1', 'y1 -- z1']
    test_ig(expected_ig, allocator)

    expected_colors = {'z1': 'spill', 'y1': '3', 'x1': '2', 'w1': '1'}
    test_colored_graph(expected_colors, allocator)

def spills_least_defs():
    ir = [
        "Main:",
        "assign, w, 10.0,",
        "assign, w, w,",
        "assign, x, 10.0,",
        "assign, x, x,",
        "assign, y, 0.0,",
        "assign, y, y,",
        "assign, z, 0.0,",

        "add, p, w, 10.0,",
        "add, p, x, 10.0,",
        "add, p, y, 10.0,",
        "add, p, z, 10.0,",
        "return, , ,"
        ]

    allocator = hw3.Allocator(ir)
    allocator.apply_functions()

    expected_ig = ['w1 -- x1', 'w1 -- y1', 'w1 -- z1', 'x1 -- y1', 'x1 -- z1', 'y1 -- z1']
    test_ig(expected_ig, allocator)

    expected_colors = {'z1': 'spill', 'y1': '3', 'x1': '2', 'w1': '1'}
    test_colored_graph(expected_colors, allocator)

def spills_least_uses():
    ir = [
        "Main:",
        "assign, w, 10.0,",
        "assign, x, 10.0,",
        "assign, y, 0.0,",
        "assign, z, 0.0,",

        "add, p, w, 10.0,",
        "add, p, w, 10.0,",

        "add, p, x, 10.0,",
        "add, p, x, 10.0,",

        "add, p, y, 10.0,",

        "add, p, z, 10.0,",
        "add, p, z, 10.0,",
        "return, , ,"
        ]

    allocator = hw3.Allocator(ir)
    allocator.apply_functions()

    expected_ig = ['w1 -- x1', 'w1 -- y1', 'w1 -- z1', 'x1 -- y1', 'x1 -- z1', 'y1 -- z1']
    test_ig(expected_ig, allocator)

    expected_colors = {'z1': '3', 'y1': 'spill', 'x1': '2', 'w1': '1'}
    test_colored_graph(expected_colors, allocator)

print("three variables.")
test_three_variables()
print("only fallthrough use.")
only_fallthrough_usage()
print("only branch usage.")
only_branch_usage()
print("diamond sides.")
test_unused_diamond_sides()
print("non-overlapping left and right.")
non_overlapping_left_and_right()
print("loop extra liveness.")
loop_extra_liveness()
print("jump fallthrough match.")
jump_fallthrough_match()
print("unreachable uses.")
unreachable_uses()
print("only used after redefine.")
only_used_after_redefinition()
print("only use after redefinition and jump.")
only_used_after_redefinition_jumps()
print("IG partial overlap.")
ig_partial_overlap()
print("Spills first if usages tie.")
spills_first_if_usage_ties()
print("spills least defs.")
spills_least_defs()
print("spill least uses.")
spills_least_uses()

# test unreachable uses and defs do not contribute to costs.
