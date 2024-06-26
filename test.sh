#!/bin/bash
# Runs the NetBox plugin unit tests

# exit when a command exits with an exit code != 0
set -e

# The docker compose command to use
doco="docker compose --file docker-compose.yml"

test_netbox_unit_tests() {
  echo "⏱  Running NetBox Unit Tests"
  $doco run --rm netbox python manage.py makemigrations netbox_vrf_ext --check
  $doco run --rm netbox python manage.py test netbox_vrf_ext -v 2
}

test_cleanup() {
  echo "💣  Cleaning Up"
  $doco down -v
  $doco rm -fsv
  docker image rm docker.io/library/netbox-vrf-ext-netbox || echo ''
}

echo "🐳🐳🐳  Start testing"

# Make sure the cleanup script is executed
trap test_cleanup EXIT ERR
test_netbox_unit_tests

echo "🐳🐳🐳  Done testing"