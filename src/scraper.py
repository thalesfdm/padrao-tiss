from pathlib import Path

from scrapy import Spider
from scrapy.crawler import CrawlerProcess


class PadraoTissSpider(Spider):
    name = "padrao-tiss-spider"

    start_urls = [
        "https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss",
    ]

    def parse(self, response):
        print(f" > Scraping {response.url}")
        next_url = response.css(".alert-link.internal-link").attrib["href"]
        yield response.follow(response.urljoin(next_url), callback=self.parse_next)

    def parse_next(self, response):
        print(f" > Scraping {response.url}")
        pdf_url = response.css(
            ".btn.btn-primary.btn-sm.center-block.internal-link"
        ).attrib["href"]
        yield response.follow(response.urljoin(pdf_url), callback=self.save_pdf)

    def save_pdf(self, response):
        print(f" > Scraping {response.url}")
        dest_path = "./data/pdf/"
        file_path = (
            dest_path + response.url.split("/")[-1].rsplit("_", 1)[0] + "_latest.pdf"
        )
        Path(dest_path).mkdir(parents=True, exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(response.body)
            f.close()


process = CrawlerProcess(
    {"USER_AGENT": "Mozilla/5.0", "ROBOTSTXT_OBEY": False, "LOG_LEVEL": "ERROR"}
)


def run():
    print("> Scraper running...")
    process.crawl(PadraoTissSpider)
    process.start()


if __name__ == "__main__":
    run()
