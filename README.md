# 🌐 SubHunt

A fast, multithreaded subdomain enumeration tool built in Python. SubHunt helps penetration testers and bug bounty hunters uncover valid subdomains of a target domain using brute-force techniques. It supports multithreading, color-coded results, and result export to a file.


---

## 🚀 Usage

```bash
python subhunt.py <TARGET_DOMAIN> [options]
```


### 📌 Example

```bash
python subhunt.py example.com -w subdomains.txt -t 100 -o found.txt
```

---


## ⚙️ Command-Line Options

 Option                   Description                                         

 `domain`                Target domain (e.g., `example.com`)                 
                         
 `--wordlist`, `-w`      Path to subdomain wordlist file (`subdomains.txt` default)                 

 `--threads`, `-t`       Number of concurrent threads (default: 50)        

 `--output`, `-o`        Output file to save valid subdomains (default: `found_subdomains.txt`)       

---


## ✨ Features

- ✅ **Multithreaded subdomain resolution**  
- ✅ **Color-coded output** (Found = Green, Not Found = Red)  
- ✅ **Save results** to an output file  
- ✅ **Custom wordlists and thread count**  
- ✅ **Minimal dependencies** and lightweight code  

---



## 📦 Requirements

- Python 3.x  
- `colorama` for colored output  

Install using:

```bash
pip install colorama
```

---



## 📁 Sample Wordlist Format

```
www
admin
blog
ftp
mail
```

---


## 🛡️ Disclaimer

This tool is intended for **educational and authorized security testing only**. Do not use it on targets you do not have permission to scan.

---



## 📄 License

This project is licensed under the [MIT License](LICENSE).#   s u b h u n t 
 
 
