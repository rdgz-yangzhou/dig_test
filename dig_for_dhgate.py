#!/usr/bin/env python
#encoding=utf-8
#coding by yangzhou 2015-07-13

import os,sys
import time
import urllib2,urllib

g_totalFeedback = 0
g_totalDigFeedback = {}

g_Code2Desc = {
	"ao":"安哥拉",\
	"af":"阿富汗",\
	"al":"阿尔巴尼亚",\
	"dz":"阿尔及利亚",\
	"ad":"安道尔共和国",\
	"ai":"安圭拉岛",\
	"ag":"安提瓜和巴布达",\
	"ar":"阿根廷",\
	"am":"亚美尼亚",\
	"ac":"阿森松",\
	"au":"澳大利亚",\
	"at":"奥地利",\
	"az":"阿塞拜疆",\
	"bs":"巴哈马",\
	"bh":"巴林",\
	"bd":"孟加拉国",\
	"bb":"巴巴多斯",\
	"by":"白俄罗斯",\
	"be":"比利时",\
	"bz":"伯利兹",\
	"bj":"贝宁",\
	"bm":"百慕大群岛",\
	"bo":"玻利维亚",\
	"bw":"博茨瓦纳",\
	"br":"巴西",\
	"bn":"文莱",\
	"bg":"保加利亚",\
	"bf":"布基纳法索",\
	"mm":"缅甸",\
	"bi":"布隆迪",\
	"cm":"喀麦隆",\
	"ca":"加拿大",\
	"ky":"开曼群岛",\
	"cf":"中非共和国",\
	"td":"乍得",\
	"cl":"智利",\
	"cn":"中国",\
	"co":"哥伦比亚",\
	"cg":"刚果",\
	"ck":"库克群岛",\
	"cr":"哥斯达黎加",\
	"cu":"古巴",\
	"cy":"塞浦路斯",\
	"cz":"捷克",\
	"dk":"丹麦",\
	"dj":"吉布提",\
	"do":"多米尼加共和国",\
	"ec":"厄瓜多尔",\
	"eg":"埃及",\
	"sv":"萨尔瓦多",\
	"ee":"爱沙尼亚",\
	"et":"埃塞俄比亚",\
	"fj":"斐济",\
	"fi":"芬兰",\
	"fr":"法国",\
	"gf":"法属圭亚那",\
	"ga":"加蓬",\
	"gm":"冈比亚",\
	"ge":"格鲁吉亚",\
	"de":"德国",\
	"gh":"加纳",\
	"gi":"直布罗陀",\
	"gr":"希腊",\
	"gd":"格林纳达",\
	"gu":"关岛",\
	"gt":"危地马拉",\
	"gn":"几内亚",\
	"gy":"圭亚那",\
	"ht":"海地",\
	"hn":"洪都拉斯",\
	"hk":"香港",\
	"hu":"匈牙利",\
	"is":"冰岛",\
	"in":"印度",\
	"id":"印度尼西亚",\
	"ir":"伊朗",\
	"iq":"伊拉克",\
	"ie":"爱尔兰",\
	"il":"以色列",\
	"it":"意大利",\
	"ci":"科特迪瓦",\
	"jm":"牙买加",\
	"jp":"日本",\
	"jo":"约旦",\
	"kh":"柬埔寨",\
	"kz":"哈萨克斯坦",\
	"ke":"肯尼亚",\
	"kr":"韩国",\
	"kw":"科威特",\
	"kg":"吉尔吉斯坦",\
	"la":"老挝",\
	"lv":"拉脱维亚",\
	"lb":"黎巴嫩",\
	"ls":"莱索托",\
	"lr":"利比里亚",\
	"ly":"利比亚",\
	"li":"列支敦士登",\
	"lt":"立陶宛",\
	"lu":"卢森堡",\
	"mo":"澳门",\
	"mg":"马达加斯加",\
	"mw":"马拉维",\
	"my":"马来西亚",\
	"mv":"马尔代夫",\
	"ml":"马里",\
	"mt":"马耳他",\
	"mp":"马里亚那群岛",\
	"mq":"马提尼克",\
	"mu":"毛里求斯",\
	"mx":"墨西哥",\
	"md":"摩尔多瓦",\
	"mc":"摩纳哥",\
	"mn":"蒙古",\
	"ms":"蒙特塞拉特岛",\
	"ma":"摩洛哥",\
	"mz":"莫桑比克",\
	"na":"纳米比亚",\
	"nr":"瑙鲁",\
	"np":"尼泊尔",\
	"ats":"荷属安的列斯Antilles",\
	"nl":"荷兰",\
	"nz":"新西兰",\
	"ni":"尼加拉瓜",\
	"ne":"尼日尔",\
	"ng":"尼日利亚",\
	"kp":"朝鲜",\
	"no":"挪威",\
	"om":"阿曼",\
	"pk":"巴基斯坦",\
	"pa":"巴拿马",\
	"pg":"巴布亚新几内亚",\
	"py":"巴拉圭",\
	"pe":"秘鲁",\
	"ph":"菲律宾",\
	"pl":"波兰",\
	"pf":"法属玻利尼西亚",\
	"pt":"葡萄牙",\
	"pr":"波多黎各",\
	"qa":"卡塔尔",\
	"re":"留尼旺",\
	"ro":"罗马尼亚",\
	"ru":"俄罗斯",\
	"lc":"圣卢西亚",\
	"vc":"圣文森特岛",\
	"as":"东萨摩亚(美)",\
	"ws":"西萨摩亚",\
	"sm":"圣马力诺",\
	"st":"圣多美和普林西比",\
	"sa":"沙特阿拉伯",\
	"sn":"塞内加尔",\
	"sc":"塞舌尔",\
	"sl":"塞拉利昂",\
	"sg":"新加坡",\
	"sk":"斯洛伐克",\
	"si":"斯洛文尼亚",\
	"sb":"所罗门群岛",\
	"so":"索马里",\
	"za":"南非",\
	"es":"西班牙",\
	"lk":"斯里兰卡",\
	"lc":"圣卢西亚",\
	"vc":"圣文森特",\
	"sd":"苏丹",\
	"sr":"苏里南",\
	"sz":"斯威士兰",\
	"se":"瑞典",\
	"ch":"瑞士",\
	"sy":"叙利亚",\
	"tw":"台湾省",\
	"tj":"塔吉克斯坦",\
	"tz":"坦桑尼亚",\
	"th":"泰国",\
	"tg":"多哥",\
	"to":"汤加",\
	"tt":"特立尼达和多巴哥",\
	"tn":"突尼斯",\
	"tr":"土耳其",\
	"tm":"土库曼斯坦",\
	"ug":"乌干达",\
	"ua":"乌克兰",\
	"ae":"阿拉伯联合酋长国",\
	"gb":"英国",\
	"us":"美国",\
	"uy":"乌拉圭",\
	"uz":"乌兹别克斯坦",\
	"ve":"委内瑞拉",\
	"vn":"越南",\
	"ye":"也门",\
	"yu":"南斯拉夫",\
	"zw":"津巴布韦",\
	"zr":"扎伊尔",\
	"zm":"赞比亚",\
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
		title = ',占比,'.join(self.keywords_list)
		title += ",占比"
		buff = "国家,%s\n"%(title)

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
		buff += "总量,%s\n"%(temp[:-1])

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
