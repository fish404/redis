from sshtunnel import SSHTunnelForwarder
from redis import Redis

with SSHTunnelForwarder(
    ssh_address_or_host = 'xxx.xxx.xxx',  # 本机能够访问的跳板机A 的ip

    ssh_username = 'username',  # 本机能够访问的跳板机A 的账号

    ssh_password = 'passwd',  # 本机能够访问的跳板机A 的密码

    remote_bind_address=('yyy.yyy.yyy.yy', port)  # 需要访问的目的ip，不能直接访问
) as server:

    server.start()
    r = Redis(host='127.0.0.1', port=server.local_bind_port, password='passwd_of_reids', decode_responses=True)
    a = r.get('test_key')
    print(a)
    count = 0
    for key in r.scan_iter("user*"):
        # sex, name, nick= r.hmget(key,'sex','head','nick')
        b = r.hgetall(key)
        # print(key, b)
        if b['head'] == '':
            print(b)
            count += 1
    print('游客数量 ', count) 
