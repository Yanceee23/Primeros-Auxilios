Primeros Auxilios — Indicaciones de instalación y uso

Chatbot web en Python (Flask) que recibe los síntomas de una persona, los clasifica por nivel de gravedad (leve, moderado, grave) y genera una recomendación usando la API de Gemini.

Requisitos previos
Python 3.10 o superior instalado
Una API key de Gemini (gratuita): https://aistudio.google.com/apikey
1. Clonar o descargar el proyecto
bash
git clone https://github.com/Yanceee23/Primeros-Auxilios#primeros-auxilios
cd tu-repositorio
2. Crear el entorno virtual
bash
python -m venv venv
3. Activar el entorno virtual

Windows (PowerShell):

bash
venv\Scripts\activate

Mac/Linux:

bash
source venv/bin/activate

Debe aparecer (venv) al inicio de la línea de la terminal.

4. Instalar las dependencias
bash
pip install flask python-dotenv google-generativeai
5. Configurar la API key
Copia el archivo de ejemplo: Windows:
bash
   copy .env.example .env

Mac/Linux:

bash
   cp .env.example .env
Abre el archivo .env y reemplaza el valor con tu propia API key de Gemini, sin comillas:
   GEMINI_API_KEY=tu_api_key_real_aqui

⚠️ El archivo .env nunca se sube a GitHub (ya está excluido en .gitignore). Solo .env.example se comparte, como referencia de qué variables se necesitan.

6. Ejecutar el proyecto
bash
python app.py

Cuando la terminal muestre:

Running on http://127.0.0.1:5000

abre esa dirección en tu navegador.

7. Cómo usarlo
Escribe en el cuadro de texto qué sientes (ej. "me duele la cabeza y tengo fiebre").
Presiona Enviar.
El bot clasifica el síntoma por gravedad y muestra una recomendación:
🟢 Leve: cuidados generales
🟡 Moderado: indicaciones más detalladas
🔴 Grave: alerta de emergencia y recomendación de llamar al 911
8. Detener el servidor

En la terminal, presiona:

Ctrl + C
Estructura del proyecto
proyecto/
├── app.py
├── .env              (no se sube a GitHub)
├── .env.example
├── .gitignore
├── requirements.txt
└── templates/
    └── index.html
Notas
Este chatbot ofrece orientación general y no sustituye la atención médica profesional.
Ante una emergencia real, llama de inmediato a los servicios de emergencia.