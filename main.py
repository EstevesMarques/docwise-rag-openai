# main.py

from rag.qa import ask_question

def main():
    print("🔍 Faça uma pergunta sobre os documentos PDF (ou digite 'sair'):\n")
    while True:
        query = input("❓ Pergunta: ")
        if query.lower() in ("sair", "exit", "quit"):
            break
        answer = ask_question(query)
        print(f"\n💬 Resposta: {answer}\n")

if __name__ == "__main__":
    main()
