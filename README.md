


# 🚀 PORTSC++ - Advanced Python Port Scanner  

A lightning-fast ⚡ and efficient port scanner written in Python. It scans target IPs or domains for open **TCP** and **UDP** ports, detects services, and grabs banners.  

## ✨ Features  
- 🔍 Scans multiple ports or port ranges (e.g., `1-1024,8080`).  
- ⚡ Uses multithreading for faster scans (up to 200 threads).  
- 🛠 Detects **TCP** and **UDP** services.  
- 🏷 Grabs banners for common services like HTTP and SSH.  
- 💾 Saves scan results to a JSON file (`scan_results.json`).



## 🛠 Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/portscpp.git  
   cd portscpp  
   ```  

2. Install the required dependencies:  
   ```bash
   chmod +x requirements.txt
   pip install -r requirements.txt  
   ```  

## 🚦 Usage  
Run the script with the target IP or domain:  
```bash  
python3 portscpp.py <target> [options]  
```  

### ⚙️ Options  
- `-p` or `--ports`: Specify ports to scan (default: `1-1024,3000-4000,8080,8443`).  
- `-t` or `--threads`: Set the number of threads (default: `200`).  
- `-u` or `--udp`: Enable **UDP scanning** (default: TCP).  

### 📌 Examples  
1. **TCP Scan**:  
   ```bash  
   python3 portscpp.py example.com -p 1-1000,8080 -t 100  
   ```  

2. **UDP Scan**:  
   ```bash  
   python3 portscpp.py example.com -p 53,67,68,161 -u  
   ```  

## 📊 Output  
The script will display:  
- ✅ Open ports with their services.  
- 🏷 Banners for detected services (TCP only).  
- 📝 A summary of the scan (total ports scanned, open ports, etc.).  
- 💾 Results saved to `scan_results.json`.  

## 📋 Requirements  
- Python 3.x  
- Libraries: `argparse`, `socket`, `concurrent.futures`, `termcolor`, `pyfiglet`  


