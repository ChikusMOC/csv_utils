from pathlib import Path
import pandas as pd
from io import StringIO


class CSVIngestionError(Exception):
    """Erro específico para problemas na ingestão de CSV."""
    pass


def _remover_byte_invalido(content: bytes) -> bytes:
    if content.startswith(b'\xff') and not content.startswith(b'\xff\xfe'):
        return content[1:]
    return content


def _padronizar_para_utf8(content: bytes) -> str:
    try:
        return content.decode("utf-8")
    except UnicodeDecodeError:
        return content.decode("iso-8859-1")


def carregar_csv(path: str | Path, sep: str = ";") -> pd.DataFrame:
    """
    Lê CSV com possíveis problemas de encoding.
    
    Args:
        path: caminho para o arquivo CSV
        sep: separador do CSV (padrão ';')
    
    Returns:
        pd.DataFrame limpo
    """
    path = Path(path)

    if not path.exists():
        raise CSVIngestionError(f"Arquivo não encontrado: {path}")

    with open(path, "rb") as f:
        content = f.read()

    content = _remover_byte_invalido(content)
    texto = _padronizar_para_utf8(content)

    df = pd.read_csv(StringIO(texto), sep=sep)
    return df