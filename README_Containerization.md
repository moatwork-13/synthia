# Details

## Setup

<!-- │ public_key   │ b2d6f6e811366761330ecc283619d5795ef4c9e456e06d7f068c1665c371fe1e │
 -->

```bash
comx key create mamout-test

cd synthia

docker build -t nakamoto-miner -f Dockerfile . 

docker run -v ${PWD}:/app -v ~/.commune:/root/.commune -it -p 8080:8080 nakamoto-miner bash startup_script.sh


```