FROM python:3.10-slim

RUN pip install --no-cache-dir rembg[cpu] flask pillow

RUN python -c "from rembg import new_session; new_session('u2net')"

COPY server.py /app/server.py
WORKDIR /app
EXPOSE 5000
CMD ["python", "server.py"]