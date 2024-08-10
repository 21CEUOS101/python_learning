from flask import Flask , request
from flask_cors import CORS

app = Flask(__name__)
CORS(app , resources={r"/*": {"origins": "*"}})

data = [
    {
    'name': 'John Doe',
    'email': 'john@gmail.com',
    'phone': '123-456-7890'
},
{
    'name': 'Jane Doe',
    'email': 'doe@gmail.com',
    'phone': '123-456-7890'
}
]

@app.get('/')
def index():
    return "Welcome to the home page!"

@app.get('/users')
def get_users():
    return data

# dynamic route
@app.get('/users/<int:id>')
def get_user(id):
    return data[id]

# get data from the request body
@app.post('/users')
def add_user():
    user = request.get_json()
    data.append(user)
    return "User added successfully!"

@app.put('/users/<int:id>')
def update_user(id, user):
    data[id] = user
    return "User updated successfully!"

@app.delete('/users/<int:id>')
def delete_user(id):
    data.pop(id)
    return "User deleted successfully!"

if __name__ == '__main__':
    app.run(debug=True)