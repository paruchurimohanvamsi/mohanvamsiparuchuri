from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Sample projects data - you can customize this with your actual projects
projects = [
    {
        'id': 1,
        'title': 'Credit Card Fraud Detection',
        'description': 'Machine learning model to detect fraudulent credit card transactions using Python and scikit-learn.',
        'technologies': ['Python', 'scikit-learn', 'pandas', 'numpy', 'matplotlib'],
        'github_url': 'https://github.com/parchurimohanvasmsi/fraud-transcations-in-crdit-card',
        'live_url': 'https://github.com/parchurimohanvasmsi/fraud-transcations-in-crdit-card',
        'image': 'credit-card-fraud.jpg'
    },
    {
        'id': 2,
        'title': 'Heart Disease Prediction',
        'description': 'Automated data extraction from websites using Python web scraping techniques.',
        'technologies': ['Python', 'BeautifulSoup', 'requests', 'pandas','Ibm Ananlytics','Ibm cloud'],
        'github_url': 'https://github.com/parchurimohanvasmsi/Visualizing-and-Predicting-Heart-Diseases-with-an-Interactive-Dash-Board',
        'live_url': 'https://github.com/parchurimohanvasmsi/Visualizing-and-Predicting-Heart-Diseases-with-an-Interactive-Dash-Board',
        'image': 'web-scraping.jpeg'
    },
    {
        'id': 3,
        'title': 'ATM Program',
        'description': 'Interactive ATM simulation with user authentication and transaction management.',
        'technologies': ['Python', 'SQLite', 'tkinter'],
        'github_url': 'https://github.com/parchurimohanvasmsi/python-mini-projects',
        'live_url': 'https://github.com/parchurimohanvasmsi/python-mini-projects',
        'image': 'atm-program.jpg'
    },
    {
        'id': 4,
        'title': 'Co2 emmision from flights',
        'description': 'calucluated more than 50000 flights and their co2 emmision where data is gatherd by using web scraping',
        'technologies': ['Python', 'pandas', 'numpy', 'matplotlib', 'seaborn'],
        'github_url': '#',
        'live_url': '#',
        'image': 'data-analysis.jpg'
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle contact form submission
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Here you could add email sending functionality
        return jsonify({'success': True, 'message': 'Message sent successfully!'})
    return render_template('contact.html')

@app.route('/api/projects')
def api_projects():
    return jsonify(projects)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0') # Corrected 'flase' to 'False'