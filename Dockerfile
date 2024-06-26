FROM python:3.9-bullseye
ENV PATH = $PATH:/root/.local/bin
RUN apt update && apt upgrade -y
RUN apt install curl vim nano git -y
RUN mkdir mika
WORKDIR /mika
RUN git clone -b develop --single-branch https://github.com/hwr-chatbot/M.I.K.A..git .
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry env use system
RUN poetry config virtualenvs.create false --local
RUN poetry install
RUN poetry run rasa telemetry disable
# RUN poetry run rasa train
EXPOSE 5005
CMD poetry run rasa run --enable-api --cors "*" --model /mika/models/20240625-135354-black-road.tar.gz && rasa run actions --cors "*"
