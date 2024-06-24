# MIKA HWR Chatbot
## How to run the bot locally
### Prerequisites
- Make sure docker engine is installed. Check it with:
    ```bash
    docker --version
    ```
    If its not installed you can download it on the [Docker](https://docs.docker.com/engine/install/) website.

- Make sure NodeJs is installed. Check it with:
    ```bash
    node --version
    ```
    If its not installed you can download it on the [NodeJs](https://nodejs.org/en/download/prebuilt-installer) website.

- Make sure npm is installed. Check it with:
    ```bash
    npm --version
    ```
### Setup guide

1. Clone the [repositorys](https://github.com/hwr-chatbot) ```M.I.K.A.``` and ```Rasa-chatroom-react``` to your machine
2. Open your commandline and navigate to the ```M.I.K.A``` repository
3. Build the Dockerfile using
    ```bash
    docker build -t my-mika-image .
    ```
4. Run the Docker image using
    ```bash
    docker run -p 5005:5005 my-mika-image
    ```
5. Use your commandline and navigate to the ```Rasa-chatroom-react``` repository
6. Use the following command to start your frontend
    ```bash
    npm run dev
    ```
    By default the site is hostet on http://localhost:5173/

## Further commands for extended use
### RASA (Chatbot) starten: 
```bash
poetry run rasa run --enable-api --cors "" && rasa run actions --cors ""
```

### Model trainieren: 
```bash
poetry run rasa train
```
