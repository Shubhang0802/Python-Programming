move = [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ']
st = '''

{}|{}|{}
-----
{}|{}|{}
-----
{}|{}|{}


'''.format(*move)
print(st)
turn = '0'
while 1:
    player_in=int(input(f'{turn} turn Enter location 0-8: '))
    if move[player_in]=='x' or move[player_in]=='0':
        print('Position already used, try another position')
        continue
    else:
        move[player_in]=turn
        st = '''

        {}|{}|{}
        -----
        {}|{}|{}
        -----
        {}|{}|{}


        '''.format(*move)
    print(st)
    if move[0]==move[1]==move[2]!=' ':
        print(move[0], 'wins')
        break
    if move[3]==move[4]==move[5]!=' ':
        print(move[3], 'wins')
        break
    if move[6]==move[7]==move[8]!=' ':
        print(move[6], 'wins')
        break
    if move[0]==move[4]==move[8]!=' ':
        print(move[0], 'wins')
        break
    if move[2]==move[4]==move[6]!=' ':
        print(move[2], 'wins')
        break
    if move[0]==move[3]==move[6]!=' ':
        print(move[0], 'wins')
        break
    if move[1]==move[4]==move[7]!=' ':
        print(move[1], 'wins')
        break
    if move[2]==move[5]==move[8]!=' ':
        print(move[0], 'wins')
        break
    if ' ' not in move:
        print('Match Draw')
        break
    turn = 'x' if turn == '0' else '0'
    

        
        
