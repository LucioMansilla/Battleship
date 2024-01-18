# views.py
from flask import jsonify
import random
from app import app

@app.route('/rng', methods=['GET'])
def get_random_number():
    random_number = random.randint(1, 15)
    return jsonify({'rng': random_number})




