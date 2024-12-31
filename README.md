# Arvan-Challange

I was asked from Arvan Team to resolve up a challange and I am so happy to make it ready last week

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

    

---

## 4. Deploying PostgreSQL Cluster

Deploying a PostgreSQL database cluster on Kubernetes:
- **Tools Used**: Kubernetes (kubectl, Helm, or manifests).
- **Process**:
  1. Create Kubernetes manifests or Helm charts for PostgreSQL.
  2. Apply the configuration to deploy the PostgreSQL cluster.
  3. Verify the deployment and ensure high availability.

---

## 5. Deploying the Python Project

Automating the deployment of the Python application:
- **Tools Used**: Docker, Nexus Artifactory, GitOps, ArgoCD.
- **Process**:
  1. Build a Docker image for the Python project.
  2. Push the Docker image to a Nexus Artifactory repository.
  3. Create Kubernetes manifests for the application.
  4. Use GitOps principles with ArgoCD to deploy the application to the Kubernetes cluster.
  5. Monitor and verify the deployment.

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


