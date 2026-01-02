# Background

Proyecto en Python para eliminar automáticamente el fondo de imágenes y GIFs.

## Descripción

Permite eliminar el fondo de imágenes y GIFs animados utilizando la librería `rembg`. El programa guarda las imágenes sin fondo en `output/` organizadas por fecha y mantiene una copia de las originales en `output/[fecha]/originals/`.

## Requisitos

- Python 3.7+
- rembg (`pip install rembg`)
- Pillow (`pip install pillow`)

## Instalación

1. Clona este repositorio:

```
git clone https://github.com/edwarSuarezQ/BackGround.git
```

2. Instala las librerías necesarias con el siguiente comando:

```bash
pip install rembg pillow
```

## 💡 **Recomendación: Entornos Virtuales (VENV)**
Se recomienda encarecidamente utilizar un entorno virtual para este proyecto.

#### ¿Por qué es útil?
- **Aislamiento**: Mantiene las librerías del proyecto separadas de tu instalación principal de Python.
- **Control de Versiones**: Evita conflictos si diferentes proyectos necesitan versiones distintas de la misma librería.
- **Limpieza**: Si deseas eliminar el proyecto, simplemente borras la carpeta venv y no quedan residuos en tu sistema.

#### ¿Cómo configurarlo?
1. **Crear el entorno virtual**:
```bash
python -m venv venv
```
2. **Activar el entorno**:
- **Windows**:
```bash
.\venv\Scripts\activate
```
- **macOS / Linux**:
```bash
source venv/bin/activate
```
3. **Instalar dependencias dentro del entorno**:
```bash
pip install rembg pillow
```

## Uso

Ejecuta el programa:

```bash
python BackGroundRemove.py
```
