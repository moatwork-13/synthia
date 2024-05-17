#!/bin/bash

activate () {
  echo "Activating virtual environment"
  . /root/.local/share/pypoetry/venv/bin/activate
  echo "Starting the server"
  which python
  which comx
  pm2 start "comx module serve synthia.miner.anthropic.AnthropicModule mamout-test --subnets-whitelist 3 --ip 0.0.0.0 --port 8080" --name nakamoto-mamout-1
  pm2 logs
}
# source /root/.local/share/pypoetry/venv/bin/activate

activate
