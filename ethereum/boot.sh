#!/usr/bin/env bash

if [[ $1="--init" ]]; then
    geth --datadir /home/ubuntu/rb_geth init /home/ubuntu/rb_geth/myGenesis.json
fi

geth --networkid "10" --nodiscover --datadir "/home/ubuntu/rb_geth" console 2>> /home/ubuntu/rb_geth/geth_err.log
