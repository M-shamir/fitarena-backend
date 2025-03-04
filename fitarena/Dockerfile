FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy Pipfile and Pipfile.lock to install dependencies
COPY Pipfile Pipfile.lock /app/

# Install pipenv and project dependencies
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --deploy --ignore-pipfile

# Copy the rest of the application code to the container
COPY . /app/

# Run migrations and start the Django application
CMD ["pipenv", "run", "python", "manage.py", "migrate"]
