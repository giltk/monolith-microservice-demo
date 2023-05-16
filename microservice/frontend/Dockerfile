# First stage
FROM node:alpine

# Create app directory
WORKDIR /usr/frontend

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
COPY package*.json ./
RUN npm install

# Copy app code
COPY . .

# Build production ready app for local usage
RUN npm run build

# Second stage
FROM nginx:latest

# Copy the configuration file for NGINX
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the app files
RUN mkdir -p /var/www/frontend/
COPY --from=0 /usr/frontend/build/ /var/www/frontend/