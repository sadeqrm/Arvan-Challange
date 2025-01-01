# Arvan-Challange

I was asked from Arvan Team to bring up a challange request and I am so happy to make it ready last week.
The scenario is divided into some parts which I have to solve them.
1.Infra(IaC) 2.k8s Cluster(Ansible)  3.Postgres Cluster Setup 5.Deploying python app in k8s 6.Monitoring

# Project Overview

This project involves setting up a production-ready Kubernetes environment and deploying a Python application with a series of automated and orchestrated steps. Below is an outline of the workflow and key components involved:

## Table of Contents
1. [Preparing Infrastructure](#1-preparing-infrastructure)
2. [Provisioning Virtual Machines](#2-provisioning-virtual-machines)
3. [Setting up a Kubernetes Cluster](#3-setting-up-a-kubernetes-cluster)
4. [Deploying PostgreSQL Cluster](#4-deploying-postgresql-cluster)
5. [Deploying the Python Project](#5-deploying-the-python-project)

---

## 1. Preparing Infrastructure

The first step involves setting up the foundational infrastructure:
- **Tools Used**: VMware Workstation, vSphere vCenter, ESXi.
- **Process**:
  1. Install and configure VMware Workstation.
  2. Deploy vSphere vCenter on VMware Workstation.
     * IP : 10.10.49.152
       
       ![image](https://github.com/user-attachments/assets/af2e5df3-a806-427f-aec3-2f93596cbbf9)

  4. Add one ESXi host to vCenter to serve as the hypervisor.
     * IP : 10.10.49.153

---

## 2. Provisioning Virtual Machines

Using Terraform to automate the creation of virtual machines:
Path : IaC-Terraform-ArvanChallange
- **Tools Used**: Terraform.
- **Process**:
 Write Terraform configurations to define and provision three virtual machines in vCenter then execute Terraform commands to apply the configurations and create the VMs.

  * SSH to 192.168.13.36 :
  
  ![image](https://github.com/user-attachments/assets/30226871-0f94-40e7-9c8f-b35810a69c65)

  1. Go to specific path :
  `cd /opt/IaC-Terraform-ArvanChallange`

  2. Initializing a working directory containing Terraform configuration files :
  `terraform init`

  3.  Creating an execution plan in Terraform :
   `terraform plan`

  4. Applying changes to my infrastructure :
  `terraform apply`

---

## 3. Setting up a Kubernetes Cluster ![image](https://github.com/user-attachments/assets/af8ec33a-fb05-4a28-95b7-417f029dec8f)


Setting up a three-node production-ready Kubernetes cluster:
Path : Arvan
- **Tools Used**: Ansible(Kubespray Method)
- **Process**:
  1. Use Ansible for automated setup and configuration.
  2. Leverage Kubespray for deploying the Kubernetes cluster on the provisioned VMs.
  3. Ensure the cluster is production-ready with necessary configurations.
     All files related to my configuration is in Arvan folder.
  * SSH to Master 10.10.49.154
  
 `git clone https://github.com/kubernetes-sigs/kubespray.git`
 
 `cd kubespray`
 
 `cd inventory/Arvan/`

Copy environment variable files for custom installation:
  `# Copy inventory/sample as inventory/MeCan`
   `cp -rfp inventory/sample inventory/Arvan`

Tuning group_vars/all/all.yml.
Tuning group_vars/all/containerd.yml.
Tuning group_vars/all/etcd.yml.
Tuning group_vars/k8s_cluster/addons.yml.
Tuning group_vars/k8s_cluster/k8s-cluster.yml.
Tuning group_vars/k8s_cluster/k8s-net-calico.yml.

In the last command we execute our ansible-playbook command to make our cluster up :
  `ansible-playbook -i inventory/MeCan/hosts.yaml  --become --become-user=root cluster.yml`

Issue bellow commands to verify our cluster : 

  `kubectl get nodes`
  
  ![image](https://github.com/user-attachments/assets/773f9757-fd20-4544-88ff-31a61750da4a)
  
  `kubectl top nodes`
  
  ![image](https://github.com/user-attachments/assets/374e468b-a264-4a4d-bd4d-3741a723a004)

---

## 4. Deploying PostgreSQL Cluster

Deploying a PostgreSQL database cluster on Kubernetes:

For this purpose I read an article from DigitalOcean which i put it's link bellow here.

  https://www.digitalocean.com/community/tutorials/how-to-deploy-postgres-to-kubernetes-cluster

Path : k8s/postgres
- **Tools Used**: Kubernetes (kubectl, Helm, or manifests).
- **Process**:
  1. Create Kubernetes manifests or Helm charts for PostgreSQL.
  2. Apply the configuration to deploy the PostgreSQL cluster.
  3. Verify the deployment and ensure high availability.

    ![image](https://github.com/user-attachments/assets/f5418fb1-ea11-433d-b76d-66010fbfc618)

    ![image](https://github.com/user-attachments/assets/b7475bb2-84f2-408c-b2fe-d9331c9aab7c)

    ![image](https://github.com/user-attachments/assets/07c9a916-2472-4adc-b95d-5427d1804ea4)


---

## 5. Deploying the Python Project

Automating the deployment of the Python application:
Path: Docker-Project
- **Tools Used**: Docker, Nexus Artifactory, GitOps, ArgoCD.
- **Process**:
  1. Build a Docker image for the Python project.
  2. Push the Docker image to a Nexus Artifactory repository.
     
     * ![image](https://github.com/user-attachments/assets/0f67c868-8c1f-4dbf-91b6-7ab420359b3b)

  4. Create Kubernetes manifests for the application.
     * Path : manifest
  6. Use GitOps principles with ArgoCD to deploy the application to the Kubernetes cluster.
     * First: connect gihub repo to ArgoCD.
       
       ![image](https://github.com/user-attachments/assets/b02a17b9-b02d-485a-b8b6-373c58bd106e)

     * Second: create application in ArgoCD.
       
       ![image](https://github.com/user-attachments/assets/803e4431-da16-4741-af16-c79b05331e19)

  8. Monitor and verify the deployment.
  9. 
       ![image](https://github.com/user-attachments/assets/a26b7c76-d45e-4076-82f3-89107d74385c)

---

## Prerequisites

- VMware Workstation with required resources.
- Terraform installed and configured.
- Ansible installed and configured.
- Access to Nexus Artifactory.
- Git repository for the Python project.
- ArgoCD installed and configured in the Kubernetes cluster.

---

## How to Run

1. Follow the instructions in [Preparing Infrastructure](#1-preparing-infrastructure) to set up the base environment.
2. Use Terraform configurations to provision the VMs as described in [Provisioning Virtual Machines](#2-provisioning-virtual-machines).
3. Deploy the Kubernetes cluster following the steps in [Setting up a Kubernetes Cluster](#3-setting-up-a-kubernetes-cluster).
4. Deploy PostgreSQL as described in [Deploying PostgreSQL Cluster](#4-deploying-postgresql-cluster).
5. Build, push, and deploy the Python application following the steps in [Deploying the Python Project](#5-deploying-the-python-project).

---

## Additional Notes

- Ensure all tools and dependencies are pre-installed before beginning.
- Configure firewalls, networking, and storage to meet the requirements of a production-ready setup.
- Use monitoring tools like Prometheus and Grafana to oversee cluster health.
- Test and validate each step before moving to the next.


