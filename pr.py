
tel = input()
if tel[0] == '8' or tel[0:2] == '+7':
    tel = [a for a in tel if a not in ['(', ')', ' ', '-']]
    if tel[0] == '8':
        tel[0] = '+7'
    print(''.join(tel))
if '  ' not in tel:
    tel = [a for a in tel if a not in ['(', ')', ' ', '-']]
    if tel[0] == '8':
        tel[0] = '+7'
    print(''.join(tel))
if '--' not in tel:
    tel = [a for a in tel if a not in ['(', ')', ' ', '-']]
    if tel[0] == '8':
        tel[0] = '+7'
    print(''.join(tel))
elif tel.count('(') == tel.count(')'):
    tel = [a for a in tel if a not in ['(', ')', ' ', '-']]
    if tel[0] == '8':
        tel[0] = '+7'
    print(''.join(tel))
else:
    raise Exception('error')
