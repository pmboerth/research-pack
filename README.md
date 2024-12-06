# Fall 2024 CS 3200 Project - Research Pack

This project is a web application called Research Pack designed to provide students and professors with an easy way to browse and post research opportunities. The app allows users to:
- Browse Research Opportunities: View research opportunities posted by other students and professors in various fields.
- Post Research Opportunities: Submit new research opportunities for other students and professors to apply to.
- Update Profile Information: Modify personal information, including academic details and research interests.

The application is built using Streamlit for the front-end and is integrated with a SQL database to fetch and store data. The backend was designed in python using flask to manage and retrieve research opportunities, while the front-end allows users to interact with the data in a clean and user-friendly interface. This project is containerized using Docker.

## Features

- Research Opportunities: View, apply for, and manage research opportunities posted by users.
- Post New Opportunities: Students and professors can post new opportunities for collaboration or research.
- Profile Update: Users can update their profile information, such as skills, department, and research interests.
- Search and Filter: Users can filter posts by group or research area to find opportunities that match their interests.

# Getting Started

## Prerequisites

Ensure you have the following tools installed:

- Frontend: Streamlit
- Backend: Flask API
- Database: SQL
- Containerization: Docker
- Other dependencies: Pandas, Requests

Currently, there are three major components which will each run in their own Docker Containers:

- Streamlit App in the `./app` directory
- Flask REST api in the `./api` directory
- SQL files for the data model and data base in the `./database-files` directory

### Folder Information

Folder Structure:

- /app                - Contains the Streamlit frontend app, responsible for displaying the user interface and handling user interactions.
- /api                - Contains the Flask backend API, which handles HTTP requests, manages business logic, and interacts with the database.
- /database-files     - Contains SQL database schema and setup files, which define the structure of the database and initialize it with necessary data.


## Running the Application

### Running with Docker

1. **Clone the repository**:

   ```bash
   git clone https://github.com/pmboerth/research-pack.git
   cd research-pack

2. **Build the Docker containers:**:

   ```bash
   docker-compose build

3. **Start the Docker containers:**:

   ```bash
   docker-compose up

This will start all necessary containers (backend, database, and front-end) and make the application accessible at http://localhost:8501.

4. **Access the App:**:

   ```bash
   http://localhost:8501

Open your browser and navigate to the above. You should see the Streamlit interface where you can browse and manage research opportunities.

## Demo Video
We have provided video of our app [here](https://drive.google.com/file/d/1vG_LS6ELH9ylFvzph3VNxXHPbOBSp0Ok/view?usp=sharing)
