# BlackoutPDF: Protótipo Inicial

[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)](https://github.com/seu-usuario/blackoutpdf)
[![Versão](https://img.shields.io/badge/version-0.1.0-blue)](https://github.com/seu-usuario/blackoutpdf/releases)
[![Licença](https://img.shields.io/badge/license-MIT-green)](LICENSE)

O **BlackoutPDF** é uma ferramenta para processamento de arquivos PDF, com foco na detecção e ocultação de **Informações Pessoais Sensíveis (PII)**, como nomes e CPFs. Este projeto é um protótipo inicial para demonstração.

## Funcionalidades
- Recebe arquivos PDF para processamento.
- Remove ou oculta informações de identificação pessoal (PII) como **CPF** e **Nome**.
- Retorna um PDF processado com as informações sensíveis escondidas.
- Fornece a URL do PDF processado, juntamente com o status e a data do processamento.

## Endpoint

### `POST /process-pdf`
Este endpoint recebe um PDF para processamento.

**Request Body (JSON):**
```json
{
  "path": "string (URL para download do PDF)"
}

**Responses**

**200 Successful Response**
```json
{
  "url": "string (URL do PDF processado)",
  "status": true,
  "data": "2025-09-19T01:30:28.644686"
}
