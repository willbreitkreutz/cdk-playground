FROM ubuntu:22.04

ARG AWS_CDK_VERSION=2.74.0

RUN useradd cdk

RUN mkdir -p /home/cdk/app && chown -R cdk:cdk /home/cdk

ENV HOME=/home/cdk

COPY ./requirements.txt /home/cdk/

WORKDIR /home/cdk

RUN apt-get update && apt-get install -y \
curl python3-pip python3-venv git unzip \
&& curl -fsSL https://deb.nodesource.com/setup_19.x | bash - \
&& apt-get install -y nodejs \
&& npm install -g aws-cdk-local aws-cdk@${AWS_CDK_VERSION} \
&& curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip \
&& unzip awscliv2.zip && ./aws/install && rm awscliv2.zip \
&& pip3 install -r requirements.txt \
&& rm -rf /var/lib/apt/lists/* \
&& chown -R cdk:cdk /home/cdk

USER cdk

# ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD chown -R cdk:cdk /home/cdk && tail -f /dev/null