# 1. Lean base image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Set Python path (so `src/` works)
ENV PYTHONPATH=/app

# 4. Copy requirements first (cache optimisation)
COPY requirements.txt .

# 5. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy all project files
COPY . .

# 7. Expose FastAPI port
EXPOSE 8000

# 8. Run FastAPI app
CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]