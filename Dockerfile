FROM python:3.8-slim
RUN apt-get update
RUN pip install selenium
RUN pip install dotenv
RUn apt-get install -y wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb
COPY src/ .

ENTRYPOINT python main.py

