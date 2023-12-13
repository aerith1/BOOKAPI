FROM python:3.8.18
WORKDIR /book_api
COPY . /book_api
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]