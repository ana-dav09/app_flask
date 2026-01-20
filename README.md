# Web App con Flask

Esta aplicación web con Flask permite:
- Crear, actualizar y eliminar items
- Subir archivos y ver su contenido
- Listar items

## Requisitos

- Docker instalado
- Puerto 5000 libre

## Instrucciones

1. Clonar el repositorio:
```bash
git clone https://github.com/ana-dav09/app_flask
cd app_flask

2. Construir la imagen del docker
```bash
docker build -t app_flask .
```

3. Correr el contenedor
```bash
docker run -p 5000:5000 app_flask
```

4. Abrir en el navegador
```bash
http://localhost:5000
```

## Notas
- Los archivos subidos se guardan en la carpeta uploads dentro del contenedor.
- Todos los cambios en items se mantienen mientras el contenedor esté corriendo (no hay DB persistente).
