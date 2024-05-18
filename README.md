# python3-course

## Step 0: 專案前置

python3

## Step 1: Create

### 安裝 PDM

python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install pdm

#### 若 pdm not found 則輸入 (通常為新安裝電腦需要)

export PATH=$PATH:~/.local/bin

## Step 2: init project

```
pdm init
pdm add fastapi uvicorn
```

```
// main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

## Step 3: start project

```
pdm run uvicorn main:app --reload
or
pdm run uvicorn main:app --reload --port 8000
```
