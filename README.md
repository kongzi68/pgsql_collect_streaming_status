# n9e自定义插件脚本，采集postgresql流复制状态实例

postgresql采集流复制状态

## 1.插件名称：pgsql_collect_streaming_status.py

插件脚本内容如下：略，见文件“pgsql_collect_streaming_status.py”

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
