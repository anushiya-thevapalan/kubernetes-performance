# kubernetes-performance

## Deploy the Spring-boot application in Kubernetes

#### Build the Docker image
```bash
cd springboot-app/
docker build --no-cache -t anushiya/app:latest .
docker build --no-cache -t [dockerhub account name]/[name of the application]:[version number]
```

#### Push the Docker image to DockerHub
```bash
docker push anushiya/app:latest
```

#### Deploy the the application
```bash
cd deployment/app
kubectl apply -f app.yaml
kubectl apply -f [name of the deployment yaml]
```

