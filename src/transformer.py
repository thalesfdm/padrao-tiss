import csv
from pathlib import Path

import camelot


def run(pages):
    print("> Transformer running...")

    pdf_file = "./data/pdf/padrao_tiss_componente_organizacional_latest.pdf"

    dest_path = "./data/csv/"
    Path(dest_path).mkdir(parents=True, exist_ok=True)

    multi_page = [page for page in pages if "-" in page]
    single_page = [page for page in pages if "-" not in page]

    for interval in multi_page:
        first_page = interval.split("-", 1)[0]
        last_page = interval.split("-", 1)[1]
        first_table = {}
        last_table = {}

        if first_page in single_page:
            first_table = camelot.read_pdf(pdf_file, pages=first_page)._tables[-1]
            interval = f"{int(first_page) + 1}-{last_page}"

        if last_page in single_page:
            last_table = camelot.read_pdf(pdf_file, pages=last_page)._tables[0]
            interval = f"{first_page}-{int(last_page) - 1}"

        tables = camelot.read_pdf(pdf_file, pages=interval, line_scale=30)

        if first_table:
            tables[0].df.append(first_table.df)

        for index, table in enumerate(tables):
            if index == 0:
                continue
            tables[0].df = tables[0].df.append(table.df)

        if last_table:
            tables[0].df = tables[0].df.append(last_table.df)

        tables[0].df.to_csv(
            f"./data/csv/padrao_tiss-page-{first_page}-{last_page}-table-{tables[0].order}.csv",
            index=False,
            header=False,
            quoting=csv.QUOTE_ALL,
        )

    tables = camelot.read_pdf(pdf_file, pages=",".join(single_page), line_scale=30)
    tables.export(dest_path + "padrao_tiss.csv", f="csv")
