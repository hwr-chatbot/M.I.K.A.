#!/bin/bash

# Start Rasa server in the background
poetry run rasa run --enable-api --cors "*" &

# Start Actions server
poetry run rasa run actions --cors "*"
