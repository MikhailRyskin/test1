players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}
list_a_rest = [player['name'] for player in players_dict.values() if player['team'] == 'A'
               and player['status'] == 'Rest']
print(list_a_rest)
list_b_training = [player['name'] for player in players_dict.values() if player['team'] == 'B'
                   and player['status'] == 'Training']
print(list_b_training)
list_c_travel = [player['name'] for player in players_dict.values() if player['team'] == 'C'
                 and player['status'] == 'Travel']
print(list_c_travel)
