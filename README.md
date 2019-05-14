# Grow only CRDT counter

This is a demonstration of [Grow Only CRDT](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type#G-Counter_(Grow-only_Counter)) counter.
Implementation of counter only has increment and merge methods
for the sake of simplicity and other methods may require more
code to write and effort towards reconciliation of conflicts etc.

## Communication between nodes

Communication between nodes relies on Redis and 2 parallel workers in each
node first responsible to broadcast updates every 2 seconds, second
is responsible to expect updates and merge current state of the node
with the incoming state.

## How number of nodes affect counter?

Since implementation is abstract and does not rely on exact amount of nodes
we can be sure that eventually all view counts will be the same on all nodes.

## Prerequisites
Project requires Docker, [Pipenv](https://docs.pipenv.org), `docker-compose` to present in your development environment.

## How to run and stop?

### Start
```sh
$ scripts/run
```

### Stop
```sh
$ scripts/stop
```

If you want to change the number of running services then you can set

```sh
export REPLICAS=N
```

Then run the script again.

## Docker-compose setup

Compose file uses `haproxy` to load-balance to `web` service nodes.

**NOTE**: `haproxy` works with default configuration.

## How to access counter

To access counter please open http://127.0.0.1/my-video

## Validation

To validate if counters work properly you need to have `ab`
and [jq](https://stedolan.github.io/jq/) cli utilities installed. Once everything in place you can call.

**NOTE**: make sure you started the application using `scripts/run`

```sh
$ tests/validate.sh
```

## Running tests

First install dev dependencies or pytest

```sh
$ pipenv install --dev
OR
$ pip install pytest
```

Then run

```sh
$ pytest
```
