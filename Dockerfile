FROM python:3.11-slim

# Sets the default directory inside the container 
# all subsequent COPY, RUN, and CMD commands after this line goes to "/app"
WORKDIR /app 

# Copy 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Put after pip, so changing the code doesn’t trigger dependency reinstall
COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]
