# 📄 defenses.md — Como se Proteger de Token Grabbers e Ferramentas Simuladas

> Este projeto é educacional. O conteúdo abaixo detalha como mitigar riscos relacionados a ferramentas que tentam capturar tokens de autenticação do Discord (ou outras plataformas). Essas recomendações servem para **usuários finais, administradores de sistemas e profissionais de segurança**.

---

## 🔐 1. Use Autenticação de Dois Fatores (2FA)

- Ative o 2FA em **todas as contas importantes**, especialmente em serviços como Discord, Google, e redes sociais.
- Mesmo que um token seja capturado, o invasor **não conseguirá acessar a conta** sem o código 2FA.
- Use aplicativos como **Authy, Google Authenticator ou Microsoft Authenticator** para armazenar os códigos 2FA com segurança.

---

## 🧠 2. Conscientização do Usuário

- **Desconfie de programas com promessas exageradas**, como "aumentar o FPS", "desbloquear funções secretas", "créditos grátis", etc.
- Nunca execute arquivos recebidos por DM, e-mail ou baixados de fontes não oficiais.
- Muitos malwares se disfarçam com **ícones familiares e nomes chamativos** (ex: `boostFPS.exe`, `nitro_boost.exe`).

---

## 🖥️ 3. Use Antivírus e Proteção em Tempo Real

- Mantenha um **antivírus confiável** ativado (Windows Defender, Kaspersky, Bitdefender, etc.).
- Ative o recurso de **proteção contra acesso à pasta** (Folder Access Protection) no Windows Defender.
- Bloqueie scripts e executáveis em diretórios como `Downloads`, `Temp`, e `%APPDATA%`.

---

## 🧼 4. Cuidados com Logs e Arquivos Sensíveis

- Nunca armazene tokens de autenticação ou credenciais em **arquivos `.log`, `.txt` ou `.json`**.
- Faça limpeza periódica de caches e pastas temporárias:
  - `%AppData%`
  - `%LocalAppData%`
  - `Temp`

---

## 📊 5. Monitoramento e Auditoria

- Em ambientes corporativos, use ferramentas de auditoria para **detectar execução de binários desconhecidos**.
- Soluções como EDR (Endpoint Detection & Response) ajudam a identificar comportamentos anômalos.
- Monitorar o tráfego de rede também pode ajudar a identificar **exfiltração de tokens** via webhooks ou HTTP.

---

## 🚫 6. Bloqueie Webhooks Externos (em redes corporativas)

- Configure firewalls ou soluções de rede para **bloquear conexões HTTP para `discord.com/api/webhooks`**.
- Essa simples medida pode prevenir que tokens coletados sejam enviados a um invasor.

---

## 🔒 7. Práticas para Desenvolvedores

- Nunca exponha tokens de API ou informações sensíveis em logs.
- Obfusque ou criptografe dados sensíveis em ambientes de produção.
- Use variáveis de ambiente e gerenciamento seguro de segredos.

---

## ✅ Conclusão

Embora esse projeto tenha fins educativos, ele representa uma técnica real usada em ataques. A melhor defesa é a combinação de **conhecimento, vigilância e tecnologia adequada**.
