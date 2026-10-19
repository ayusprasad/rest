FROM python:3.11-alpine

WORKDIR /app

ENV PORT=8080

COPY . .

EXPOSE 8080

CMD ["python", "serve_report.py"]
