FROM ubuntu:latest

WORKDIR /
RUN mkdir /photos
COPY generate-images.sh /
COPY flag /flag
RUN /generate-images.sh
RUN rm /flag
RUN chmod 000 -R /photos
RUN chmod 111 /photos
RUN useradd user

RUN apt update && apt -y install socat
USER user
CMD ["socat", "TCP-LISTEN:5555,reuseaddr,fork", "EXEC:/bin/bash,pty,stderr,setsid,sigint,sane,echo=0"]
