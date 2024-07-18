FROM python:3.9-bullseye

# Set environment path
ENV PATH=$PATH:/root/.local/bin

# Install necessary packages
RUN apt update && apt upgrade -y && \
    apt install curl vim nano git -y

# Create and set working directory
RUN mkdir /mika
WORKDIR /mika

# Clone the repository
RUN git clone -b develop --single-branch https://github.com/hwr-chatbot/M.I.K.A..git .

# Install Poetry and project dependencies
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    poetry env use system && \
    poetry config virtualenvs.create false --local && \
    poetry install && \
    poetry run rasa telemetry disable

# Expose port 5005 for Rasa server
EXPOSE 5005
# Expose port 5055 for Actions server
EXPOSE 5055

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Use the entrypoint script to start both Rasa server and Actions server
CMD ["/entrypoint.sh"]
