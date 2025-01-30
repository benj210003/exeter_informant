# Use the official Node.js image as the base
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app's source code
COPY . /app

# Expose port 3000 (default React dev server port)
EXPOSE 3000

# Start the development server (with hot reloading)
CMD ["npm", "start"]
