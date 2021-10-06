import sys

from src import scraper, transformer


def main():
    scraper.run()
    transformer.run(sys.argv[1:])


main()
