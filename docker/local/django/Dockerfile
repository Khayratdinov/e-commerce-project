FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/app
# copy project
COPY . .


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN python3 -m pip install --no-cache-dir --no-warn-script-location --upgrade pip \
    && python3 -m pip install --no-cache-dir --no-warn-script-location --user -r requirements/development.txt

# copy entrypoint.sh
COPY ./scripts/entrypoint.sh /usr/src/app/
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# entrypoint.sh will be discussed later.
CMD [ "/usr/src/app/entrypoint.sh" ]

