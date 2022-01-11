FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PATH $PATH:/home/bookwyrm/.local/bin

RUN useradd -u 2000 -g users -d /home/bookwyrm -m bookwyrm
RUN install -d -o bookwyrm -g users -m 0755 /app /app/static /app/images

WORKDIR /app

USER bookwyrm
COPY requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir
