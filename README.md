# Crear entorno virtual


```bash
python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

pip list
```


# Redes

```bash
netstat -ano | findstr :5555

tasklist | findstr 14268

taskkill /PID 14268 /F
```