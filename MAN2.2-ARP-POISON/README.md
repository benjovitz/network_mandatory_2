started out by setting up ip rules
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to- ports 8080                             
sudo iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-ports 8443

i then setup burp to both http and https, i exported the CA from burp and transferred it to my victim VM and setup as trusted CA in firefox.

I am running my arp posing script to poison both the router and the target.
