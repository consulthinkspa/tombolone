# Tombolone

Tabella segna punti per il gioco della tombola.

### Build and run MS Windows

Per compilare il file `.exe` per poter eseguire il tabellone, posizionarsi nella cartella del repository e lanciare i comandi a seguire:

```
python -m pip install pyinstaller
python -m PyInstaller --clean --onefile .\tombola.py
```

Per poi successivamente eseguire:

```
.\dist\tombola.exe
```

### Run on Unix-like systems

Sugli altri sistemi operativi, generalmente è nativamente presente Python.
Pertanto è sufficiente sempre posizionarsi nella cartella del repository ed eseguire il comando:

```
python tombola.py
```