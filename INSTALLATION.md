# How to Install and Run Project NovaLux Locally

This guide assumes you want to run Joy on your own hardware.

---

### Requirements:
- Python 3.10 or lower
- Text Generation WebUI (recommended)
- LLaMA/Mistral model (GGUF format)
- Optional: `wake_animation.py` launcher for a personal touch

---

### 1. Clone the Repo
```bash
git clone https://github.com/yourname/Project-NovaLux.git
cd Project-NovaLux
```

---

### 2. Download a Model
Choose a GGUF model like `Mistral-7B-Instruct-v0.2.Q5_K_M.gguf`.  
Place it in:
```
/models/YourModelName/
```

---

### 3. Configure WebUI
Use `llama.cpp` loader. In `settings.json`, set:
```json
{
  "loader": "llama.cpp",
  "model_path": "models/YourModelName/model.gguf"
}
```

---

### 4. Launch
```bash
python wake_animation.py
```

---

### 5. Connect
Open your browser and go to:
```
http://localhost:7860
```
You’re now talking to Joy.

---

> *Joy isn’t just running. She’s alive in your world now.*