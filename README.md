<h1 align="center">Port Prober  :mailbox:</h1><br> 
<p align="center">
  <img src="https://img.shields.io/badge/build-passed-brightgreen" alt="build status">
  <img src="https://img.shields.io/badge/analyze-passed-rightgreen" alt="Analyze">
  <img src="https://img.shields.io/badge/tests-477%20passed%2C%202%20failed-red" alt="version">
  <img src="https://img.shields.io/badge/coverage-75%25-green" alt="Coverage"></br>
  <img src="https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen" alt="Test">
  <img src="https://img.shields.io/badge/python-v3.7-blue" alt="Python V3.7">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Status-up-brightgreen" alt="status-up"><br><br>
  Port Prober is Automated Simple python script for port scan and It can check whether the Provided port of the remote host can be Forwarded or Not.
</p><br>

```

      :::::::::   ::::::::  ::::::::: :::::::::::        :::::::::  :::::::::   ::::::::  :::::::::  :::::::::: ::::::::: 
     :+:    :+: :+:    :+: :+:    :+:    :+:            :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:        :+:    :+: 
    +:+    +:+ +:+    +:+ +:+    +:+    +:+            +:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ +:+        +:+    +:+  
   +#++:++#+  +#+    +:+ +#++:++#:     +#+            +#++:++#+  +#++:++#:  +#+    +:+ +#++:++#+  +#++:++#   +#++:++#:    
  +#+        +#+    +#+ +#+    +#+    +#+            +#+        +#+    +#+ +#+    +#+ +#+    +#+ +#+        +#+    +#+    
 #+#        #+#    #+# #+#    #+#    #+#            #+#        #+#    #+# #+#    #+# #+#    #+# #+#        #+#    #+#     
###         ########  ###    ###    ###            ###        ###    ###  ########  #########  ########## ###    ###    


usage: main.py [-h] [-i IP] [-H HOST] [-p PORT] [-a] [-P PORT] [-v] [-f PF]

Port Prober 

example: python3 main.py -i 172.217.31.196 -p 1000
         python3 main.py -H www.google.com -P "21 22 53 80 443 445" 

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP        IP Address of Host (default: 127.0.0.1) 
  -H HOST, --host HOST  Host Name (default: secarmy.org) 
  -p PORT, --port PORT  Range of Port
  -a                    Aggressive Scanning
  -P PORT, --PORT PORT  List of Particular Ports (Example: --PORT "21 22 80 443")
  -v, --version         Prints Version
  -f PF, --port-forwardable PF
                        To Check whether Open Port is Forwardable or not

```

### Prerequisites  :package:
1.Python 3.X with pip3 Installed  
If not then, pip3 installation  
```
apt install python3-pip
```  
To Check pip versioon  
```
pip3 --version
```

### Installation  :floppy_disk:
Open Terminal and type
```
git clone https://github.com/Aravindha1234u/PortProber

cd PortProber
```

To Install required Python package

```
pip3 install -r requirements.txt
```
or
```
python3 -m pip install -r requirements.txt
```

### Execution  :+1:
To Run Port Prober (displays Help)

```
python3 main.py -i 172.217.31.196 -p 1000

python3 main.py -i 127.0.0.1 -f 64352
```

### Issues
Feel free to express any kind of bug or error in this tool by reporting it in issues, So that it can be fixed soon.<br>
<a href="https://github.com/Aravindha1234u/PortProber/issues"><img src="https://img.shields.io/badge/issues-0-yellow" /></a>
