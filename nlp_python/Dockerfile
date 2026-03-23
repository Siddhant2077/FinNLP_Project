FROM python:3.10-slim

WORKDIR /app

# Copy requirements from the context root
COPY nlp_python/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole folder so it exists as /app/nlp_python
COPY nlp_python/ /app/nlp_python/

# Ensure it's treated as a package
RUN touch /app/nlp_python/__init__.py

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

EXPOSE 5000

# Run as a module so absolute imports work
CMD ["python", "-m", "nlp_python.api.app"]