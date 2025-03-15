FROM apache/airflow:2.10.5

USER root

RUN sudo apt-get update && sudo apt-get install -y gnupg software-properties-common
RUN sudo apt-get install wget
RUN wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null
RUN gpg --no-default-keyring \
--keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
--fingerprint
RUN echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list
RUN sudo apt update
RUN echo Y | sudo apt-get install terraform

