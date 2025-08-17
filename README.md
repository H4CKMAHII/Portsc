# 🚀 PORTSC++ - Advanced Python Port Scanner  

A lightning-fast ⚡ and efficient port scanner written in Python. It scans target IPs or domains for open ports, detects services, and grabs banners.  

## ✨ Features  
- 🔍 Scans multiple ports or port ranges (e.g., `1-1024,8080`).  
- ⚡ Uses multithreading for faster scans (up to 200 threads).  
- 🛠 Detects services running on open ports.  
- 🏷 Grabs banners for common services like HTTP and SSH.  
- 💾 Saves scan results to a JSON file (`scan_results.json`).



## 📸 Screenshot of Port Scanner


<p align="center">
  <img src="port++.png" alt="Port Scanner Screenshot" width="600">
</p>

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

### 📌 Example  
```bash  
python3 portscpp.py example.com -p 1-1000,8080 -t 100  
```  

## 📊 Output  
The script will display:  
- ✅ Open ports with their services.  
- 🏷 Banners for detected services.  
- 📝 A summary of the scan (total ports scanned, open ports, etc.).  
- 💾 Results saved to `scan_results.json`.  

## 📋 Requirements  
- Python 3.x  
- Libraries: `argparse`, `socket`, `concurrent.futures`, `termcolor`, `pyfiglet`  
  
