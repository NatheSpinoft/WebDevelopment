from flask import Flask, jsonify, request

app = Flask(__name__)

#Sample Data

pizzas = [

    { "id" : 1, "name" : "Margharita", "ingredients": ["tomato", "mozzarella", "basil"], "price" : 12.99},
    { "id" : 2, "name" : "Pepperoni", "ingredients": ["tomato", "pepperoni", "cheese"], "price" : 13.99},
    { "id" : 3, "name" : "Meat Lovers", "ingredients": ["tomato", "pepperoni", "bacon", "sausage", "cheese"], "price" : 15.99}

]

# 1. Get the pizza menu
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    return jsonify(pizzas)

# 2. Retrieve Pizza by ID
@app.route('/pizzas/<int:pizza_id>', methods=['GET'])
def get_pizza(pizza_id):
    pizza = next((pizza for pizza in pizzas if pizza["id"] == pizza_id), None )
    if pizza:
        return jsonify(pizza)
    else:
        return jsonify({"error": "Pizza not found"}), 404

# 3. Add a new pizza
@app.route('/pizzas', methods=['POST'])
def add_pizza():
    new_pizza = request.get_json()
    new_pizza['id'] = len(pizzas) + 1
    pizzas.append(new_pizza)
    return jsonify(new_pizza), 201

# 4. Update an existing pizza by ID
@app.route('/pizzas/<int:pizza_id>', methods=['PUT'])
def update_pizza(pizza_id):
    updated_data = request.get_json()
    pizza = next ((pizza for pizza in pizzas if pizza ['id'] == pizza_id), None)
    if pizza:
        pizza.update(updated_data)
        return jsonify(pizza)
    else:
        return jsonify({"error": "Pizza not found"}), 404
    
# 5. Delete - remove by ID
@app.route('/pizzas/<int:pizza_id>', methods=['DELETE'])
def delete_pizza(pizza_id):
    global pizzas
    pizzas = [pizza for pizza in pizzas if pizza['id'] != pizza_id]
    return jsonify({"message":"Pizza deleted"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)