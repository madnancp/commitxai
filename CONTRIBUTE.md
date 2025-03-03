# 🤝 Contributing to CommitXAI  
## 🛠️ How to Contribute  

### 1️⃣ Fork & Clone the Repository  
1. Click the **Fork** button on the top right of the repo.  
2. Clone your fork locally:  
```bash
git clone https://github.com/your-username/commitxai.git
cd commitxai
git remote add upstream https://github.com/original-author/commitxai.git
```
3. Keep your fork updated with the latest changes:  
```bash
git fetch upstream
git merge upstream/main
```

### 2️⃣ Set Up the Development Environment  
Ensure you have **Python** and **uv** installed. Then, set up the environment:  
```bash
uv venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
uv pip install -e .
```

### 3️⃣ Create a New Branch  
Before making changes, create a feature branch:  
```bash
git checkout -b feature-branch-name
```

### 4️⃣ Make Your Changes  
- Follow best practices for **code quality** and **documentation**.  
- Run tests before pushing your changes.  

### 5️⃣ Commit Your Changes  
Use meaningful commit messages:  
```bash
git add .
git commit -m "feat: Add feature X to improve Y"
```

### 6️⃣ Push and Create a Pull Request  
```bash
git push origin feature-branch-name
```
Go to the **GitHub repository**, navigate to the **Pull Requests** tab, and open a new PR.  

## ✅ Contribution Guidelines  
- **Write clean and readable code** 📝  
- **Follow the existing project structure** 📁  
- **Include necessary tests** ✅  
- **Ensure your changes do not break existing functionality** 🚀  
