#!/bin/bash


activate () {
  echo "Starting the server on port ${PORT}"
  echo "Anthropic key: ${ANTHROPIC_API_KEY}"
  poetry run which python
  poetry run which comx
  poetry run pm2 start "comx module serve synthia.miner.anthropic.AnthropicModule mamout-test --subnets-whitelist 3 --ip 0.0.0.0 --port ${PORT}" --name nakamoto-mamout-1
  poetry run pm2 logs
}

activate