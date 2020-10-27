# n9e自定义插件脚本，采集postgresql流复制状态实例

postgresql采集流复制状态

## 1.插件名称：pgsql_collect_streaming_status.py

插件脚本内容如下：

```python
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
```

## 2.插件脚本部署在需要被采集的服务器（n9e的agent）上

插件的完整路径：`/opt/n9e_plugin/pgsql_collect_streaming_status.py`

```bash
[root@ecs-ydy-db-002 n9e_plugin]# ll
total 8
-rwxr-xr-x 1 root root 1017 Oct 27 17:34 pgsql_collect_streaming_status.py
-rwxr-xr-x 1 root root 1016 Oct 27 17:39 pgsql_collect_streaming_status_test.py
[root@ecs-ydy-db-002 n9e_plugin]# pwd
/opt/n9e_plugin

# 如果插件采集报错，将会在这个日志下显示错误信息
[root@ecs-ydy-db-002 n9e_plugin]# tail -f /opt/n9e/logs/agent/ERROR.log
2020-10-27 17:33:28.534923 ERROR plugins/scheduler.go:97 exec /opt/n9e_plugin/pgsql_collect_streaming_status.py fail: Traceback (most recent call last):
  File "/opt/n9e_plugin/pgsql_collect_streaming_status.py", line 41, in <module>
    main()
  File "/opt/n9e_plugin/pgsql_collect_streaming_status.py", line 32, in main
    collect_pg_streaming_stats()
  File "/opt/n9e_plugin/pgsql_collect_streaming_status.py", line 18, in collect_pg_streaming_stats
    "select * from pg_stat_wal_receiver;"], stdout=subprocess.PIPE)
  File "/usr/lib64/python3.6/subprocess.py", line 423, in run
    with Popen(*popenargs, **kwargs) as process:
  File "/usr/lib64/python3.6/subprocess.py", line 729, in __init__
    restore_signals, start_new_session)
  File "/usr/lib64/python3.6/subprocess.py", line 1364, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'psql': 'psql'
```

## 3.在n9e的“采集配置”中，创建插件采集

![](https://github.com/kongzi68/pgsql_collect_streaming_status/blob/main/%E6%8F%92%E4%BB%B6%E9%87%87%E9%9B%86%E9%85%8D%E7%BD%AE.jpg)

## 4.收到的邮件报警信息

![](https://github.com/kongzi68/pgsql_collect_streaming_status/blob/main/874afc35-f385-40a3-b154-68d6097de09d.png)
