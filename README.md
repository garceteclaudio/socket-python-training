# Crear entorno virtual
python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

pip list


# Redes

netstat -ano | findstr :5555

tasklist | findstr 16132

taskkill /PID 16132 /F