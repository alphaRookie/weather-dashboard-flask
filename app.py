from flask import Flask, render_template, request, redirect, url_for, session
from weather import main as get_weather # from main func in 'weather.py'
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # needed for session

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # access form data (take what user type) and '.strip()' to remove space
        city = request.form['cityName'].strip() 
        country = request.form['countryCode'].strip() 

        # removes old leftovers from previous request (new post = fresh attempt)
        session.pop('data', None) 
        session.pop('error', None)

        if not city or not country:
            session['error'] = "Please enter your city and country code"
        else:
            data = get_weather(city, country) # calls weather logic
            if data is None:
                session['error'] = "City or Country code is not found" # if API fails, save error in session
            else:
                session['data'] = data # otherwise, save data in session

        return redirect(url_for('index'))  # ends POST request, and FORCE browser to make new request (to '/') using GET

    # GET request (after redirect)
    data = session.pop('data', None) # reads data and delete it immediately (stop shows same error/same city)
    error = session.pop('error', None)

    return render_template('index.html', data=data, error=error) # sends weather info or 'None' AND error message or 'None' to index.html

# Its like power button 
if __name__ == '__main__': # “Run the server only if this file is executed directly, Not when imported (e.g., tests, other scripts)” 
    app.run(debug=True) # auto-reload
