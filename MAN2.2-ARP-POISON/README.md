started out by setting up ip rules
```
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to- ports 8080                             
sudo iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-ports 8443
```

I am running my arp posing script to poison both the router and the target.

![[arp_table.png]]

I then setup burp to both http and https.

![[burp_setup.png]]

I exported the CA from burp and transferred it to my victim VM and setup as trusted CA in firefox.

![[transfer_cert.png]]

![[ca_setup.png]]

I am now able to MITM http and https traffic.

![[http.png]]

![[https.png]]
