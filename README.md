# FastAPI Project with uv and Ruff

This project uses **FastAPI** with [**uv**](https://github.com/astral-sh/uv) to manage dependencies and includes [**Ruff**](https://github.com/charliermarsh/ruff) for linting. It also comes with a **Dockerfile** and a **docker-compose.yml** for containerizing the application.

---

## Requirements

- **Python 3.13.2** (recommended)
- **uv** (to install dependencies and run commands)
- **Ruff** (for linting; installed via `uv sync` if defined in `pyproject.toml`)
- *(Optional)* **Docker** and **Docker Compose** (for containerization)

---

## Installation and Running with uv

1. **Install `uv`** (if not already installed):
   ```bash
   pip install uv
   ```
   Or check the [uv official documentation](https://github.com/astral-sh/uv) for other install options.

2. **Clone this repository**:
   ```bash
   git clone https://github.com/Afordin/beerdin-api
   cd beerdin-api
   ```

3. **Sync dependencies**:
   ```bash
   uv sync
   ```
   - This will create or update the `.venv` virtual environment and install all dependencies (including Ruff).

4. **Run the application** (using the FastAPI CLI, installed inside `.venv`):
   ```bash
      uv run fastapi dev
   ```

   - Once running, the app will be available at:
     ```
     http://localhost:8000
     ```
   - The API docs are located at:
     ```
     http://localhost:8000/docs
     ```

---

## Using Ruff with uv

To run **Ruff** via uv, simply execute:

```bash
uv run ruff check .
```

This will lint your code and display any style or syntax suggestions.

---

## Running with Docker

### Dockerfile

The included **Dockerfile**:
1. Uses a slim Python base image.
2. Copies the `uv` binary.
3. Copies the project into `/app`.
4. Runs `uv sync` to install dependencies.
5. Uses `fastapi` to start the app within the container.

### docker-compose.yml

You’ll also find a **docker-compose.yml** file for running the service. Use it like so:

```bash
docker-compose build
docker-compose up -d
```

This:
- **Builds** the image using the Dockerfile.
- **Starts** the container mapping the internal port (usually `80`) to `8000` on your host.  
- Your application will be available at `http://localhost:8000`.

---

## Project Structure (Example)

- **app/main.py**  
  Main entry point for the FastAPI application.
- **pyproject.toml**  
  Project info and dependencies (used by `uv` and Ruff).
- **Dockerfile**  
  Instructions for building the Docker image.
- **docker-compose.yml**  
  Optional file for starting containers with Docker Compose.
- **.gitignore**  
  Lists files and folders to ignore (e.g., `.venv/`, `.ruff_cache/`, etc.).
