# Project: Flask and VueJS in MVC pattern

- Created by: Luu Van Thanh
- Updated at: 22-10-2023

## Table of Contents

- [Project: Flask and VueJS in MVC pattern](#project-flask-and-vuejs-in-mvc-pattern)
  - [Table of Contents](#table-of-contents)
  - [Technologies Used](#technologies-used)
    - [Backend:](#backend)
    - [Frontend:](#frontend)
    - [Deployment:](#deployment)
  - [Key Features](#key-features)
  - [Endpoints](#endpoints)
  - [Installation](#installation)
  - [Todo](#todo)
    - [Backend:](#backend-1)
    - [Frontend:](#frontend-1)
  - [Contact](#contact)

## Technologies Used

### Backend:

- Flask
- Flask-RESTful
- Flask-JWT
- SQLAlchemy
- PostgreSQL

### Frontend:

- VueJS
- Vue Router
- Vuex
- Axios

### Deployment:

- Docker
- Docker Compose

## Key Features

The key features of this web include:

- Token authen
- Retrict premission for normal user and admin
- User login and registration
- Product search
- Product management
- Add/edit/delete products
- Paginated product listing
- Product details page

## Endpoints

| Endpoint                                   | Description                      |
| ------------------------------------------ | -------------------------------- |
| **GET /users/**                      | Get list of users                |
| **POST /users/user**                 | Create a new user                |
| **DELETE /users/{user_id}**          | Delete a user                    |
| **GET /users/{user_id}**             | Get a user                       |
| **PUT /users/{user_id}**             | Update a user                    |
| **POST /auth/login**                 | Login                            |
| **POST /auth/refresh**               | Refresh access token             |
| **POST /auth/register**              | Register new user                |
| **DELETE /auth/revoke_access**       | Revoke access and refresh tokens |
| **GET /categories/**                 | Get list of categories           |
| **POST /categories/category**        | Create a new category            |
| **DELETE /categories/{category_id}** | Delete a category                |
| **GET /categories/{category_id}**    | Get a category                   |
| **PUT /categories/{category_id}**    | Update a category                |
| **GET /products/**                   | Get list of products             |
| **POST /products/product**           | Create a new product             |
| **DELETE /products/{product_id}**    | Delete a product                 |
| **GET /products/{product_id}**       | Get a product                    |
| **PUT /products/{product_id}**       | Update a product                 |

## Installation

1. Clone this repository:

```
git clone https://github.com/ThanhLV97/mvc_python_application.git
```

2. Navigate to the project directory:

```
cd mvc_python_application
```

3. Create .env.dev file
   ```
   mv src/backend/.env.example src/backend/.env.dev 
   ```
4. Build and start the Docker containers:

```
docker-compose up --build -d
```

4. Initialize the database:

```
docker-compose exec -it app bash

flask init_db
```

5. Open the Swagger API documentation:Navigate to http://localhost:5000
6. Access the frontend:
   Navigate to http://localhost:8080
7. Register a new user:

- You can register a new user through the frontend at http://localhost:8080/register
- or through the Swagger docs in the auth namespace: http://localhost:5000
  ![Register](image-1.png)

8. Assign user roles:
   To assign roles for a user, comeback terminal and run:

```
docker-compose exec -it app bash

flask assign_role <username> <role>
```

Where:

``<username>`` is the username you registered

`` <role>`` is "User" or "Admin"

## Todo

### Backend:

- [X] Implement token authen
- [X] Implement login, register and logout api
- [X] implement user api
- [X] Implement product and category api
- [X] Implement restrict repermission for product
- [ ] Integrating with frontend for the product searching

### Frontend:

- [X] Init master template with header and footer
- [X] Implement login and register page
- [X] Implement product searching with category filtering
- [ ] Integrate product searching
- [ ] Implement product page for listing product
- [ ] Integrate product searching

## Contact

Reach me at

* [Facebook](https://www.facebook.com/ambitionsky/)
* [Linkedin](https://www.linkedin.com/in/thanhlv97/)
* [Skype](https://join.skype.com/invite/k9Cb7FxyLhIH)
