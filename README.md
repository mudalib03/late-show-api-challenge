# Late Show API

A Flask REST API for managing a Late Night TV show system.

## Features

- MVC architecture
- PostgreSQL database
- JWT authentication
- Flask blueprints for modular routes
- API tested with Postman

## Folder Structure

```
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   ├── controllers/
├── migrations/
├── challenge-4-lateshow.postman_collection.json
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/late-show-api-challenge.git
   cd late-show-api-challenge
   ```

2. **Install dependencies:**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Configure PostgreSQL:**
   - Create a database:
     ```sql
     CREATE DATABASE late_show_db;
     ```
   - Edit `server/config.py` with your DB credentials.

4. **Run migrations and seed data:**
   ```bash
   export FLASK_APP=server/app.py
   export PYTHONPATH=.
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   python server/seed.py
   ```

5. **Run the server:**
   ```bash
   export FLASK_APP=server/app.py
   export PYTHONPATH=.
   flask run
   ```

## Authentication Flow

- **Register:** `POST /register` — Create a user.
- **Login:** `POST /login` — Get JWT token.
- **Protected routes:** Send `Authorization: Bearer <token>` header.

## API Routes

| Route                       | Method | Auth Required | Description                       |
|-----------------------------|--------|---------------|-----------------------------------|
| `/register`                 | POST   | ❌            | Register a user                   |
| `/login`                    | POST   | ❌            | Log in and get JWT token          |
| `/episodes`                 | GET    | ❌            | List episodes                     |
| `/episodes/<int:id>`        | GET    | ❌            | Get episode + appearances         |
| `/episodes/<int:id>`        | DELETE | ✅            | Delete episode + appearances      |
| `/guests`                   | GET    | ❌            | List guests                       |
| `/appearances`              | POST   | ✅            | Create appearance                 |

## Postman

- Import `challenge-4-lateshow.postman_collection.json` into Postman to test all endpoints.

## Testing

- Run tests with:
  ```bash
  pytest
  ```

## License

MIT

---

**GitHub:** [https://github.com/<your-username>/late-show-api-challenge](https://github.com/<your-username>/late-show-api-challenge)
