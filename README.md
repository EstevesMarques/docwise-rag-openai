# 📄 DocWise RAG OpenAI

> Um pipeline simples e funcional de Retrieval-Augmented Generation (RAG) para PDFs usando OpenAI, LangChain e FAISS, escrito 100% em Python. Ideal para aprendizado, POCs ou projetos internos.



## 🚀 Visão Geral

**DocWise RAG OpenAI** permite carregar documentos PDF, processá-los com chunking, gerar embeddings com a API da OpenAI e armazenar os vetores localmente usando FAISS. A partir disso, você pode fazer perguntas em linguagem natural e obter respostas baseadas no conteúdo dos documentos.



## 📁 Estrutura do Projeto

```

docwise-rag-openai/
├── .env                      # Variáveis de ambiente (não versionar)
├── requirements.txt          # Dependências do projeto
├── main.py                   # Entrada principal da aplicação (chat de perguntas)
├── ingest.py                 # Script de ingestão de PDFs e criação de índice FAISS
├── config.py                 # Carregamento de configurações do .env
├── rag/                      # Módulos principais do pipeline
│   ├── **init**.py
│   ├── loader.py             # Leitura dos PDFs
│   ├── splitter.py           # Split dos textos em chunks
│   ├── embedder.py           # Criação dos embeddings
│   ├── vectorstore.py        # Armazenamento/recarregamento FAISS
│   └── qa.py                 # Pipeline de perguntas e respostas
├── data/                     # Pasta para armazenar os PDFs
│   └── seu-arquivo.pdf

````



## 🛠️ Pré-Requisitos

- Python 3.10+
- API Key válida da [OpenAI](https://platform.openai.com/account/api-keys)
- Crie um ambiente virtual:

```bash
python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/macOS
````



## 📦 Instalação

Instale as dependências com:

```bash
pip install -r requirements.txt
```



## 🔐 Configuração `.env`

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
OPENAI_LLM_MODEL=gpt-4o  # ou gpt-3.5-turbo, gpt-4, etc.
DATA_DIR=data
CHUNK_SIZE=500
CHUNK_OVERLAP=50
```

> ⚠️ Nunca compartilhe sua API Key pública ou versionada!



## 🧠 Pipeline de Ingestão

Este processo carrega os PDFs da pasta `data/`, divide o conteúdo em chunks e gera os embeddings que serão salvos no índice local (`faiss_index/`):

```bash
python ingest.py
```



## 💬 Interagindo com o Assistente

Após a ingestão, execute:

```bash
python main.py
```

Você verá o prompt interativo:

```
🔍 Faça uma pergunta sobre os documentos PDF (ou digite 'sair'):

❓ Pergunta:
```

Digite qualquer pergunta em linguagem natural com base nos documentos PDF carregados. Exemplo:

```
❓ Pergunta: Qual o prazo para entrega da proposta?
```



## 🧪 Exemplos de Perguntas

* "Quais são os critérios de avaliação da RFP?"
* "A proposta deve ser enviada por e-mail ou sistema?"
* "Existe alguma exigência de certificação técnica?"
* "Qual o valor estimado do contrato?"



## 🧰 Tecnologias Utilizadas

* [LangChain](https://python.langchain.com/)
* [OpenAI API](https://platform.openai.com/)
* [FAISS](https://github.com/facebookresearch/faiss)
* [PyPDF2](https://github.com/py-pdf/PyPDF2)
* [dotenv](https://pypi.org/project/python-dotenv/)



## 🧼 Limpeza e Reindexação

Se desejar reprocessar os PDFs (por exemplo, após atualizar os arquivos), exclua o diretório `faiss_index/`:

```bash
rm -rf faiss_index/
```

E execute novamente:

```bash
python ingest.py
```



## ⚠️ Avisos

* Este projeto usa **deserialização com Pickle** para FAISS, o que **deve ser evitado com fontes não confiáveis**. Use `allow_dangerous_deserialization=True` **somente se você confia na origem do índice FAISS.**
* É um projeto educacional/demonstrativo, **não recomendado para produção sem adaptações.**



## 🧭 Próximos Passos (Sugestões)

* ✅ Suporte a múltiplos arquivos PDF
* 📊 Interface web com Streamlit ou Gradio
* 🌍 Suporte multilíngue
* 🔐 Controle de acesso e histórico de perguntas
* ☁️ Armazenamento vetorial remoto (ex: Weaviate, Pinecone, Azure AI Search)



## 📖 Licença

MIT License — sinta-se à vontade para clonar, estudar e adaptar!



## ✍️ Autor

Esteves Marques — [iaplaybook.tech](https://iaplaybook.tech)
Siga a jornada no LinkedIn: [@estevesmarques](https://linkedin.com/in/estevesmarques)
