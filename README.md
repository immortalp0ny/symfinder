# SymFinder
Multi platform simple tool for resolving symbols by their hashes. 
This technique most used by malware
### Installing
Install [Python 2.7](https://www.python.org/downloads/release/python-2716/)

Just clone the repository. 
```bash
git clone https://github.com/immortalp0ny/symfinder.git
```
Install all python requirements via pip
```bash
pip install click tabulate colorama pefile pyelftools
```

### Example
```bash
symfinder sym ror13add -h 0xBF60601C -h 0xE553E06F -o win -l kernel32.dll --fmt-append-zero

[+] - [2019-05-06 21:34:01] - [R] - Check hash 0xbf60601c inside lib kernel32.dll
[+] - [2019-05-06 21:34:07] - [R] - Check hash 0xe553e06f inside lib kernel32.dll
╒════════════════╤════════════╤══════════════╕
│ Sym Name       │ Hash       │ Dll Name     │
╞════════════════╪════════════╪══════════════╡
│ GlobalAlloc    │ 0xbf60601c │ kernel32.dll │
├────────────────┼────────────┼──────────────┤
│ GetProcAddress │ 0xe553e06f │ kernel32.dll │
╘════════════════╧════════════╧══════════════╛
```
