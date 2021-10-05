import sys
from pathlib import Path

import camelot


def run(*pages):
    print("> Transformer running...")
    pdf_file = "./data/pdf/padrao_tiss_componente_organizacional_latest.pdf"
    tables = camelot.read_pdf(pdf_file, pages=",".join(pages), line_scale=30)

    Path("./data/csv/").mkdir(parents=True, exist_ok=True)

    tables.export("./data/csv/padrao_tiss.csv", f="csv")


if __name__ == "__main__":
    run(*sys.argv[1:])
