## Project: Flask and VueJS in MVC pattern
* Created by: Luu Van Thanh
* Updated at: 22-10-2023

### Technologies Used

#### Backend:

* Flask
* Flask-RESTful
* Flask-JWT
* SQLAlchemy
* PostgreSQL

#### Frontend:

* VueJS
* Vue Router
* Vuex
* Axios

#### Deployment:

* Docker
* Docker Compose

### Key Features

The key features of this web include:

* Token authen
* Retrict premission for normal user and admin
* User login and registration
* Product search
* Product management
* Add/edit/delete products
* Paginated product listing
* Product details page

### Installation

To run the project locally, follow these steps:

```
docker-compose up --build -d
```

```
 docker-compose exec -it app bash
```

Run CLI to init master table

```
 flask init_db
```

Access into http://localhost:8080

Assign role for user by running cli:

```
flask assign_role <user_name> <"User"|"Amind">
```

### TODO

Backend:

- [X] Implement token authen
- [X] Implement login, register and logout api
- [X] implement user api
- [X] Implement product and category api
- [X] Implement restrict repermission for product

Frontend:

- [X] Init master template with header and footer
- [X] Implement login and register page
- [X] Implement product searching with category filtering
- [ ] Integrate product searching
- [ ] Implement product page for listing product
- [ ] Integrate product searching
