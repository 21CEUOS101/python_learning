from flask import Flask , request , send_from_directory , send_file
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

# file upload
@app.post('/users/resume/<int:id>')
def upload_resume(id):
    resume = request.files['resume']

    # check if the file is a pdf
    if resume.filename.split('.')[-1] != 'pdf':
        return "Invalid file format. Please upload a pdf file."
    
    #check if the file is empty
    if resume.filename == '':
        return "No file selected. Please select a file to upload."
    
    # check if the file is too large
    if len(resume.read()) > 1000000:
        return "File is too large. Please upload a file less than 1MB."
    
    # save the file
    resume.save(f'resume-{id}.pdf')
    return "Resume uploaded successfully!"

# get the uploaded file
@app.get('/users/resume/<int:id>')
def get_resume(id):
    try:
        return send_file(f'../resume-{id}.pdf', as_attachment=True)
    except FileNotFoundError:
        return "File not found!"
    

if __name__ == '__main__':
    app.run(debug=True)