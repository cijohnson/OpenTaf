import string

template = string.Template("""
[DEFAULT]
root=$__opentaf_root__
testbed=$__opentaf_testbed__

[PUBLISH]
host=$__test_result_server_ip__
port=$__test_result_server_port__

[SCHEDULER]
host=$__testbed_scheduler_ip__
port=$__testbed_scheduler__port__
""")
