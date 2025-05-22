# Educational Token Grabber - BoostFPS Simulator

> Projeto educacional para demonstrar como um token grabber pode funcionar na prática, simulando um falso otimizador de FPS para jogos.

---

## Sobre

Este projeto simula um programa que supostamente melhora o desempenho do PC/games ("BoostFPS"), mas na verdade procura por tokens de autenticação do Discord em arquivos simulados e envia para um webhook.

**Objetivo:**  
Demonstrar de forma didática e segura como funciona a captura e exfiltração de tokens, útil para aprendizado em segurança ofensiva (Red Team) e conscientização.

---

## Funcionalidades

- Interface gráfica simples e convincente simulando otimização de FPS.
- Varredura em arquivos `.log` dentro da pasta `simulated_logs` para capturar tokens.
- Envio automático dos tokens capturados para um webhook Discord configurável.
- Criação da pasta `simulated_logs` caso não exista para simulação.

---

## Como usar

1. Clone ou baixe o projeto.
2. Certifique-se de ter Python 3 instalado.
3. Configure seu webhook Discord no arquivo `app.py` (procure pela variável `webhook_url`).
4. Execute o programa:

