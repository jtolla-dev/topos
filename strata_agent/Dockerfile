FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN apt-get update && apt-get install -y \
    curl \
    && curl -LsSf https://astral.sh/uv/install.sh | sh \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin:$PATH"

# Copy project files
COPY pyproject.toml .
COPY strata_agent/ strata_agent/

# Install dependencies
RUN uv pip install --system --no-cache .

# Config will be mounted at runtime
CMD ["strata-agent", "--config", "/config/config.yaml"]
