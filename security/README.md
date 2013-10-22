$ openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout fb_staging1.key -out fb_staging1.crt
Generating a 1024 bit RSA private key
...++++++
.++++++
writing new private key to 'fb_staging1.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:MA
Locality Name (eg, city) []:Cambridge
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Redstar Ventures LLC
Organizational Unit Name (eg, section) []:FamilyBridge
Common Name (e.g. server FQDN or YOUR name) []:
Email Address []:tech@redstar.com

$ openssl pkcs12 -export -in fb_staging1.crt -inkey fb_staging1.key -out fb_staging1.p12
Enter Export Password:
Verifying - Enter Export Password:

### Uploaded fb_staging1.crt to IPP App
