# Kerstdorp muziek nieuwe opzet

Python applicatie kerstdorp.py is een service aangemaakt. De naam van deze service heet bigben.service.
Indien een applicatie als service functioneerd dan dient workpad in python applicatiie toegevoegd worden. Variable WORK_DIR wordt hiervoor gebuikt.
Verder aandacht voor aplay deze werkt ook anders als service. De volgende optie extra toegevoegd:
- aplay -D hw:2,0 (geeft aan dat hoofdtelefoon uitgang gebruikt dient te worden)

## Service aanmaken/onderhouden

- De service kan met volgende commando bewerkt worden<br>
sudo nano /etc/systemd/system/bigben.service

- Service starten tijdens boot proces<br>
sudo systemctl enable bigben.service

- Commando service starten tijdens opstarten<br>
sudo systemctl start bigben.service

- Controle of de service functioneert<br>
sudo systemctl status bigben.service

## Huidige service bigben
[Unit]<br>
Description=Bigben Python App<br>
<br>
[Service]<br>
ExecStart=/usr/bin/python /home/jsplinter/Documents/Kerstdorp/kerstdorp.py<br>
Restart=always<br>
User=root<br>
Group=root<br>
<br>
[Install]<br>
WantedBy=multi-user.target
