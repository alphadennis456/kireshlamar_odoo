FROM odoo:16.0

# Copy custom addons
COPY ./custom_addons /mnt/extra-addons

ENV DB_HOST=dpg-d26k3c95pdvs73a7ciug-a.frankfurt-postgres.render.com \
    DB_PORT=5432 \
    DB_USER=kireshlamar_db_user \
    DB_PASSWORD=4iNX6hXHTUsdjeoTDTQcgOFrd8WCSLW4 \
    DB_NAME=kireshlamar_db

EXPOSE 8069

CMD ["odoo", "-c", "/etc/odoo/odoo.conf", "--addons-path=/mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons"]