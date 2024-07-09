from flask import Flask, render_template, request
import re
import csv

# Create a Flask app
app = Flask(__name__)

csvfile = 'user_data.csv'

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

def save_to_csv(user_data, filename):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(user_data)

# Define a route for the landing page
@app.route('/')
def landing_page():
    return render_template('landing_page.html')
    
# Define a route for processing form submissions
@app.route('/subscribe', methods=['POST'])
def subscribe():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        if is_valid_email(email):
             save_to_csv([name, email], csvfile)
        
        # Redirect the user to a thank you page
        return render_template('thank_you.html')
        
# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
