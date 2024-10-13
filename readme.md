# DataVision - Extração de Dados de Imagens com OCR e IA

Este aplicativo utiliza OCR e Inteligência Artificial para extrair dados de imagens e fornecer análises detalhadas.

## Funcionalidades

* **Extração de texto de imagens:** Utiliza a biblioteca `pytesseract` para realizar o reconhecimento óptico de caracteres (OCR) em imagens e extrair o texto contido nelas.
* **Processamento de linguagem natural:** Envia o texto extraído para o modelo de IA `gemini-1.5-pro` do Google Generative AI para análise e interpretação.
* **Interface gráfica amigável:** Interface gráfica simples e intuitiva construída com `tkinter`, facilitando a interação do usuário.

## Pré-requisitos

* **Python 3.x:** Certifique-se de ter o Python 3 instalado em seu sistema.
* **Bibliotecas:** Instale as bibliotecas necessárias utilizando o `pip`:
    ```bash
    pip install tkinter pillow pytesseract google-generativeai
    ```
* **Tesseract OCR:** Faça o download e instale o Tesseract OCR em seu sistema.
    * **Windows:** [Baixe aqui](https://github.com/UB-Mannheim/tesseract/wiki)
    * **Linux:** Utilize o gerenciador de pacotes da sua distribuição (ex: `sudo apt-get install tesseract-ocr`).
* **Chave da API do Google Generative AI:** Obtenha uma chave de API do Google Generative AI e **configure-a no código.** (Veja instruções detalhadas na seção "Como usar")

## Como usar

1. **Clone o repositório:**
    ```bash
    git clone [https://github.com/arthur-oliveira-oficial/datavision](https://github.com/arthur-oliveira-oficial/datavision)
    ```
2. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Configure o caminho do Tesseract:**
    * No arquivo `main.py`, atualize a variável `pytesseract.pytesseract.tesseract_cmd` com o caminho completo para o executável do Tesseract OCR em seu sistema. Por exemplo: 
       ```python
       pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 
       ```
4. **Insira sua chave de API:**
    * No arquivo `main.py`, na linha 8, substitua `"COLE SUA CHAVE API"`  pela sua chave da API do Google Generative AI:
       ```python
       genai.configure(api_key="SUA_CHAVE_API_AQUI") 
       ```
5. **Execute o aplicativo:**
    ```bash
    python main.py
    ```
6. **Carregue uma imagem:**
    * Clique no botão "Carregar Imagem" e selecione a imagem desejada.
7. **Extraia o texto:**
    * O texto extraído da imagem será exibido na área de texto à esquerda.
8. **Envie o texto para análise:**
    * Clique no botão "Enviar para Tratamento" para enviar o texto extraído para o modelo de IA.
9. **Visualize os resultados:**
    * A resposta gerada pela IA, contendo os dados detalhados extraídos do texto, será exibida na área de texto à direita.

## Observações

* O código foi projetado para extrair dados de imagens em português.
* A qualidade da extração de texto depende da qualidade da imagem e da clareza do texto.
* Certifique-se de ter uma conexão com a internet para utilizar o Google Generative AI.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.