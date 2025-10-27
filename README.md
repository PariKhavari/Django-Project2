# 🍎 fruit_app2


## 🇬🇧 Description
A simple **Django project** with an app named **fruit_app2**.  
The app displays fruits on simple HTML pages.  
Perfect for Django beginners.




### 2️⃣ Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # macOS/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the server
```bash
python manage.py runserver
```

Then open:  
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## 🧩 Structure

core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
fruit_app2/
│   │
│   │──static/
│   │  └──css     
│   │
│   ├── templates/
│   │   └── *.html
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
manage.py
requirements.txt
```


## 💬 Example Commit
```bash
git add .
git commit -m "feat(fruit_app2): simple HTML fruit app added"
```

