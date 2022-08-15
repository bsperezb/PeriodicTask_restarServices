#! usr/bin/bash
systemctl restart vpntcc 
pm2 restart restify 
pm2 restart restify-seg-box 
pm2 restart restify-channel 