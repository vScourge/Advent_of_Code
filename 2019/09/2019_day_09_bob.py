from operator import add, mul, lt, eq
from collections import defaultdict
from functools import wraps
from typing import List, Dict
import os

def coroutine(gen):
    @wraps(gen)
    def start(*args, **kwargs):
        g = gen(*args, **kwargs)
        next(g)
        return g
    return start

# @coroutine
def run_program(state: List[int]):
    if os.path.exists(r'D:\projects\ctg\main\out2.txt' ):
        os.remove( r'D:\projects\ctg\main\out2.txt' )

    def get_value(pntr, mode):
        if mode == 0:
            return memory[pntr]
        if mode == 1:
            return pntr
        if mode == 2:
            return memory[pntr+relative_base]

    two_param_operations = {
        1: add,
        2: mul,
        7: lt,
        8: eq,
    }

    pointer_position = 0
    relative_base = 0
    op_params = (0, 3, 3, 1, 1, 2, 2, 3, 3, 1)
    memory: Dict[int, int] = defaultdict(int) # Keeps me from guessing as to how much memory expansion I need to do.
    memory.update(enumerate(state)) # Fastest way to convert a list into a dictionary and keep the indicies in order.
    c = 0
    while memory[pointer_position] != 99:
        c += 1

        # Get the current opcode, and storage location
        opcode = f'{memory[pointer_position]:05d}'
        print( '---' )
        print( 'c =', c )
        print( 'rel_base =', relative_base )
        print( 'opcode =', opcode )

        op = int(opcode[-2:])
        modes = [int(c) for c in opcode[:-2]][::-1]
        param_count = op_params[op]
        storage_position = memory[pointer_position+param_count] if modes[param_count-1] == 0 else memory[pointer_position+param_count] + relative_base
        # Advance the pointer by 1 so we can start processing parameters.
        pointer_position += 1
        parameters = [get_value(memory[idx], mode) for idx, mode in zip(range(pointer_position, pointer_position+param_count), modes)]
        print( 'params =', ','.join( [ str(x) for x in parameters] ))

        increment = True

        if op in (1, 2, 7, 8): # 2 parameters
            memory[storage_position] = int(two_param_operations[op](parameters[0], parameters[1]))
        elif op == 3: # input
            print( 'rel_base =', relative_base )
            z = yield
            print( 'codes[ {0} ] = {1}'.format( storage_position, z ) )
            print( 'Writing input value {0} to idx {1}'.format( z, storage_position ) )
            memory[storage_position] = z
        elif op == 4: # output
            yield parameters[0]
        elif op == 9: # update offset
            print( 'Shifting relative base {0} + {1} = {2}'.format( relative_base, parameters[0], relative_base + parameters[0] ) )
            relative_base += parameters[0]
        elif (op == 5 and parameters[0]) or (op == 6 and not parameters[0]): # Jumps
            pointer_position = parameters[1]
            # We want to avoid incrementing the pointer position because we did a jump
            increment = False

        if increment:
            pointer_position += param_count

        print( 'rel_base =', relative_base )

        with open( r'D:\projects\ctg\main\out2.txt', 'a' ) as out_file:
            out_file.write( ','.join( [ str( x ) for x in memory.values( ) ] ) + '\n' )

        if c == 100:
            break

    return memory[0]

data = [int(v) for v in open('input.txt').read().split(',')]
#assert [v for v in run_program([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])] == [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
#assert [len(str(v)) for v in run_program([1102,34915192,34915192,7,4,7,99,0])] == [16]
#assert [v for v in run_program([104,1125899906842624,99])] == [1125899906842624]

boost = coroutine(run_program)(data)
print(boost.send(1))
boost = coroutine(run_program)(data)
print(boost.send(2))