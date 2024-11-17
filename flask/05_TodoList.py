# Creating TODO LIST using flask

from flask import Flask, request, jsonify, redirect, render_template

app = Flask('__name__')

# Initial Data in TODO list

items = [
    {'id': 1, 'name': 'Item 1', 'description': 'This is item 1'},
    {'id': 2, 'name': 'Item 2', 'description': 'This is item 2'}
]

@app.route('/')
def home():
    return render_template('index.html')

# GET: Retrive all the todos
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET: Retrive item by Id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_by_id(item_id):
    item = next((item for item in items if item['id']==item_id), None)
    if item is None:
        return jsonify({'error': 'item not found'})
    return jsonify(item)

# POST: cerate a new item
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'error': 'item not found'})
    new_item={
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'description': request.json['description']
    }

    items.append(new_item)
    return jsonify(new_item)

# PUT: Update an existing file
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id']==item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# DELETE: Delete the item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'result':'Item deleted'})

if __name__ == '__main__':
    app.run(debug=True)

