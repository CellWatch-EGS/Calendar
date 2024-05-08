FROM python:3.8-alpine

WORKDIR /calendar_app

COPY . /calendar_app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV APP_NAME="CalendarService"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]