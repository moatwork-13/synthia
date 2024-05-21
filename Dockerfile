FROM python:3.12.3-bullseye

RUN apt-get update && \
    apt-get install -y tmux npm curl libhdf5-dev && \
    npm install pm2@latest -g

SHELL ["/bin/bash", "-c"]

WORKDIR /app

COPY src /app/src
COPY pyproject.toml /app
COPY poetry.toml /app
COPY poetry.lock /app
COPY README.md /app

# Explicitly copy startup_script.sh to the container. Don't rely on file mounts. This will inheret the file
# permissions of the host system if it is mounted.
COPY startup_script.sh /app

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | bash -s -- -y && \
    curl -sSL https://install.python-poetry.org | python3 - -y

ENV PATH="/root/.cargo/bin:/root/.local/bin:${PATH}"

RUN /bin/bash -c "source /root/.cargo/env && poetry install"

# Mark the container copy of the start up script as executable.
RUN chmod +x /app/startup_script.sh

# Set the default command - doesn't matter, the compose file will override this.
CMD ["/bin/bash", "-c", "sleep infinity"]
