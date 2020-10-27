#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import subprocess
import time

items = []

def collect_pg_streaming_stats():
    item = {}
    item["metric"] = "proc.pg.streaming.status"
    item["tagsMap"] = {
        "srv": "postgresql",
        "project": "ydy"
    }
    PG_STREAMING_INFO = subprocess.run(["/data/server/pgsql/bin/psql", "-h127.0.0.1", "-Upostgres", "-tc", \
                                        "select * from pg_stat_wal_receiver;"], stdout=subprocess.PIPE)
    try:
        PG_STREAMING_STATS = str(PG_STREAMING_INFO.stdout).split('|')[1].strip()
    except:
        # IndexError: list index out of range
        PG_STREAMING_STATS = None
    if PG_STREAMING_STATS == "streaming":
        item["value"] = 1
    else:
        item["value"] = 0
    items.append(item)

def main():
    timestamp = int(time.time())
    collect_pg_streaming_stats()

    for item in items:
        item["timestamp"] = timestamp

    print(json.dumps(items))


if __name__ == '__main__':
    main()

