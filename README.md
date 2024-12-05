# Fall 2024 CS 3200 Project - Research Pack

This project is a web application called Research Pack designed to provide students and professors with an easy way to browse and post research opportunities. The app allows users to:
- Browse Research Opportunities: View research opportunities posted by other students and professors in various fields.
- Post Research Opportunities: Submit new research opportunities for other students and professors to apply to.
- Update Profile Information: Modify personal information, including academic details and research interests.

The application is built using Streamlit for the front-end and is integrated with a SQL database to fetch and store data. The backend is designed to manage and retrieve research opportunities, while the front-end allows users to interact with the data in a clean and user-friendly interface. This project is containerized using Docker.

## Features

Research Opportunities: View, apply for, and manage research opportunities posted by users.
Post New Opportunities: Students and professors can post new opportunities for collaboration or research.
Profile Update: Users can update their profile information, such as skills, department, and research interests.
Search and Filter: Users can filter posts by group or research area to find opportunities that match their interests.

## Prerequisites

- Streamlit: A Python-based framework for building interactive web applications.
- SQL Database: A relational database for storing user and research opportunity data.
- Docker: Containerization platform for packaging the app with all dependencies for easy deployment.
- Requests: For making HTTP requests to interact with APIs.
- Pandas: For data manipulation (if applicable to the project).


## Current Project Components

Currently, there are three major components which will each run in their own Docker Containers:

- Streamlit App in the `./app` directory
- Flask REST api in the `./api` directory
- SQL files for your data model and data base in the `./database-files` directory

## Suggestion for Learning the Project Code Base
 
