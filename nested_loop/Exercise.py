width = int(input())
length = int(input())
cake_size = width * length
piece_taken = 0
total_pieces_taken = 0

while total_pieces_taken <= cake_size:
    piece_taken = input()
    if piece_taken == 'STOP':
        break
    else:
        piece_taken = int(piece_taken)
        total_pieces_taken = total_pieces_taken + piece_taken

if cake_size > total_pieces_taken or piece_taken == 'STOP':
    difference = cake_size - total_pieces_taken
    print(f'{difference} pieces are left.')
else:
    difference = total_pieces_taken - cake_size
    print(f'No more cake left! You need {difference} pieces more.')
