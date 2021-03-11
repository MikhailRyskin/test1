server_data = {

    "server": {

        "host": "127.0.0.1",

        "port": "10"

    },

    "configuration": {

        "access": "true",

        "login": "Ivan",

        "password": "qwerty"

    }
}
for key, value in server_data.items():
    print(f'{key}:')
    for in_key, in_value in value.items():
        print(f'    {in_key} : {in_value}')
