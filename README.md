# 📦 FastAPI Secure User Management & Authentication Service

A secure FastAPI web application featuring an asynchronous/synchronous database architecture powered by SQLAlchemy, robust input validation and serialization via Pydantic, password hashing, and token-based authentication. The project includes a comprehensive automated test suite and a continuous integration/continuous deployment (CI/CD) pipeline built with GitHub Actions that automates testing and publishes production container images to Docker Hub.

---

## 🐳 Docker Hub Repository

The automated CI/CD pipeline packages and deploys production-ready container images directly to Docker Hub upon passing all automated tests.

- **Docker Hub Repository**: [https://hub.docker.com/r/venki2005/fastapi-secure-app](https://hub.docker.com/r/venki2005/fastapi-secure-app)
- **Pull Latest Image**:
  ```bash
  docker pull venki2005/fastapi-secure-app:latest
  ```

---

## 🧪 How to Run Tests Locally

The test suite contains 75 comprehensive tests spanning unit tests (validating password hashing algorithms, password policies, and Pydantic schemas) and integration tests (validating PostgreSQL constraints, transactional rollbacks, database sessions, and authenticated endpoint lifecycles).

### 1. Database Setup

Integration tests require an active PostgreSQL instance. Spin up a container using Docker:

```bash
docker run --name local-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=app_db \
  -p 5432:5432 \
  -d postgres:15
```

Verify that the database container is healthy:

```bash
docker ps
```

### 2. Set Environment Variable & Execute Pytest

Export the database connection string and execute `pytest`:

```bash
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/app_db"

# Run all unit and integration tests with verbose output
pytest -v

# Run only unit tests
pytest -v tests/unit/

# Run only integration tests
pytest -v tests/integration/

# Generate an HTML test coverage report
pytest --cov=app --cov-report=html
```

---

## 🚀 Running the Project Locally

### Running via Uvicorn (Development Mode)

```bash
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/app_db"
uvicorn main:app --reload --port 8000
```

- **Interactive Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Running via Docker Container

```bash
# Build the local Docker image
docker build -t fastapi-secure-app:local .

# Run the container (using host network access for the PostgreSQL container)
docker run -p 8000:8000 \
  -e DATABASE_URL="postgresql://postgres:postgres@host.docker.internal:5432/app_db" \
  fastapi-secure-app:local
```

---

# 📦 Developer Machine Setup

---

## 🧩 1. Install Homebrew (Mac Only)

> Skip this step if you're on Windows.

Homebrew is a package manager for macOS. You’ll use it to easily install Git, Python, Docker, etc.

**Install Homebrew:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Verify Homebrew:**

```bash
brew --version
```

---

## 🧩 2. Install and Configure Git

### Install Git

- **macOS (using Homebrew)**:
  ```bash
  brew install git
  ```
- **Windows**:
  Download and install [Git for Windows](https://git-scm.com/download/win). Accept default options during installation.

### Configure Git Globals

Set your name and email so Git tracks your commits properly:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Confirm settings:

```bash
git config --list
```

### Generate SSH Keys and Connect to GitHub

> Only do this once per machine.

1. Generate a new SSH key:
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   (Press Enter at all prompts.)
2. Start the SSH agent:
   ```bash
   eval "$(ssh-agent -s)"
   ```
3. Add the SSH private key to the agent:
   ```bash
   ssh-add ~/.ssh/id_ed25519
   ```
4. Copy your SSH public key:
   - **macOS/Linux**: `cat ~/.ssh/id_ed25519.pub | pbcopy`
   - **Windows (Git Bash)**: `cat ~/.ssh/id_ed25519.pub | clip`
5. Add the key to your GitHub account under [GitHub SSH Settings](https://github.com/settings/keys).
6. Test connection:
   ```bash
   ssh -T git@github.com
   ```

---

## 🧩 3. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

---

## 🛠️ 4. Install Python 3.10+ & Virtual Environment

### Install Python

- **macOS**: `brew install python`
- **Windows**: Download from [Python for Windows](https://www.python.org/downloads/) (ensure **Add Python to PATH** is checked).

Verify installation:

```bash
python3 --version
```

### Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate.bat     # Windows
```

### Install Required Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🐳 5. Docker Desktop Setup

1. Install [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/) or [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/).
2. Verify Docker daemon is running:
   ```bash
   docker --version
   docker ps
   ```

---

## ⚙️ CI/CD Pipeline Overview

The GitHub Actions workflow (`.github/workflows/ci-cd.yml`) triggers on pushes to the `main` branch:

1. **Automated Testing**: Runs PostgreSQL service container and executes the full Pytest test suite.
2. **Automated Deployment**: Builds the container image with Docker Buildx and publishes tagged images (`:latest` and commit SHA) to Docker Hub.

---

## 📝 6. Submission Instructions

After completing and verifying all changes:

```bash
git add .
git commit -m "Complete secure user model, tests, and CI/CD deployment"
git push origin main
```

Submit your GitHub repository link along with the required workflow and Docker Hub screenshots.

---

## 🔥 Useful Commands Cheat Sheet

| Action                       | Command                                                                                                            |
| :--------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| Activate Virtual Environment | `source venv/bin/activate` / `venv\Scripts\activate.bat`                                                           |
| Install Python Packages      | `pip install -r requirements.txt`                                                                                  |
| Start Test Database          | `docker run --name local-postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=app_db -p 5432:5432 -d postgres:15` |
| Run Test Suite               | `pytest -v`                                                                                                        |
| Check Test Coverage          | `pytest --cov=app tests/`                                                                                          |
| Start FastAPI Local Server   | `uvicorn main:app --reload --port 8000`                                                                            |
| Build Docker Image           | `docker build -t fastapi-secure-app .`                                                                             |
| Push to GitHub               | `git add . && git commit -m "Update" && git push origin main`                                                      |

---

## 📎 Quick Links

- [Docker Hub Repository](https://hub.docker.com/r/venki2005/fastapi-secure-app)
- [Homebrew](https://brew.sh/)
- [Python Downloads](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [GitHub SSH Setup Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
