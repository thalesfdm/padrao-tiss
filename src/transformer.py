import sys
from pathlib import Path

import camelot


def run(*pages):
    print("> Transformer running...")

    pdf_file = "./data/pdf/padrao_tiss_componente_organizacional_latest.pdf"
    tables = camelot.read_pdf(pdf_file, pages=",".join(pages), line_scale=30)

    dest_path = "./data/csv/"
    file_path = dest_path + "padrao_tiss.csv"
    Path(dest_path).mkdir(parents=True, exist_ok=True)

    tables.export(file_path, f="csv")


if __name__ == "__main__":
    run(*sys.argv[1:])
