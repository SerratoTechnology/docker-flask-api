# Base image: the official nginx image, tag "latest".
# This tag moves when a new nginx release is published, so a later build
# can pick up a different version than the one used today.
FROM nginx:latest

# Replace only the site config. The image already includes every file in
# /etc/nginx/conf.d/ from its main nginx.conf, which stays untouched.
# default.conf is a server block: it serves index.html and proxies /api
# to the backend container at http://backend:5001.
COPY default.conf /etc/nginx/conf.d/default.conf

# Copy the page nginx will serve.
# The default document root in the nginx image is /usr/share/nginx/html,
# so a request for / reads /usr/share/nginx/html/index.html.
COPY index.html /usr/share/nginx/html/

# Records that nginx listens on port 80 inside the container.
# It does not publish the port on the host. Compose does that with ports.
EXPOSE 80

# Main process of the container.
# "daemon off" keeps nginx in the foreground. If it backgrounds itself,
# the container's process 1 exits and Docker stops the container.
# The exec form (JSON list) makes nginx process 1, so it receives Docker's
# stop signals.
CMD ["nginx", "-g", "daemon off;"]
