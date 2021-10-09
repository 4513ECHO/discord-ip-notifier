FROM alpine:latest
COPY . /opt/app/
RUN echo '0 * * * * cd /opt/app; python3 main.py' > /var/spool/cron/crontabs/root
CMD ["crond", "-f"]

