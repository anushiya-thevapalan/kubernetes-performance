# Performance Testing in Kubernetes

## Deploy the Spring-boot application in Kubernetes

#### Build the Docker image
```bash
$ cd springboot-app/
$ docker build --no-cache -t anushiya/app:latest .
$ docker build --no-cache -t [dockerhub account name]/[name of the application]:[version number]
```

#### Push the Docker image to DockerHub
Note that the name of the application and the version number should be same as the one used to build the image above
```bash
$ docker push anushiya/app:latest
$ docker push [dockerhub account name]/[name of the application]:[version number]
```

#### Deploy the the application
```bash
cd deployment/app
kubectl apply -f app.yaml
kubectl apply -f [name of the deployment yaml]
```

