# FastAPI Test Management System

## Project Description

This project is an online test management system built using FastAPI and MySQL. The system allows admins to create, update, and delete tests, while users can register, attempt tests, and view their results. The application uses SQLAlchemy for ORM and Alembic for database migrations.

### Features

- **Admin**:
  - Create, update, and delete tests.
  - Manage test questions and answers.
  - View user submissions and results.

- **User**:
  - Register and log in.
  - Attempt available tests.
  - View their own test results.

## Setup and Installation

### Prerequisites

Ensure you have Docker installed on your machine. If not, follow the installation guide at [Docker Install](https://docs.docker.com/get-docker/).

### 1. Clone the Repository

```bash
git@github.com:m-umarr/online-test-management.git
cd online-test-management
