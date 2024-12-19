# Airflow Kubernetes

This repository contains a template of how to deploy Apache Airflow on Kubernetes using Helm,
and a simple DAG to demonstrate the setup.

## Setup
### Kubernetes
You need a Kubernetes cluster to deploy Airflow. You can use Minikube, Docker Desktop, or any other Kubernetes cluster. 
The examples here are using [Kind](https://kind.sigs.k8s.io/).
> Note: all the commands below are for macOS. If you are using a different OS, please refer to the official documentation.
##### Install Kind
```shell
brew install kind
```
##### Create a Kubernetes cluster
```shell
kind create cluster --name apache-airflow
```
### Helm
You need Helm to deploy Airflow. If you don't have Helm installed, you can install it using the following command:
```shell
brew install helm
```
### Kubectl
You need Kubectl to interact with your Kubernetes cluster. If you don't have Kubectl installed, you can install it using the following command:
```shell
brew install kubectl
```

## Deploy Airflow
### Add the Airflow Helm repository
```shell
helm repo add apache-airflow https://airflow.apache.org
```
### Deploy Airflow
```shell
helm upgrade --install airflow apache-airflow/airflow --namespace airflow --values helm/values.yaml
```

## Access Airflow
### Port-forward the Airflow webserver
```shell
kubectl port-forward svc/airflow-webserver 8080:8080 --namespace airflow
```
### Access Airflow UI
Open your browser and go to [http://localhost:8080](http://localhost:8080). The default username and password are `admin`.

