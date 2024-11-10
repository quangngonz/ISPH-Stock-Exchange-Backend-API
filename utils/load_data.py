import json
import os

def load_data():
    base_dir = os.path.dirname(__file__)
    data_dir = os.path.join(base_dir, '../data')

    with open(os.path.join(data_dir, 'users.json')) as f:
        users = json.load(f)
    with open(os.path.join(data_dir, 'portfolios.json')) as f:
        portfolios = json.load(f)
    with open(os.path.join(data_dir, 'houses.json')) as f:
        houses = json.load(f)

    return users, portfolios, houses
