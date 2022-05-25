def vowel_counter():
    print('Vowel Counter')
    sentence = input('Enter sentence: ')
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    print('*' * 50)
    print(sentence)
    print('*' * 50)
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    a_cap = 0
    e_cap = 0
    i_cap = 0
    o_cap = 0
    u_cap = 0
    total_vowel_count = 0
    for letters in sentence:
        if letters in vowels:
            total_vowel_count += 1
            if 'a' in letters:
                a += 1
            if 'e' in letters:
                e += 1
            if 'i' in letters:
                i += 1
            if 'o' in letters:
                o += 1
            if 'u' in letters:
                u += 1
            if 'A' in letters:
                a_cap += 1
            if 'E' in letters:
                e_cap += 1
            if 'I' in letters:
                i_cap += 1
            if 'O' in letters:
                o_cap += 1
            if 'U' in letters:
                u_cap += 1
    if a > 0:
        print(f'a: {a}')
    if e > 0:
        print(f'e: {e}')
    if i > 0:
        print(f'i: {i}')
    if o > 0:
        print(f'o: {o}')
    if u > 0:
        print(f'u: {u}')
    if a_cap > 0:
        print(f'A: {a_cap}')
    if e_cap > 0:
        print(f'E: {e_cap}')
    if i_cap > 0:
        print(f'I: {i_cap}')
    if o_cap > 0:
        print(f'O: {o_cap}')
    if u_cap > 0:
        print(f'U: {u_cap}')
    if total_vowel_count == 0:
        print('No vowel(s) detected.')
    if total_vowel_count != 0:
        print(f'Total vowels: {total_vowel_count}')


vowel_counter()
