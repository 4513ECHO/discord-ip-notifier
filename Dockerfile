FROM alpine:latest
RUN apk --no-cache add python3
COPY . /opt/app/
RUN echo '0 * * * * cd /opt/app; python3 main.py' > /var/spool/cron/crontabs/root
CMD ["crond", "-f"]

