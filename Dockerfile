FROM python:3.11-slim

# 1. Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 2. Copy ONLY the dependency files first (for better caching)
COPY pyproject.toml uv.lock ./

# 3. Install dependencies 
# --frozen: ensures uv.lock isn't changed
# --no-install-project: skips installing the FRAgent code itself in this layer
RUN uv sync --frozen --no-install-project --no-dev

# 4. Copy the rest of your code
COPY . .

# 5. Final sync to install the actual project code
RUN uv sync --frozen --no-dev

# Place the virtualenv binaries on the PATH so you don't need to "activate"
ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv", "run", "main.py"]