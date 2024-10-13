import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract
import google.generativeai as genai

# Configurar a chave da API do Google Generative AI
genai.configure(api_key="COLE SUA CHAVE API AQUI")  # Substitua pela sua chave

# Especificar o caminho do executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Função para carregar a imagem e realizar o OCR
def carregar_imagem():
    imagem_caminho = filedialog.askopenfilename(
        filetypes=[("Arquivos de imagem", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff")]
    )
    if not imagem_caminho:
        return

    try:
        img = Image.open(imagem_caminho)
        texto_extraido = pytesseract.image_to_string(img, lang='por')
        texto_entrada.delete("1.0", tk.END)
        texto_entrada.insert(tk.END, texto_extraido)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao carregar a imagem: {e}")

# Função para enviar o texto extraído ao modelo de IA e exibir o retorno
def enviar_texto():
    texto = texto_entrada.get("1.0", tk.END)
    if not texto.strip():
        messagebox.showwarning("Aviso", "Por favor, extraia o texto da imagem antes de enviar.")
        return

    # Prompt descritivo corrigido
    prompt = f"""
    Analise o seguinte texto e me forneça os dados detalhado:

    {texto}
    """

    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(prompt)

    texto_saida.delete("1.0", tk.END)
    texto_saida.insert(tk.END, response.text)

# Criar a janela principal
janela = tk.Tk()
janela.title("DataVision")

# Criar um frame para os campos de entrada e saída
frame_principal = tk.Frame(janela)
frame_principal.pack(padx=10, pady=10)

# Criar um frame para o campo de entrada de texto
frame_entrada = tk.Frame(frame_principal)
frame_entrada.grid(row=0, column=0, padx=5)

label_entrada = tk.Label(frame_entrada, text="Texto extraído da imagem:")
label_entrada.pack(anchor="w")

scroll_entrada = tk.Scrollbar(frame_entrada)
scroll_entrada.pack(side=tk.RIGHT, fill=tk.Y)

texto_entrada = tk.Text(frame_entrada, height=20, width=60, yscrollcommand=scroll_entrada.set)
texto_entrada.pack()

scroll_entrada.config(command=texto_entrada.yview)

# Criar um frame para o campo de saída de texto
frame_saida = tk.Frame(frame_principal)
frame_saida.grid(row=0, column=1, padx=5)

label_saida = tk.Label(frame_saida, text="Resposta gerada pela IA:")
label_saida.pack(anchor="w")

scroll_saida = tk.Scrollbar(frame_saida)
scroll_saida.pack(side=tk.RIGHT, fill=tk.Y)

texto_saida = tk.Text(frame_saida, height=20, width=60, yscrollcommand=scroll_saida.set)
texto_saida.pack()

scroll_saida.config(command=texto_saida.yview)

# Botão para carregar a imagem e realizar OCR
botao_carregar_imagem = tk.Button(janela, text="Carregar Imagem", command=carregar_imagem)
botao_carregar_imagem.pack(pady=5)

# Botão para enviar o texto
botao_enviar = tk.Button(janela, text="Enviar para Tratamento", command=enviar_texto)
botao_enviar.pack(pady=5)

janela.mainloop()