# Header-Hunter
Trying to avoid the fatigue!


#### Usage
      ./HeaderHunter.py -h
      usage: HeaderHunter.py [-h] [-ch] [-o] [-x] (-t  | -w ) [ ...]

      positional arguments:


      optional arguments:
        -h, --help        show this help message and exit
        -ch, --cheaders   Fetch current headers
        -o , --origin     Origin required for API
        -x , --proxy      Proxy - http://IP:PORT
        -t , --target 
        -w , --wordlist   Provide list of targets
        
#### Setup for single targe
##### The script accepts variations, so it can supplied `https`, `http` or nothing. Either case you will work. At least it was supposed to work!
##### The flag `-ch` fetches the current headers, which means, retrieve all headers
       ./HeaderHunter.py -t https://target.com

#### Sample output with `-ch` flag on
      ./HeaderHunter.py -t https://target.com -ch
      Created By: SickAndTired

      [•] BASE TARGET - [https://target.com]
      [»] REDIRECTION - [https://target.com/]

      [Info Disclosure]
      [*] - Server: Microsoft-IIS/8.5
      [*] - X-Powered-By: ASP.NET
      [*] - X-Powered-By-Plesk: PleskWin

      [Missing Security Headers]
      [x] - X-Frame-Options
      [x] - X-Content-Type-Options
      [x] - Referrer-Policy
      [x] - Strict-Transport-Security
      [x] - Content-Security-Policy
      [x] - Permissions-Policy
      [x] - X-XSS-Protection
      [x] - Access-Control-Allow-Origin

      [Current Headers]
      [✓] - Content-Type
      [✓] - Server
      [✓] - X-Powered-By
      [✓] - X-Powered-By-Plesk
      [✓] - Date
      [✓] - Content-Length
