# Details

## Setup

<!-- │ public_key   │ b2d6f6e811366761330ecc283619d5795ef4c9e456e06d7f068c1665c371fe1e │
 -->

```bash

apt install docker.io docker-compose-v2

cd synthia

docker compose build

source /root/.local/share/pypoetry/venv/bin/activate

comx key create mamout-test


docker compose up nakamoto-miner-1


comx module register mamout-1 mamout-test --ip 194.163.148.58 --port 8080 --netuid 3  


```


## Old Setup

```bash

docker build -t nakamoto-miner -f Dockerfile . 

docker run -v ${PWD}:/app -v ~/.commune:/root/.commune -it -p 8080:8080 nakamoto-miner bash startup_script.sh


```