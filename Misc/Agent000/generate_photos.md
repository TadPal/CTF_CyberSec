# Chmod 000

1. Docker file says that chmod 111 was actually run
2. We can read the generate_photos.sh
```bash
flag="$(cat flag)"

for (( i=0; i<${#flag}; i++ )); do
        size=$(printf "%d" "'${flag:$i:1}")
        for (( j=0; j < $size; j++ )); do
                printf "%s" "${flag:$i:1}" >> photos/$i
        done
done
```
The script copies the flag and makes a file named 0-N for each letter in the flag. It also writes as many character in to the file as is the value of the character in ASCII.

3. You cannot read the contents of photos but you can access it. And since we know the files are named "0-N" we can check their size with 
```bash
stat -c %s NAME_OF_FILE
``` 
