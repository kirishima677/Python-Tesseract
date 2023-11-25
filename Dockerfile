FROM ubuntu:22.04

# Update package lists and install necessary dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y software-properties-common python3 python3-pip vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add Tesseract PPA, update, and install Tesseract
RUN add-apt-repository ppa:alex-p/tesseract-ocr5 && \
    apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev tesseract-ocr-jpn

RUN pip3 install --upgrade pip && \
    pip3 install pillow && \
    pip3 install pyocr && \
    pip3 install pytesseract

# Set the working directory to /app and create it if not exists
WORKDIR /app

# Link the local 'app' folder with the container's '/app' folder
COPY ./app /app
