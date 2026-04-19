FROM python:3.11-slim
WORKDIR /app
COPY image-resizer.py .
RUN pip install pillow
CMD ["python", "image-resizer.py"]
