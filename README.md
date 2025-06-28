# Reto_6_POO
Reto 6 manejo de errores
### 1. Añadir excepciones a los ejercicios del reto 1
- Al estar trabajando con funciones solo fue necesario en su mayoria añadir error del tipo ValueError para evitar que se ingresaran valores no validos a las funciones
### 2. Añadir excepciones a los ejercicios del reto 4 (clase shape)
Para este caso se añadieron:
- ValueError en la clase shape para determinar que el dato ingresado para crear una isntancia de esta sea una lista (esto sera heredado y comprobado por todas las demas clases)
- Type error en las instancias de triangulos y rectangulos para verificar que el tipo de datos ingresados sean lineas
- Index error en Rectangle y los diferentes tipos de triangulos para verificar la cantida de datos dentro de la lista "aristas" necesarios para crear una instancia de la figura
