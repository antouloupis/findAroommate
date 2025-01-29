# findAroommate
## Overview

findAroommate is a Django-powered web application designed to help users find roommates or post listings for potential roommates. It allows users to create profiles, view available listings, and interact with others in their search for shared housing.

This is the production branch, optimized for running a live service. Instead of the default Django development server, Gunicorn is used along with Nginx to enhance performance and caching.

This application was developed as part of a BSc Computer Science thesis.

## Features:

- User Profiles: Create and manage user profiles.
- Listings: Post and browse roommate listings based on preferences like location and budget.
- Search & Filters: Search for listings using filters like location and room type.
- Contact Requests: Send contact requests to users for potential roommate connections.

## How to Run
### Prerequisites

Ensure you have the following tools installed:

- Docker: To build and run the application in containers.
- Docker Compose: To manage multi-container Docker applications.

### Steps:

1. Clone this repository
2. Configure the environment variables in both .env files.
Fill out the .env files with the appropriate settings. 

You may need to configure:

- Django secret key
- Database connection details
- Any other necessary configurations for the project (e.g., email, API keys)

Run the application with Docker Compose:
Make sure you have Docker and Docker Compose installed, then run the following command to start the application:

```docker-compose up```

This will build the Docker images and start the services defined in the docker-compose.yml (e.g., web server, database).
    
The application will be available at http://localhost.

Disclaimer: Any API key found in this repository, including those for Google Places API, is inactive and provided only as a placeholder. Ensure you replace them with your own valid API keys in the appropriate locations where the API is used before running the application (ex. create, edit, and single templates under the listings app.)
