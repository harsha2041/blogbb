FROM python:3.6
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN chmod 755 manage.py
CMD ["python", "manage.py"]