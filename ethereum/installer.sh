#!/usr/bin/env bash

function prepare() {
    sudo apt-get update
    sudo apt-get upgrade -y
}

function install() {
    sudo apt-get install -y software-properties-common
    sudo add-apt-repository -y ppa:ethereum/ethereum
    sudo apt-get update
    sudo apt-get install -y ethereum
}


prepare
install
