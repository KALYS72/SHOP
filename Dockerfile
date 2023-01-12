FROM ubuntu

WORKDIR /

COPY . .

RUN apt-get update
RUN apt-get install  -y apt-utils
RUN apt-get install -y python3-pip 
RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install -r req.txt


ENV SECRET_KEY=8x6t!7v4se%j-t7a@flk!ilac+1h86y^ow!3)%jkx321k29smq
ENV DB_NAME=railway
ENV DB_USER=postgres
ENV DB_PASSWORD=S74UFKt4qqEnjqXXBVvc
ENV DB_HOST=containers-us-west-70.railway.app
ENV DB_PORT=8000
ENV ALLOWED_HOSTS=127.0.0.1
# postgresql://postgres:S74UFKt4qqEnjqXXBVvc@containers-us-west-70.railway.app:5863/railway

RUN python3 manage.py migrate
RUN python3 manage.py collectstatic


CMD gunicorn --bind 0.0.0.0:8000 config.wsgi:application