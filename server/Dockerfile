FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY fastmcp.py .

EXPOSE 3000

CMD ["python", "fastmcp.py"]