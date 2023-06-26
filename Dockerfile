From python:latest
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN ls
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
