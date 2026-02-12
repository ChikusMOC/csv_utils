# CSV Utils

Módulo Python para ingestão robusta de arquivos CSV, com tratamento de encoding e bytes inválidos.

##  Objetivo

Facilitar a leitura de arquivos CSV problemáticos, evitando erros comuns relacionados a encoding (UTF-8, Latin-1, etc.) e caracteres corrompidos.

##  Funcionalidades

- Leitura segura de arquivos CSV
- Tratamento automático de encoding
- Ignora ou corrige bytes inválidos
- Estrutura modular e reutilizável

##  Exemplo de uso

```python
from ingestao import carregar_csv

df = carregar_csv("dados.csv")
print(df.head())
