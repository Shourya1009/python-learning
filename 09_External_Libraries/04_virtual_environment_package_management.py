"""
🐍 Virtual Environment & Package Management in Python

----------------------------------------
🔹 What is a Virtual Environment?
----------------------------------------
- A virtual environment (venv) is an isolated environment for Python projects.
- Each project can have its own dependencies, separate from system Python.
- Prevents version conflicts when working on multiple projects.

----------------------------------------
🔹 Creating a Virtual Environment
----------------------------------------
    python -m venv myenv

----------------------------------------
🔹 Activating the Virtual Environment
----------------------------------------
    Windows -> myenv\Scripts\activate
    Linux/Mac -> source myenv/bin/activate

(After activation, you’ll see (myenv) before your terminal prompt)

----------------------------------------
🔹 Deactivating the Virtual Environment
----------------------------------------
    deactivate

----------------------------------------
🔹 Package Management with pip
----------------------------------------
# Install a package
    pip install requests

# Install a specific version
    pip install requests==2.31.0

# Upgrade a package
    pip install --upgrade requests

# Uninstall a package
    pip uninstall requests

----------------------------------------
🔹 Requirements File
----------------------------------------
# Save dependencies to file
    pip freeze > requirements.txt

# Install dependencies from file
    pip install -r requirements.txt

----------------------------------------
✅ Example Workflow
----------------------------------------
1. mkdir myproject && cd myproject
2. python -m venv venv
3. Activate:
    venv\Scripts\activate (Windows)
    source venv/bin/activate (Linux/Mac)
4. pip install flask requests
5. pip freeze > requirements.txt
6. Share project → others run: pip install -r requirements.txt

----------------------------------------
📦 Summary
----------------------------------------
Virtual environments keep projects isolated, 
pip manages packages, and requirements.txt makes your project reproducible.
"""