# FLASK API

This readme provides information on how to interact with the Flask API using any RESTful API client.

## Images used
```Flask Application```
```MySQL```
```Nginx```


## Prerequisites

- Docker
- Docker-compose

## Setup

1. Open the terminal in the project's directory
2. Type ```docker-compose up -d```
3. Type ```docker ps``` to ensure the containers are running
4. Interact with the API with any RESTful API Client

## API Requests

### Register

- **Description**: Registers an user.
- **URL**: `http://127.0.0.1/register`
- **Method**: POST
- **Body (JSON)**:
  ```json
  {
    "name": "Ahsan Tahseen",
    "email": "ahsan@gmail.com",
    "password": "123"
  }


### Login

- **Description**: Authenticate a user and obtain an access token.
- **URL**: `http://127.0.0.1/login`
- **Method**: POST
- **Body (JSON)**:
  ```json
  {
    "email": "ahsan@gmail.com",
    "password": "123"
  }

### Get Students

- **Description**: Retrieve all students.
- **URL**: `http://127.0.0.1/student/`
- **Method**: GET
- **Headers**:
  - `x-access-token: `


### Get Student by ID

- **Description**: Retrieve a student by ID.
- **URL**: `http://127.0.0.1/student/1`
- **Method**: GET
- **Headers**:
  - `x-access-token: `

### Insert Student

- **Description**: Insert a new student.
- **URL**: `http://127.0.0.1/student`
- **Method**: PUT
- **Headers**:
  - `x-access-token: `
- **Body (JSON)**:
  ```json
  {
    "name": "Ahsan",
    "age": 22,
    "cgpa": 3.67,
    "semester": 8
  }

### Update Student

- **Description**: Update a student by ID.
- **URL**: `http://127.0.0.1/student/3`
- **Method**: PUT
- **Headers**:
  - `x-access-token: `
- **Body (JSON)**:
  ```json
  {
    "name": "Hallar",
    "age": 24,
    "cgpa": 2.67,
    "semester": 6
  }

### Delete Student

- **Description**: Delete a student by ID.
- **URL**: `http://127.0.0.1/student/7`
- **Method**: DELETE
- **Headers**:
  - `x-access-token: `
