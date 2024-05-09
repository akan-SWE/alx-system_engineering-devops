# 0x08. Networking basics #1

Implementations for the project.

# Table of contents
    
- [Task 0](#Task0)
- [Task 1](#Task1)
- [Task 2](#Task2)


## Task0

### Subject: Change your home IP

This script configures an Ubuntu server with the below requirements;

- [ ] localhost resolves to 127.0.0.2

- [ ] facebook.com** resolves to 8.8.8.8

- [ ] The checker is running on Docker.
    

### Example:

```sh 
    sylvain@ubuntu$ ping localhost
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.012 ms
^C
--- localhost ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.012/0.012/0.012/0.000 ms
sylvain@ubuntu$
sylvain@ubuntu$ ping facebook.com
PING facebook.com (157.240.11.35) 56(84) bytes of data.
64 bytes from edge-star-mini-shv-02-lax3.facebook.com (157.240.11.35): icmp_seq=1 ttl=63 time=15.4 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 15.432/15.432/15.432/0.000 ms
sylvain@ubuntu$
sylvain@ubuntu$ sudo ./0-change_your_home_IP
sylvain@ubuntu$
sylvain@ubuntu$ ping localhost
PING localhost (127.0.0.2) 56(84) bytes of data.
64 bytes from localhost (127.0.0.2): icmp_seq=1 ttl=64 time=0.012 ms
64 bytes from localhost (127.0.0.2): icmp_seq=2 ttl=64 time=0.036 ms
^C
--- localhost ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 0.012/0.024/0.036/0.012 ms
sylvain@ubuntu$
sylvain@ubuntu$ ping facebook.com
PING facebook.com (8.8.8.8) 56(84) bytes of data.
64 bytes from facebook.com (8.8.8.8): icmp_seq=1 ttl=63 time=8.06 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 8.065/8.065/8.065/0.000 ms
```

### File: 0-change_your_home_IP

## Task1

### Subject: Show attaced IPs

This bash script displays all active IPv4 IPs on the machine it's executed on.

### Example:

``` sh
sylvain@ubuntu$ ./1-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$
sylvain@ubuntu$
```
#### File: 1-show_attached_IPs

## Task2

### Subject: Port listening on localhost
This bash script listens on port 98 on localhost.

### Example:

#### Terminal 0

Starting my script.

``` sh
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
```


##### Terminal 1

Connecting to localhost on port 98 using telnet and typing some text.

``` sh
sylvain@ubuntu$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is '^]'.
Hello world
test
```

##### Terminal 0

Receiving the text on the other side.

``` sh
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
Hello world
test
```

    

