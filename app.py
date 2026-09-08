import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.5-flash")

app = Flask(__name__)

PALABRAS_GRAVE = [
    "no respira", "no puede respirar", "inconsciente", "convulsion",
    "convulsiones", "sangra mucho", "sangrado abundante", "no responde",
    "paro", "asfixia", "atragant", "dolor de pecho fuerte", "desangrando"
]

PALABRAS_MODERADO = [
    "fiebre alta", "vomito", "vómito", "mareo fuerte", "dolor fuerte",
    "quemadura", "torcedura", "esguince", "corte profundo", "alergia"
]

PALABRAS_LEVE = [
    "dolor de cabeza", "dolor leve", "mareo", "gripe", "tos",
    "dolor de garganta", "cansancio", "estres", "estrés", "insomnio"
]


def clasificar_sintoma(texto):
    texto = texto.lower()

    for palabra in PALABRAS_GRAVE:
        if palabra in texto:
            return "grave"

    for palabra in PALABRAS_MODERADO:
        if palabra in texto:
            return "moderado"

    for palabra in PALABRAS_LEVE:
        if palabra in texto:
            return "leve"

    return "leve"


def generar_recomendacion(sintoma, nivel):
    prompt = f"""
    Eres un asistente de primeros auxilios. Un usuario describió este síntoma: "{sintoma}".
    Se clasificó como nivel de gravedad: {nivel}.
    Da una recomendación breve (máximo 4 líneas), clara y en español,
    sobre qué puede hacer la persona. Si el nivel es grave, indica que
    llame de inmediato al número de emergencias (911 en El Salvador).
    No des diagnósticos médicos, solo orientación general.
    """
    respuesta = model.generate_content(prompt)
    return respuesta.text


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    nivel = None
    sintoma = ""

    if request.method == "POST":
        sintoma = request.form.get("sintoma", "").strip()
        if sintoma:
            nivel = clasificar_sintoma(sintoma)
            resultado = generar_recomendacion(sintoma, nivel)

    return render_template("index.html", resultado=resultado, nivel=nivel, sintoma=sintoma)


if __name__ == "__main__":
    app.run(debug=True, port=5000)