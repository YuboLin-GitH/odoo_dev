docker stop container-postgresdb
docker stop odoo
docker start container-postgresdb
docker start odoo
Start-Process chrome.exe http://localhost:8069/web?debug=1