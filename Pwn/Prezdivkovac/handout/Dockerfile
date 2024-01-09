FROM ubuntu:22.04

EXPOSE 9999

RUN apt update
RUN apt install -y socat gcc make
COPY ./chall.c /opt/chall.c
COPY ./Makefile /opt/Makefile
WORKDIR /opt
RUN make
RUN chmod -R a+rX /opt

ENTRYPOINT ["socat", "-T30", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:./chall"]
#ENTRYPOINT ["socat", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:./chall"]
