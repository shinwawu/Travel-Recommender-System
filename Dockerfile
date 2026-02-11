# Use official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /code

# Copy requirements and install
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the app and data
COPY ./app /code/app
COPY ./data /code/data

# Run the API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]