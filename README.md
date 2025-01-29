#findAroommate (for development)
##Overview

findAroommate is a Django-powered web application designed to help users find roommates or post listings to search for potential roommates. It allows users to create profiles, view available listings, and interact with others in their search for shared housing.

This application was developed as part of a thesis for a BSc degree in Computer Science.

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
2. Configure the environment variables in both .env files:
Fill out the .env file(s) with the appropriate settings. 
- You may need to configure:

- Django secret key
- Database connection details
- Any other necessary configurations for the project (e.g., email, API keys)


Run the application with Docker Compose:
Make sure you have Docker and Docker Compose installed, then run the following command to start the application:

```docker-compose up```

This will build the Docker images and start the services defined in the docker-compose.yml (e.g., web server, database).
    
The application will be available at http://localhost:8000.