1. Create Docker image
```
docker build -t myimage ./
```

2. Run app in container
```
docker run -d -p 80:80 -e VARIABLE_NAME="api" myimage
```
This will run the app on http://localhost:8080/.

The base image used in the Dockerfile: https://github.com/tiangolo/uvicorn-gunicorn-starlette-docker