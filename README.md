TCPWrappers
=========

Manages entries in `/etc/hosts.allow` and `/etc/hosts.deny` which are used by TCP Wrappers to limit connections to daemons that utilise the `libwrap` library.

Requirements
------------

None

Role Variables
--------------

**tcpwrappers_allow_all_connections**: Boolean whether you want to permit all connection from all hosts.
**tcpwrappers_deny_all_connections**: Boolean whether you want to refuse all connection from all hosts.
**tcpwrappers_allows**: A list of allowed connection. If you turned tcpwrappers_allow_all_connections on, this list would be ignored.

**tcpwrappers_denys**: A list of denied connection. If you turned tcpwrappers_deny_all_connections on, this list would be ignored.

* daemon - A name of daemon you want to allow or deny.
* clients - A list of hosts.

Dependencies
------------

None

Example Playbook
----------------
```
- hosts: all
  vars:
    tcpwrappers_allow_all_connections: false
    tcpwrappers_deny_all_connections: true
    tcpwrappers_allows:
      - daemon: 'sshd'
        clients: [ 'ALL' ]
        comment: 'Allow all on SSH'
    tcpwrappers_denys: []

  roles:
    - role: ivoamorim.tcpwrappers
```

License
-------

BSD
