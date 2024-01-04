# Easy forensics

1. Check out /var/log
2. File messages
~~~bash
Oct 10 14:36:14 controller1 auth.info sshd[4892]: Connection closed by invalid user user 192.168.152.151 port 33246 [preauth]
Oct 10 14:36:14 controller1 auth.info sshd[4889]: Invalid user support from 192.168.152.151 port 33238
Oct 10 14:36:14 controller1 auth.info sshd[4893]: Invalid user supervisor from 192.168.152.151 port 33248
Oct 10 14:36:14 controller1 auth.info sshd[4890]: Invalid user ubnt from 192.168.152.151 port 33240
Oct 10 14:36:14 controller1 auth.info sshd[4893]: Failed password for invalid user supervisor from 192.168.152.151 port 33248 ssh2
Oct 10 14:36:14 controller1 auth.info sshd[4889]: Failed password for invalid user support from 192.168.152.151 port 33238 ssh2
Oct 10 14:36:14 controller1 auth.info sshd[4890]: Failed password for invalid user ubnt from 192.168.152.151 port 33240 ssh2
Oct 10 14:36:14 controller1 auth.info sshd[4889]: Connection closed by invalid user support 192.168.152.151 port 33238 [preauth]
Oct 10 14:36:14 controller1 auth.info sshd[4890]: Connection closed by invalid user ubnt 192.168.152.151 port 33240 [preauth]
Oct 10 14:36:14 controller1 auth.info sshd[4893]: Connection closed by invalid user supervisor 192.168.152.151 port 33248 [preauth]
Oct 10 14:48:30 controller1 auth.info sshd[4910]: Accepted password for admin from 192.168.152.151 port 33258 ssh2
~~~
3. Admin compormised
4. Check out /home/admin
5. See minerd app and nohup.out file
6. Lookup minerd online