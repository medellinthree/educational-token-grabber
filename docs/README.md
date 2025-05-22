🎯 Educational Token Grabber — Projeto Simulado

Este projeto demonstra **como ferramentas maliciosas podem ser disfarçadas** com interfaces legítimas para capturar tokens de autenticação de usuários. Ele foi desenvolvido **exclusivamente para fins educacionais** — como simulação e conscientização sobre segurança digital.

> ⚠️ **ATENÇÃO:** Este projeto não deve ser usado para fins maliciosos. Toda a execução e análise devem ser feitas em ambientes controlados (VMs, sandboxes, laboratórios de teste).

---

📦 Sobre o Projeto

- 🧠 **Objetivo:** Demonstrar técnicas comuns usadas em ataques de engenharia social (como executáveis disfarçados).
- 🛠️ **Tecnologia:** Python + Tkinter (interface gráfica).
- 🧪 **Simulação:** Tokens são extraídos de arquivos `.log` fictícios e enviados a um webhook configurado.

---

🖼️ Interface

A aplicação se apresenta como um otimizador de desempenho ("BoostFPS") com barra de progresso e botão "Otimizar FPS". Ao ser executada, simula ações e coleta dados de logs falsos.

---

📁 Estrutura da Pasta

educational-token-grabber/
├── build/ # Arquivos temporários gerados na build
├── dist/ # Contém o executável final
├── screenshots/ # Imagens da interface do programa
├── simulated_logs/ # Logs simulados que contêm tokens falsos
├── app.py # Interface principal (BoostFPS)
├── grabber.py # Script alternativo (linha de comando)
├── icone.ico # Ícone usado no executável
├── readme.md # Este arquivo
├── defenses.md # Como se proteger de ferramentas desse tipo
└── tokens_encontrados.txt # Gerado após execução, com tokens simulados

---

🚀 Como Executar

🔧 Pré-requisitos
- Python 3.10+
- `requests` instalado (`pip install requests`)

▶️ Executando como script
```bash
python app.py

🧊 Gerando o Executável
Use o PyInstaller com suporte a ícone:

pyinstaller --noconsole --icon=icone.ico app.py
O executável será gerado na pasta dist/.

---

🌐 Envio para Webhook
Se tokens simulados forem encontrados, eles serão enviados para o webhook especificado no código (app.py), dentro da função enviar_para_webhook():

webhook_url = "https://discord.com/api/webhooks/..."
📌 Recomendação: use uma instância de Discord separada em uma VM para capturar os testes.

---

👤 Autor
Desenvolvido por F. Alexander
📚 Estudante de Cybersecurity | Foco em Red Team

⚖️ Licença
Este projeto é distribuído apenas para fins educacionais e de conscientização. Qualquer uso indevido é de responsabilidade do usuário.








