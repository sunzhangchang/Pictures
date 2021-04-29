#%%
import requests as req
from bs4 import BeautifulSoup as BS
urlh = 'http://tb2.bdstatic.com/tb/editor/images/qpx_n/b'
urlt = '.gif?t=20140803'
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'}
for i in range(1,151):
	stri = str(i)
	if i < 10:
		stri = '0'+stri
	url = urlh+stri+urlt
	res = req.get(url=url,headers=head)
	img = res.content
	with open('b'+stri+'.gif','wb') as f:
		f.write(img)
# %%
