# Azure Document Fraud Detection

Projeto para análise de documentos usando Azure AI e detecção de fraudes.

## Funcionalidades

1. Carregamento de documentos no Blob Storage.
2. Análise de dados com Azure Form Recognizer.
3. Detecção de padrões de fraude.
4. Treinamento de modelos para previsão.

## Como Usar

### Configurar Credenciais

Edite o arquivo `config/config.json`.

### Rodar o Pipeline

1. `upload_documents.py` para enviar arquivos.
2. `analyze_document.py` para análise.
3. `preprocess_data.py` para identificar alertas.
4. `send_alerts.py` para notificação.
