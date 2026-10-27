# Base image: Python 3.12 on Alpine, a small distribution.
# Alpine keeps the image light. The app only needs the interpreter and pip.
FROM python:3.12-alpine3.22

# Working directory inside the container, not on the host.
# Docker creates it if it does not exist. Relative paths in COPY, RUN, and CMD
# resolve from here, so "requirements.txt" means "/app/requirements.txt".
WORKDIR /app

# Copy only the dependency list, before the source code.
# This layer changes only when requirements.txt changes. While that file stays
# the same, Docker reuses the install below and does not download packages again.
COPY requirements.txt requirements.txt

# Install dependencies into this image layer.
# --no-cache-dir stops pip from storing a copy of the downloaded packages.
# That cache is never reused inside the image and would only take up space.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the build context into /app.
# The first "." is the project folder sent to Docker, already filtered by .dockerignore.
# The second "." is the WORKDIR, so files land in /app.
#
# Today this copies app.py next to the requirements.txt already in /app:
#   app.py  ->  /app/app.py
# A later package is included the same way, with no new COPY line:
#   api/routes.py  ->  /app/api/routes.py
# .venv, .env, and tests never arrive, because .dockerignore excludes them.
# Placed after pip install so editing these files does not reinstall dependencies.
COPY . .

# Records that the process listens on port 5001.
# It does not publish the port on the host. That happens at run time with -p 5001:5001.
EXPOSE 5001

# Main process of the container. The exec form (JSON list) makes Flask
# process 1, so it receives Docker's signals when the container stops.
# 0.0.0.0 listens on every interface. On 127.0.0.1, a port published
# with -p could not reach the app from outside the container.
# Flask looks for app.py and the "app" object by default, so FLASK_APP is unnecessary.
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5001"]
