#1️⃣ Use an official lightweight Python image
FROM python:3.11-slim

# 2️⃣ Set working directory inside the container
WORKDIR /app

# 3️⃣ Copy your project files into the container
COPY . /app

# 4️⃣ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Expose the port your app runs on (usually 5000)
EXPOSE 5000

# 6️⃣ Start the app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
