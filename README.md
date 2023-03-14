# xlwings Server: Hello World (Flask version)

This sample works with:

* Excel on Windows
* Excel on macOS
* Excel on the web
* Google Sheets


## Run the server locally

* Install the dependencies via `pip install -r requirements.txt`
* Run the server: `python app/main.py`

## Run the server with Docker

* You'll need to have a recent version of Docker
* Run `docker compose up` (this overrides `CMD` in the Dockerfile for local development)
* Whenever you change dependencies in `requirements.txt`, you'll need to rebuild the container via `docker compos build`
* To deploy the Dockerfile, it uses the `CMD` as specified in the Dockerfile

For more info, see the FastAPI implementation:

https://github.com/xlwings/xlwings-server-helloworld-fastapi
