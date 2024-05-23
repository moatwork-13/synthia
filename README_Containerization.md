# Details

## Setup


```bash

apt install docker.io docker-compose-v2

cd synthia

docker compose build

source /root/.local/share/pypoetry/venv/bin/activate

comx key create mamout-test

echo "ANTHROPIC_API_KEY=YOUR_API_KEY" > anthropic_key.env

docker compose up nakamoto-miner-1

comx module register mamout-1 mamout-test --ip 194.163.148.58 --port 8080 --netuid 3  


```


## Old Setup

```bash

docker build -t nakamoto-miner -f Dockerfile . 

docker run -v ${PWD}:/app -v ~/.commune:/root/.commune -it -p 8080:8080 nakamoto-miner bash startup_script.sh


```