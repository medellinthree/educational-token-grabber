import os
import re

# 1. Função para procurar "tokens falsos" em arquivos de log simulados
def find_fake_tokens(path):
    # Expressão regular que simula o formato de tokens do Discord
    pattern = r"mfa\.[\w-]{84}|[\w-]{24}\.[\w-]{6}\.[\w-]{27}"
    tokens = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".log") or file.endswith(".ldb"):
                with open(os.path.join(root, file), "r", errors="ignore") as f:
                    content = f.read()
                    found = re.findall(pattern, content)
                    tokens.extend(found)

    return list(set(tokens))  # remove duplicatas


# 2. Função para simular o "envio" dos tokens
def simulate_webhook_send(tokens):
    print("\n[+] Tokens encontrados (simulados):")
    if tokens:
        for token in tokens:
            print(f"- {token}")
    else:
        print("Nenhum token encontrado.")

    print("\n[!] Simulando envio para webhook... (NÃO está sendo enviado de verdade!)")


# 3. Função principal
if __name__ == "__main__":
    folder_to_scan = "./simulated_logs"  # Pasta com arquivos simulados
    tokens = find_fake_tokens(folder_to_scan)
    simulate_webhook_send(tokens)
