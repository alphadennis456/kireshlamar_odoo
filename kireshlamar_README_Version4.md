# Odoo 16 Bar Payment Project

This project provides a ready-to-deploy Odoo 16 instance with a custom module (`hybrid_bar`) for bar payment management.

## Features

- **Bar Payment Management**: Create and manage bar payment records with customer name, amount, and state (Pending, Assigned, Completed).
- **Tree and Form Views**: Quickly view and update payments via user-friendly Odoo interfaces.
- **Dockerized & Compose-ready**: Easy local development and deployment, compatible with Render and other cloud platforms.

## Project Structure

```
kireshlamar/
├── Dockerfile
├── docker-compose.yml
├── custom_addons/
│   └── hybrid_bar/
│       ├── __init__.py
│       ├── __manifest__.py
│       ├── models/
│       │   └── hybrid_bar_models.py
│       └── views/
│           └── hybrid_bar_views.xml
└── README.md
```

## Setup Instructions

### 1. Prerequisites

- Docker and Docker Compose installed
- (Optional) [Render](https://render.com/) account for cloud deployment

### 2. Local Development

1. **Clone the repository** and navigate to the `kireshlamar` directory.
2. **Build and run with Docker Compose**:
   ```sh
   docker-compose up --build
   ```
3. Access Odoo at [http://localhost:8069](http://localhost:8069).

### 3. Custom Module Installation

- Go to Apps in Odoo, update the app list, and install the `Hybrid Bar` module.

### 4. Deployment to Render

- Deploy using Render’s Docker or Compose configuration.
- Use the provided Postgres connection details in your Render environment settings.

## Postgres Connection (Hardcoded for Render)

- **Host:** dpg-d26k3c95pdvs73a7ciug-a.frankfurt-postgres.render.com
- **Port:** 5432
- **User:** kireshlamar_db_user
- **Password:** 4iNX6hXHTUsdjeoTDTQcgOFrd8WCSLW4
- **Database:** kireshlamar_db

---

Enjoy managing your bar payments with Odoo 16!