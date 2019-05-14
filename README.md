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
Project requires Docker to present in your development environment.


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

## Validation

To validate if counters work properly you need to have `ab` cli utility installed.
Once everything in place you can call

```sh
$ tests/validate.sh
```
