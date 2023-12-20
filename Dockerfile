FROM python:3.8-alpine3.10

# Add necessary repositories
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories

# Install dependencies
RUN apk update \
    && apk add chromium chromium-chromedriver libffi-dev build-base \
    && rm -rf /var/cache/apk/*

# Copy application files
COPY requirements.txt *.py /app/
WORKDIR /app

# Install Python packages
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install pytest-html

# Set environment variables
#ENV BASE_URL=$BASE_URL
#ENV USERNAME1=$USERNAME1
#ENV PASSWORD1=$PASSWORD1
#ENV INVALID_USERNAME=$INVALID_USERNAME
#ENV INVALID_PASSWORD=$INVALID_PASSWORD

# Run pytest when the container starts
CMD ["pytest", "--html=report.html"]
