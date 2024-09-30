# Test Flask app to fun and learn
It's just small pet project to learn Flask framework and to understend better RESTful API
## How to run it
- App uses **Poetry**
    - It's a tool for managing dependencies and project packaging
    - Currently I'm using it only for dependencies management, but in time, I hope, I would use packaging ability as well
    - To install it hit this command in the terminal:
        - `curl -sSL https://install.python-poetry.org | python3 -`
    - Then run the program:
        - `poetry run python server.py`
- Or you can run docker-container
    - `docker run docker.io/beaveru/flask-app-demo:2`

## Swagger docs
- To check app's API endpoinds you should run the program and reach `http://127.0.0.1:5000/apidocs`