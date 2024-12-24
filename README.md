
# Store Management

Basic Store Management system that supports
1. List all product details
2. Update Price
3. Add Employee
4. Add Product
5. Exit Store


## Run Locally

Extract the project

Go to the project directory

```bash
  cd shopping-mall
```

Install [uv](https://docs.astral.sh/uv)

```bash
  #If python is already installed
  pip install uv 
  
  #For MacOS and Linux
  curl -LsSf https://astral.sh/uv/install.sh | sh 
  
  #For Window using powershell
  powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Check python version

```bash
  python --version
```

Create virtualenv and Install python 3.10 using uv if not installed

```bash
  uv venv --python 3.10.0
```

Create virtualenv

```bash
  uv venv
```

Activate virtualenv

```bash
  .\.venv\Scripts\activate #Windows CMD
  source venv/Scripts/activate #Bash
```

Install dependencies from pyproject.toml file

```bash
  uv pip install -r pyproject.toml
```

Run project

```bash
  python main.py
```

