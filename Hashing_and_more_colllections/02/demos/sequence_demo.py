from collections.abc import Sequence

def use_sequence(seq: Sequence):
    print(f'the type of this sequence is {type(seq)}')
    assert(issubclass(type(seq), Sequence))
    print(f'it\'s length is {len(seq)}')
    print(f'here is it\'s repr {repr(seq)}')
    print('here are all it\'s items:')
    for seq_item in seq:
        print(seq_item)
    print('_' * 20)
    return

r_seq = range(0,20)
l_seq = [i for i in r_seq]
s_seq = ''.join(map(str, r_seq))
b_seq = bytes(r_seq)
ba_seq = bytearray(r_seq)
mv_seq = memoryview(b_seq)
all_seq = [r_seq, l_seq, s_seq, b_seq, ba_seq, mv_seq]

for seq_item in all_seq:
    use_sequence(seq_item)