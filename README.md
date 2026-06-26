# JARVIS Platform

Plataforma de leitura de fluxo de ordens. EA leitor (MT5) → backend → IA (Claude) → interface HUD.

## Estrutura
- `app.py` — backend Flask (endpoints do EA, do site e da IA)
- `templates/index.html` — home page (núcleo JARVIS)
- `templates/plataforma.html` — painel de dados em tempo real
- `render.yaml` — config de deploy

## Como subir no Render
1. Suba esta pasta no seu repositório GitHub.
2. No Render: New → Web Service → conecte o repositório.
3. Render detecta o `render.yaml` e configura sozinho. Confirme.
4. Pronto: o site fica no ar em modo demonstração (IA desligada).

## Ligar a IA (quando quiser)
No painel do Render → seu serviço → Environment → Add Environment Variable:
- Key: `ANTHROPIC_API_KEY`
- Value: sua chave da Anthropic

Salve. O Render reinicia e a IA liga sozinha.

## Conectar o EA
No MQL5, envie via WebRequest() um POST para `/api/leitura`:
```json
{ "simbolo": "BTCUSD", "dados": { "cvd_zscore": 1.84, "semi_variancia": 0.42 } }
```
Libere a URL do Render em Ferramentas → Opções → Expert Advisors → WebRequest.
