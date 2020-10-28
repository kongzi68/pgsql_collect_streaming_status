#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import subprocess
import time

items = []

def collect_pg_streaming_status():
    item = {}
    item["metric"] = "proc.pg.streaming.status"
    item["tagsMap"] = {
        "srv": "postgresql",
        "project": "ydy"
    }
    pg_streaming_info = subprocess.run(["/data/server/pgsql/bin/psql", "-h127.0.0.1", "-Upostgres", "-tc", \
                                        "select * from pg_stat_wal_receiver;"], stdout=subprocess.PIPE)
    try:
        pg_streaming_status = str(pg_streaming_info.stdout).split('|')[1].strip()
    except:
        # IndexError: list index out of range
        pg_streaming_status = None
    if pg_streaming_status == "streaming":
        item["value"] = 1
    else:
        item["value"] = 0
    items.append(item)

def main():
    timestamp = int(time.time())
    collect_pg_streaming_status()

    for item in items:
        item["timestamp"] = timestamp

    print(json.dumps(items))


if __name__ == '__main__':
    main()
