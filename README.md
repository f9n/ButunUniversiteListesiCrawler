# ButunUniversiteListesiCrawler
Turkiyedeki tum universiteler, Data'nin cekildigi site: https://yoksis.yok.gov.tr/websitesiuygulamalari/harita/

# Kurulum ve Calistirma

```bash
        $ git clone https://github.com/pleycpl/ButunUniversiteListesiCrawler
        $ cd ButunUniversiteListesiCrawler
        $ virtualenv3 crawler/venv
        $ source crawler/venv/bin/active
  (venv)$ pip3 install -r crawler/requirements.txt
  (venv)$ # Crawler'i baslatma
  (venv)$ python3 crawler/main.py
        ...
        ...
  (venv)$ deactive
        $ # settings.py dosyasini degistirme
        $ ./textmanipulating/main.sh
```
