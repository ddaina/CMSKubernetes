#!/bin/bash

currentHost=`hostname`
targetHost='crab-preprod-tw0'

if [[ "$currentHost" == *"$targetHost"* ]] && [ "$SERVICE" == "TaskManager" ] && [ -f /data/srv/cfg/filebeat.yaml ] && [ -f /usr/bin/filebeat ]; then
    ldir=/tmp/filebeat
    mkdir -p $ldir/data
    nohup /usr/bin/filebeat \
        -c /data/srv/cfg/filebeat.yaml \
        --path.data $ldir/data --path.logs $ldir -e 2>&1 1>& $ldir/log < /dev/null &
fi
