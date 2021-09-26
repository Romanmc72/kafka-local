#!/usr/bin/env bash

set -euo pipefail

main() {
    docker-compose up -d --build
}

main
