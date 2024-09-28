# Sistema de recomendación de películas/machine learning/HENRY

![Imagen del Proyecto]("C:\Users\veram\OneDrive\Escritorio\mi_directorio\El texto del párrafo.pdf")  

## Descripción

¡Hola, soy Vera! 🎬 

Este sistema de recomendación de películas utiliza técnicas de aprendizaje automático para sugerir películas similares a las que ya te gustan. Basado en un modelo de similitud del coseno que analiza características como género y overview . te ofrece una lista personalizada de títulos que podrían interesarte. ¡Descubre nuevas joyas cinematográficas y explora el mundo del cine de una manera más inteligente!

### Funcionalidades

- **Recomendación de Películas:** Recomendaciones basadas en la similitud del coseno.
- **API Rápida:** Utiliza FastAPI para proporcionar una API eficiente y rápida.
- **Despliegue en Docker:** Incluye un Dockerfile para facilitar el despliegue en cualquier entorno compatible con Docker.

### Tecnologías Utilizadas

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
- **Machine Learning:** [scikit-learn](https://scikit-learn.org/)
- **Docker:** [Docker](https://www.docker.com/)
- 

### * Instalación*

Sigue estos pasos para instalar y configurar el proyecto en tu máquina local:

1. **Clona el Repositorio:**

    ```bash
    git clone https://github.com/veraguillen/Proyecto-Machine.git
    ```

2. **Navega al Directorio del Proyecto:**

    ```bash
    cd tu_repositorio
    ```

3. **Crea un Entorno Virtual:**

    ```bash
    python -m venv venv
    ```

4. **Activa el Entorno Virtual:**

    - En Windows:

        ```bash
        venv\Scripts\activate
        ```

    - En macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Instala las Dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Configura los Datos:**

    Asegúrate de que la configuración de los datos esté correcta en el archivo.

7. **Ejecuta la Aplicación:**

    ```bash
    uvicorn app.main:app --reload
    ```


## Cómo usar la aplicación

Entra a http://localhost:8000/docs


1.Encontraras 6 endpoints donde podras hacer diferentes consultas a nuestros datos. En qué año fue estrenada cierta película?  o cuánto ha recaudado en su carrera tal actor/actriz/director?, entre otros detalles.

2.El enpoint #7  contiene el modelo de recomendación, sólo tendrás que escribir el título de alguna película y si esta en nuestro dataset te recomendara 5 películas distintas basandose en sus generos y overview. 


**Ejemplo:**

Para obtener recomendaciones de películas, envía una solicitud GET a `http://localhost:8000/recommendations?title=tu_titulo`.



