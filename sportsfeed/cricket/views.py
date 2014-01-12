from django.shortcuts import render
import urllib2,json
# Create your views here.
url = "http://cricscore-api.appspot.com/csa"
def index(request):
	
	req = urllib2.urlopen(url);
	page = req.read()
	page_json = json.loads(page)
	ids=[]
	for match in page_json:
		if match['t1']=="England" or match['t1']=="Australia" or match['t1']=="England" or match['t1']=="India" \
		or match['t1']=="South Africa" or match['t1']=="New Zealand" or match['t1']=="Sri Lanka" or match['t1']=="West Indies":
			ids.append(str(match['id']))
		elif match['t2']=="England" or match['t2']=="Australia" or match['t2']=="England" or match['t2']=="India" or \
		match['t2']=="South Africa" or match['t2']=="New Zealand" or match['t2']=="Sri Lanka" or match['t2']=="West Indies":
			ids.append(str(match['id']))

	param = ""
	for i in ids:
		param += i+"+"

	url_imp = url+"?id="+param[:(len(param)-1)]
	print url_imp
	req_imp = urllib2.urlopen(url_imp)
	page_imp = req_imp.read()
	page_json_imp = json.loads(page_imp)	
	return render(request,'cricket/index.html',{'match_info':page_json,'imp_match':page_json_imp})	

def localmatch(request,l_id):
	l_url = url + "?id=" + str(l_id)
	l_req = urllib2.urlopen(l_url)
	l_page = l_req.read()
	l_page_json = json.loads(l_page)
	print l_url
	print l_page_json
	return render(request,'cricket/localmatch.html',{'l_match_info':l_page_json}) 