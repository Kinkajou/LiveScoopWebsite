NameVirtualHost *:80

<VirtualHost *:80>
    ServerAdmin manuel@kinkajougames.com
    ServerName livescoopapp.com
    WSGIScriptAlias / /usr/share/kinkajou/livescoop/website/confs/livescoop-ws.wsgi
    WSGIPassAuthorization On
    <Location "/static">
        SetHandler None
    </Location>
    <LocationMatch "\.(jpg|gif|png)$">
        SetHandler None
    </LocationMatch>
    Alias /static /var/www/livescoopws/static
</VirtualHost>

