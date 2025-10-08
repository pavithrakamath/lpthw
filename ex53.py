import json
from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
import os

from ex51 import get_data_from_pdf


def download_pdf(pdf_url:str, pdf_name:str):
    with requests.get(pdf_url) as response:
        with open(pdf_name, "wb") as f:
            f.write(response.content)

def download_all_pdfs():
    url:str = "https://learncodethehardway.com/setup/python/ttb"
    base_url:str = "https://learncodethehardway.com"
    with requests.get(url) as response:
        soup = BeautifulSoup(response.text, "html.parser")
        anchors = soup.select("a[href*='.pdf']")
        print(f"Found {len(anchors)} pdfs for download")
    for anchor in anchors:
        href = anchor.get("href") if anchor.get("href") is not None else ""
        if href is not None and ".pdf" in href:
            pdf_name = anchor.text
            download_pdf(base_url+href, pdf_name)
            
if __name__ == "__main__":
    report_data:list[dict[str, str|int]] = []
    if(os.path.exists("report_data.json")==False):
        download_all_pdfs()
    for pdf_name in os.listdir("."):
        if pdf_name is not None:
          if ".pdf" in pdf_name:
            report_data.append(get_data_from_pdf(pdf_name))
    with open("report_data.json", "w") as f:
        json.dump(report_data, f)