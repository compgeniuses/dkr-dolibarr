FROM python:3.11

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python-on-whales download-cli

# install buildx
RUN mkdir -p ~/.docker/cli-plugins/
RUN wget https://github.com/docker/buildx/releases/download/v0.6.3/buildx-v0.6.3.linux-amd64 -O ~/.docker/cli-plugins/docker-buildx
RUN chmod a+x  ~/.docker/cli-plugins/docker-buildx

RUN echo -e '{\n  \"experimental\": \"enabled\"\n}' | tee ~/.docker/config.json