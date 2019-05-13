# Grow only CRDT counter

This is a demonstration of [Grow Only CRDT](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type#G-Counter_(Grow-only_Counter)) counter.
Implementation of counter only has increment and merge methods
for the sake of simplicity and other methods may require more
code to write and effort towards reconciliation of conflicts etc.


## Prerequisites
Project requires Docker to present in your development environment.


## How to run?

```sh
$ scripts/run
```

If you want to change the number of running services then you can set

```sh
export REPLICAS=N
```

Then run the script again.

## Docker-compose setup

Compose file uses `haproxy` to load-balance to `web` service nodes.
