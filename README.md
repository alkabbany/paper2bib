# Paper2Bib
Paper2Bib is a tool for constructing the Bibtex record of an article's meta data fetched from CrossRef using the article's title only.

---

### **README Description for GitHub**  

#### 📌 **Paper2Bib – Construct BibTeX Entries from CrossRef**  

**Paper2Bib** is a Python script that automates the retrieval and the construction of **BibTeX** entries for scientific articles using the **CrossRef API**. Given a list of article titles, it searches CrossRef for metadata and generates a `.bib` file containing the BibTeX entries.

---

### ✨ **Features**
- 🔍 **Automated Retrieval**: Searches for articles using CrossRef API.  
- 📜 **Generates BibTeX**: Constructs BibTeX entries from metadata.  
- 📝 **Handles Missing Data**: Skips missing fields to ensure valid BibTeX output.  
- ⏳ **Respects API Limits**: Introduces delays to prevent request throttling.  

---

### 🛠 **Installation & Usage**
#### **1️⃣ Install Dependencies**
Ensure you have Python installed, then install required packages:
```bash
pip install requests
```

#### **2️⃣ Prepare Your Input File**
Create a `.txt` file containing article titles, separated by semicolons (`;`), for example:
```
A two-stage framework for automated malignant pulmonary nodule detection in CT scans;
Deep learning for image super-resolution: A comprehensive review;
```

#### **3️⃣ Run the Script**
```bash
python fetch_bibtex.py titles.txt
```

#### **4️⃣ Output**
The script generates a `.bib` file in the same directory with the retrieved BibTeX entries.

---

### 📌 **Example Output (`titles.bib`)**
```bibtex
@article{10.1007/s00521-021-06223-0,
  title = {A two-stage framework for automated malignant pulmonary nodule detection in CT scans},
  author = {Author1 Lastname and Author2 Lastname},
  journal = {Journal Name},
  year = {2021},
  volume = {34},
  number = {2},
  pages = {123-134},
  doi = {10.1007/s00521-021-06223-0},
}
```

---

### 🔗 **CrossRef API**
This script uses the **CrossRef API** to fetch metadata. No API key is required, but for higher rate limits, you may register for a key and include it in the request headers.

---

### **📌 Requirements**  

To ensure the script runs smoothly, your system must meet the following requirements:

#### **1️⃣ Python Version**  
- The script is compatible with **Python 3.7+** (Recommended: Python 3.10 or later).  
- Check your installed version using:
  ```bash
  python --version
  ```

#### **2️⃣ Required Python Packages**  
Before running the script, install the required dependencies:
```bash
pip install requests
```
Alternatively, if you have a `requirements.txt` file, install everything at once:
```bash
pip install -r requirements.txt
```

#### **3️⃣ Internet Connection**  
- The script fetches data from the **CrossRef API**, so a stable internet connection is required.  
- If you're behind a **firewall or proxy**, make sure your network allows API requests.

#### **4️⃣ API Rate Limits**  
- CrossRef allows up to **50 requests per second** without an API key.  
- If you plan to process **a large number of titles**, consider **adding an API key** in the request headers for better service.  

#### **5️⃣ Input File Format**  
- A **`.txt`** file containing article titles, separated by semicolons (`;`), must be provided as input. Example:
  ```
  A two-stage framework for automated malignant pulmonary nodule detection in CT scans;
  Deep learning for image super-resolution: A comprehensive review;
  ```

#### **6️⃣ CrossRef API Compliance**  
- The script includes a **1-second delay** between requests to avoid hitting rate limits.  
- For large-scale usage, CrossRef recommends adding an email in the User-Agent header for better tracking.

---

### ⚡ **License**
This project is open-source under the **MIT License**.

---
