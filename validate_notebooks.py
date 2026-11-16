import pathlib,os,json,contextlib,io,traceback
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=pathlib.Path(__file__).resolve().parent;os.chdir(root)
out=root/'artifacts';out.mkdir(exist_ok=True)
results=[]
for p in root.glob('*.ipynb'):
 n=json.loads(p.read_text());ns={};status='PASS';count=0
 try:
  for i,c in enumerate(n['cells']):
   if c['cell_type']!='code':continue
   code=''.join(c['source']);code='\n'.join(x for x in code.splitlines() if not x.startswith('%'))
   capture=io.StringIO()
   with contextlib.redirect_stdout(capture):exec(compile(code,f'{p.name}:cell{i}','exec'),ns)
   count+=1
   for f in plt.get_fignums():plt.figure(f).savefig(out/f'{p.stem}-{i}-{f}.png')
   plt.close('all')
  (out/(p.stem+'.txt')).write_text(str({k:str(v)[:8000] for k,v in ns.items() if k in ['df2','df3','crime_count','season_df']}))
 except Exception:
  status='FAIL';(out/(p.stem+'-error.txt')).write_text(traceback.format_exc());print(traceback.format_exc())
 results.append({'notebook':p.name,'status':status,'cells_executed':count})
print(results);(out/'results.json').write_text(json.dumps(results,indent=2))

assert all(item["status"] == "PASS" for item in results), results
