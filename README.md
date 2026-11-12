Experto en Mascotas
Sistema experto en Python que recomienda una mascota según siete factores: espacio, tiempo, presupuesto, experiencia, actividad física, presencia de niños y preferencia.
Mejoras incluidas
Resolución de conflictos por votos, especificidad y prioridad.
Reglas compatibles con la preferencia seleccionada.
Recomendaciones de respaldo cuando ninguna regla específica coincide.
Explicación limitada a las reglas que apoyan la recomendación ganadora.
Manejo de errores al crear o escribir el historial CSV.
Ejecución de consola compatible con GitHub Codespaces.
Pruebas automáticas con `unittest`.
Ejecutar en GitHub Codespaces
En GitHub, seleccione Code > Codespaces > Create codespace on main.
En la terminal ejecute:
```bash
python main.py
```
Ejecutar pruebas
```bash
python -m unittest discover -s tests -v
```
Archivos
`main.py`: motor de inferencia e interacción por consola.
`knowledge_base.py`: reglas y recomendaciones de respaldo.
`tests/test_sistema.py`: pruebas automáticas.
`.devcontainer/devcontainer.json`: configuración de Codespaces.
`.gitignore`: excluye archivos temporales y el historial local.
El archivo `historial_mascotas.csv` se crea automáticamente y no se sube al repositorio.
