"""Optional historical HTML acquisition; offline notebooks use historical.csv instead."""
import argparse
from pathlib import Path
import pandas as pd
import requests
from bs4 import BeautifulSoup
URL = 'https://markets.financialcontent.com/stocks/quote/historical?Month=11&Range=12&Year=2022&Symbol=537%3A1413346'
def fetch(url=URL):
 response = requests.get(url, timeout=30)
 response.raise_for_status()
 soup = BeautifulSoup(response.text, 'lxml')
 records=[]
 for row in soup.select('tr'):
  cells=[cell.get_text(strip=True) for cell in row.select('td')]
  if len(cells)!=6: continue
  try:
   date=pd.to_datetime(cells[0], errors='raise')
   values=[float(v.replace(',', '').replace('$','')) for v in cells[1:]]
  except (ValueError,TypeError):continue
  records.append([date.date().isoformat(),*values])
 if not records: raise ValueError('No historical price rows found; website layout or availability changed')
 return pd.DataFrame(records,columns=['Date','Open','High','Low','Close','Volume']).sort_values('Date')
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True,type=Path);args=parser.parse_args()
 if args.output.exists():parser.error('Output already exists; choose a new path to preserve existing data')
 fetch().to_csv(args.output,index=False)
