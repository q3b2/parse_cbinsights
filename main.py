def parse_table2xlsx(url: str = "https://www.cbinsights.com/research-unicorn-companies"):
    import pandas
    try:
        tables = pandas.read_html(url)
        tables[0].to_excel("./table.xlsx")
        return 0
    except:
        return -1


def main():
    import time
    while True:
        parse_table2xlsx()
        time.sleep(3600)


if __name__ == "__main__":
    main()
