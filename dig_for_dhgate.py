#!/usr/bin/env python
#encoding=utf-8
#coding by yangzhou 2015-07-13

import os,sys
import time
import urllib2,urllib

g_totalFeedback = 0
g_totalDigFeedback = {}

g_Code2Desc = {
	"ao":"������",\
	"af":"������",\
	"al":"����������",\
	"dz":"����������",\
	"ad":"���������͹�",\
	"ai":"��������",\
	"ag":"����ϺͰͲ���",\
	"ar":"����͢",\
	"am":"��������",\
	"ac":"��ɭ��",\
	"au":"�Ĵ�����",\
	"at":"�µ���",\
	"az":"�����ݽ�",\
	"bs":"�͹���",\
	"bh":"����",\
	"bd":"�ϼ�����",\
	"bb":"�ͰͶ�˹",\
	"by":"�׶���˹",\
	"be":"����ʱ",\
	"bz":"������",\
	"bj":"����",\
	"bm":"��Ľ��Ⱥ��",\
	"bo":"����ά��",\
	"bw":"��������",\
	"br":"����",\
	"bn":"����",\
	"bg":"��������",\
	"bf":"�����ɷ���",\
	"mm":"���",\
	"bi":"��¡��",\
	"cm":"����¡",\
	"ca":"���ô�",\
	"ky":"����Ⱥ��",\
	"cf":"�зǹ��͹�",\
	"td":"է��",\
	"cl":"����",\
	"cn":"�й�",\
	"co":"���ױ���",\
	"cg":"�չ�",\
	"ck":"���Ⱥ��",\
	"cr":"��˹�����",\
	"cu":"�Ű�",\
	"cy":"����·˹",\
	"cz":"�ݿ�",\
	"dk":"����",\
	"dj":"������",\
	"do":"������ӹ��͹�",\
	"ec":"��϶��",\
	"eg":"����",\
	"sv":"�����߶�",\
	"ee":"��ɳ����",\
	"et":"���������",\
	"fj":"쳼�",\
	"fi":"����",\
	"fr":"����",\
	"gf":"����������",\
	"ga":"����",\
	"gm":"�Ա���",\
	"ge":"��³����",\
	"de":"�¹�",\
	"gh":"����",\
	"gi":"ֱ������",\
	"gr":"ϣ��",\
	"gd":"�����ɴ�",\
	"gu":"�ص�",\
	"gt":"Σ������",\
	"gn":"������",\
	"gy":"������",\
	"ht":"����",\
	"hn":"�鶼��˹",\
	"hk":"���",\
	"hu":"������",\
	"is":"����",\
	"in":"ӡ��",\
	"id":"ӡ��������",\
	"ir":"����",\
	"iq":"������",\
	"ie":"������",\
	"il":"��ɫ��",\
	"it":"�����",\
	"ci":"���ص���",\
	"jm":"�����",\
	"jp":"�ձ�",\
	"jo":"Լ��",\
	"kh":"����կ",\
	"kz":"������˹̹",\
	"ke":"������",\
	"kr":"����",\
	"kw":"������",\
	"kg":"������˹̹",\
	"la":"����",\
	"lv":"����ά��",\
	"lb":"�����",\
	"ls":"������",\
	"lr":"��������",\
	"ly":"������",\
	"li":"��֧��ʿ��",\
	"lt":"������",\
	"lu":"¬ɭ��",\
	"mo":"����",\
	"mg":"����˹��",\
	"mw":"����ά",\
	"my":"��������",\
	"mv":"�������",\
	"ml":"����",\
	"mt":"�����",\
	"mp":"��������Ⱥ��",\
	"mq":"�������",\
	"mu":"ë����˹",\
	"mx":"ī����",\
	"md":"Ħ������",\
	"mc":"Ħ�ɸ�",\
	"mn":"�ɹ�",\
	"ms":"���������ص�",\
	"ma":"Ħ���",\
	"mz":"Īɣ�ȿ�",\
	"na":"���ױ���",\
	"nr":"�³",\
	"np":"�Ჴ��",\
	"ats":"����������˹Antilles",\
	"nl":"����",\
	"nz":"������",\
	"ni":"�������",\
	"ne":"���ն�",\
	"ng":"��������",\
	"kp":"����",\
	"no":"Ų��",\
	"om":"����",\
	"pk":"�ͻ�˹̹",\
	"pa":"������",\
	"pg":"�Ͳ����¼�����",\
	"py":"������",\
	"pe":"��³",\
	"ph":"���ɱ�",\
	"pl":"����",\
	"pf":"��������������",\
	"pt":"������",\
	"pr":"�������",\
	"qa":"������",\
	"re":"������",\
	"ro":"��������",\
	"ru":"����˹",\
	"lc":"ʥ¬����",\
	"vc":"ʥ��ɭ�ص�",\
	"as":"����Ħ��(��)",\
	"ws":"����Ħ��",\
	"sm":"ʥ����ŵ",\
	"st":"ʥ��������������",\
	"sa":"ɳ�ذ�����",\
	"sn":"���ڼӶ�",\
	"sc":"�����",\
	"sl":"��������",\
	"sg":"�¼���",\
	"sk":"˹�工��",\
	"si":"˹��������",\
	"sb":"������Ⱥ��",\
	"so":"������",\
	"za":"�Ϸ�",\
	"es":"������",\
	"lk":"˹������",\
	"lc":"ʥ¬����",\
	"vc":"ʥ��ɭ��",\
	"sd":"�յ�",\
	"sr":"������",\
	"sz":"˹��ʿ��",\
	"se":"���",\
	"ch":"��ʿ",\
	"sy":"������",\
	"tw":"̨��ʡ",\
	"tj":"������˹̹",\
	"tz":"̹ɣ����",\
	"th":"̩��",\
	"tg":"���",\
	"to":"����",\
	"tt":"�������Ͷ�͸�",\
	"tn":"ͻ��˹",\
	"tr":"������",\
	"tm":"������˹̹",\
	"ug":"�ڸɴ�",\
	"ua":"�ڿ���",\
	"ae":"����������������",\
	"gb":"Ӣ��",\
	"us":"����",\
	"uy":"������",\
	"uz":"���ȱ��˹̹",\
	"ve":"ί������",\
	"vn":"Խ��",\
	"ye":"Ҳ��",\
	"yu":"��˹����",\
	"zw":"��Ͳ�Τ",\
	"zr":"������",\
	"zm":"�ޱ���",\
}
def GetUrlContent(url, splitResult=True):
	resp = None
	try:
		req  = urllib2.Request(url)
		resp = urllib2.urlopen(req)
	except Exception,e:
		if splitResult:
			return []
		else:
			return ""
	if splitResult:
		return resp.read().split("\n")
	else:
		return resp.read()
		


class DigDHGate:
	def __init__(self, keywords, NResult=50, NFeedback=50):

		self.keywords = keywords
		self.keywords_list = []
		self.processKeyWords()

		self.result   = {}
		if NResult > 0 and NResult < 100:
			self.maxSearchResult = NResult
		else:
			self.maxSearchResult = 50

		if NFeedback > 0 and NFeedback < 200:
			self.maxFeedback     = NFeedback
		else:
			self.maxFeedback     = 50

	def processKeyWords(self):
		if os.path.isfile(self.keywords):
			fd = file(self.keywords)
			kset = set()
			for line in fd:
				k = line.strip().replace("\r","").replace("\t","").replace(",","")
				kset.add(k)
			fd.close()

			if len(kset) > 0:
				self.keywords_list = list(kset)
		else:
			self.keywords_list = [self.keywords.strip().replace("\r","").replace("\t","").replace(",",""),]

	def RecursiveGetSearchResult(self, keywords):
		searchResult = set()
		for i in range(0, 1000):
			result = self.GetSearchResultWithPageNum(keywords, i)
			if len(result) == 0:
				break
			oldlen = len(searchResult)
			searchResult.update(result)
			newlen = len(searchResult)
			#print oldlen, newlen
			if (oldlen != 0 and oldlen == newlen ) or \
				len(searchResult) > self.maxSearchResult:
				break
		return list(searchResult)

	def GetSearchResultWithPageNum(self, keywords, pageNum=0):
		#url="http://www.aliexpress.com/premium/%s.html?site=glo&g=y&SearchText=%s&page=%d&shipCountry=all&prNum=42&needQuery=n"
		#url = "http://www.aliexpress.com/wholesale?catId=66&initiative_id=AS_20150711031558&SearchText=sex+products"
		#url = "http://www.dhgate.com/wholesale?SearchText=%s&shipcountry=all&page=%d"%(keywords, pageNum)
		if pageNum == 0:
			url = "http://www.dhgate.com/w/%s.html?pagesize=48"%(keywords)
		else:
			url = "http://www.dhgate.com/w/%s/%d.html?pagesize=48"%(keywords, pageNum)

		#print url
		buff = GetUrlContent(url)
		result = set()
		#pattern = "<a class=\"history-item product \""
		pattern = " class=\"subject\">"
		resultCounter = 0
		for line in buff:
			if resultCounter >= 48:break;
			if pattern in line:
				pattern2 = " href=\""
				start_pos = line.find(pattern2)
				if start_pos > 0:
					start_pos = start_pos + len(pattern2)
					stop_pos = line.find("\"", start_pos)
					if stop_pos > 0:
						search_result_url = line[start_pos:stop_pos]
						result.add(search_result_url)
						resultCounter += 1
		return result

	def GetProductFeedbackURL(self, url):
		#url="http://www.dhgate.com/product/w273-sports-mp3-player-headset-8gb-wireless/215028008.html#s2-0-1b|3069859691"

		buff = GetUrlContent(url)
		pattern = "<div id=\"transactionHistoryWarp\" init-src=\""
		feedbackURL = ""
		for line in buff:
			start_pos = line.find(pattern)
			if start_pos > 0:
				start_pos = start_pos + len(pattern)
				stop_pos = line.find("\"", start_pos)
				if stop_pos > 0:
					feedbackURL = line[start_pos:stop_pos].strip()
				return feedbackURL
		return feedbackURL
				
	def GetFeedbackCountryList(self, url):
		countryList = []
		feedbackURL = self.GetProductFeedbackURL(url)
		if len(feedbackURL) <= 7: 
			return countryList
		totalPage = -1
		#print url
		for i in range(1,100):
			if totalPage != -1 and i > totalPage:
				break
			tm = int(time.time() * 1000)
			newFeedbackURL = "%s&page=%d&_=%d"%(feedbackURL, i, tm);
			#print url,newFeedbackURL
			buff = GetUrlContent(newFeedbackURL)
			feedbackCounter = 0
			pattern = "img src=\"http://image.dhgate.com/images/flag/"
			pattern2 = "<span><strong>Page"
			pattern3 = "</strong> of <strong>"
			for line in buff:
				start_pos = line.find(pattern)
				if start_pos > 0:
					#print line
					start_pos = start_pos + len(pattern)
					stop_pos = line.find(".", start_pos)
					if stop_pos > 0:
						code = line[start_pos:stop_pos]
						if len(code) == 2:
							countryList.append(code.lower())
							feedbackCounter += 1
				else:
					if totalPage == -1:
						start_pos = line.find(pattern2)
						if start_pos >= 0:
							#print line
							start_pos = start_pos + len(pattern2)
							start_pos = line.find(pattern3, start_pos)
							if start_pos >= 0:
								start_pos = start_pos + len(pattern3)
								stop_pos = line.find("</strong>", start_pos)
								#print stop_pos
								if stop_pos > 0:
									code = line[start_pos:stop_pos].strip()
									if code.isdigit() :
										totalPage = int(code)
										#print "totalPage:",totalPage
								
				if len(countryList) > self.maxFeedback:
					break

				if feedbackCounter >= 8:
					break
			if feedbackCounter == 0:
				return countryList
		#print len(countryList)
		return countryList
					
				
	def GetFeedbackInfo(self, url):
		result = ["",-1]
		pattern1 = "iframe "
		pattern2 = "thesrc=\"http://feedback.aliexpress.com/display/productEvaluation.htm"
		pattern3 = "<a href=\"javascript:void(0)\">Feedback ("
		for line in buff:
			pos = line.find(pattern3)
			if pos >= 0:
				start_pos = pos + len(pattern3)
				stop_pos  = line.find(")", start_pos)
				feedback_count_str = line[start_pos:stop_pos]
				try:
					feedback_count = int(feedback_count_str)
				except Exception,e:
					feedback_count = -1
				result[1] = feedback_count
			else:		
				if pattern1 in line :
					start_pos = line.find(pattern2)
					if start_pos > 0:
						start_pos = start_pos + 8
						stop_pos  = line.find("\"", start_pos)
						if stop_pos > 0:
							feedback_url = line[start_pos:stop_pos]
							result[0] = feedback_url
							
			if result[0] != "" and result[1] != 0:
				return result
		return result

	def GetFeedbackCountryListN2(self, url):
		global g_totalFeedback
		feedbackInfo = self.GetFeedbackInfo(url)
		feedbackUrl  = feedbackInfo[0]
		if len(feedbackUrl) < 9 or feedbackInfo[1] <= 0:
			return []
		g_totalFeedback += feedbackInfo[1]
		buff = GetUrlContent(feedbackUrl)
		country_list = []
		pattern1 = "<span class=\"state\"><b class=\"css_flag css_"
		for line in buff:
			pos = line.find(pattern1)
			if pos >= 0:
				start_pos = pos + len(pattern1)
				stop_pos  = line.find("\"", start_pos)
				if stop_pos > 0:
					country = line[start_pos:stop_pos]
					if len(country) == 2:
						country_list.append(country)
		#print url,feedbackUrl,feedbackInfo[1],country_list
		return country_list

	def Stat(self, countryList, keywords):
		global g_totalDigFeedback
		for code in countryList:
			if g_totalDigFeedback.has_key(keywords): 
				g_totalDigFeedback[keywords]+= 1
			else:
				g_totalDigFeedback[keywords] = 1

			if self.result.has_key(code):
				if self.result[code].has_key(keywords):
					self.result[code][keywords] += 1
				else:
					self.result[code][keywords] = 1
			else:
				self.result[code] = {keywords:1}

	def PrintResult(self):
		global g_totalDigFeedback,g_totalFeedback
		newmap = sorted(self.result.iteritems(), key=lambda d:d[1], reverse=False)
		#for country,count in self.result.iteritems():
		self.outdir = "./result"
		self.outMode = "file"
		if os.path.isdir(self.outdir) is False:
			try:
				os.makedirs(self.outdir)
			except Exception,e:
				pass
			if os.path.isdir(self.outdir) is False:
				self.outMode = "stdout"
		title = ',ռ��,'.join(self.keywords_list)
		title += ",ռ��"
		buff = "����,%s\n"%(title)

		for country,info in self.result.iteritems():
			temp = ""
			for k in self.keywords_list:
				count = info.get(k, 0)
				total = g_totalDigFeedback.get(k,0)
				if total != 0:
					temp += "%d,%.02f%%,"%(count, float(count)/total*100)
				else:
					temp += "0,0.00%%,"
			buff += "%s,%s\n"%(g_Code2Desc.get(country,"NULL"), temp[:-1])

		temp = ""
		for k in self.keywords_list:
				total = g_totalDigFeedback.get(k,0)
				temp += "%d,100.00%%,"%(total)
		buff += "����,%s\n"%(temp[:-1])

		if self.outMode == "file":
			self.outfile = "%s/%s.result.csv"%(self.outdir, time.strftime("%Y%m%d_%H_%M", time.localtime()))
			fd = file(self.outfile, "w")
			fd.write(buff)
			fd.close()
		else:
			print buff.replace(",","\t")

	def Do(self):
		for keywords in self.keywords_list:
			searchWords = keywords.replace(" ", "+")
			searchResult = self.RecursiveGetSearchResult(searchWords)
			print "search keywords \" %s \" get %d products"%(keywords, len(searchResult))
			if len(searchResult) == 0:
				return 
			for url in searchResult:
				c = self.GetFeedbackCountryList(url)
				self.Stat(c, keywords)
		self.PrintResult()
		return

def Usage():
	print ""
	print "%s key_words|key_words_file [top_N_result] [top_N_feedback]"%(sys.argv[0])
	print ""
	return

if __name__ == "__main__" :
	if len(sys.argv) < 2 :
		Usage()
		sys.exit(1)
	NResult   = 50
	NFeedback = 50
	try:
		NResult = int(sys.argv[2])
		NFeedback = int(sys.argv[3])
	except Exception,e:
		pass
	dh = DigDHGate(sys.argv[1], NResult, NFeedback)
	dh.Do()
