pack_amt = int(input('Кол-во пакетов: '))
msg = []
bad_packs = 0
for num_pack in range(1, pack_amt + 1):
    pack = []
    print('Пакет номер', num_pack )
    for i_bit in range(1, 5):
        print(i_bit, 'бит:', end=' ')
        bit = int(input())
        pack.append(bit)
    if pack.count(-1) > 1:
        bad_packs += 1
        print('Много ошибок в пакете.')
    else:
        msg.extend(pack)
print('Полученное сообщение:', msg)
print('Кол-во ошибок в сообщении:', msg.count(-1))
print('Кол-во потерянных пакетов:', bad_packs)
