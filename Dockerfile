# ==========================================
# STAGE 1: Dependency Compiler & Python Base
# ==========================================
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir "fastmcp[dev]"

# ==========================================
# STAGE 2: Secure Production Container Runtime
# ==========================================
# LOCKED: Matching python base version 3.12 to prevent runtime path drops
FROM python:3.12-slim AS runner

WORKDIR /app

RUN useradd -u 1001 -m appuser

# Copy matching 3.12 packages smoothly
COPY --from=base /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=base /usr/local/bin /usr/local/bin

COPY . .

RUN mkdir -p /app/data && chown -R appuser:appuser /app/data /app

USER appuser

EXPOSE 8000
EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

CMD ["python3"]