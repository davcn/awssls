FROM node:latest

# install yarn
RUN curl -o- -L https://yarnpkg.com/install.sh | bash

# install python tooling
RUN apt-get update -y && apt-get install -y python-dev python-pip && pip install --upgrade pip
RUN pip install -U setuptools
RUN pip install pytest boto3 moto pyopenssl

# install serverless
RUN npm install -g serverless

