# Experto en Mascotas con interfaz web

Interfaz construida con Streamlit para ejecutarse en GitHub Codespaces.

## Ejecutar

```bash
pip install -r requirements.txt
streamlit run app.py
```

Codespaces abrirá automáticamente el puerto 8501. Si no ocurre, abra la pestaña **Ports**, busque el puerto **8501** y seleccione **Open in Browser**.

## Pruebas

```bash
python -m unittest discover -s tests -v
```

`README_UI.md` tiene un nombre diferente para no reemplazar el README existente del repositorio.
