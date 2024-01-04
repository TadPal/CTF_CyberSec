# Web crawling
1. Folder hidden from crawlers -> /robots.txt
2. /test
3. 
```bash 
wget https://kybersoutez.cz/test/flag.pdf
```
4. 
```bash
pdf2john flag.pdf > hash
```
5. Create worlidst from website
```bash
cewl -w wordlist.txt -d 2 -m 5 https://kybersoutez.cz
```
6. Bruteforce the PDF
```bash
john --wordlist=./Crypto/CyberComp2024/WebCrawling/wordlist.txt ./Crypto/CyberComp2024/WebCrawling/hash
```
7. Open PDF