import urllib2
import cookielib

url = "http://www.baidu.com"

print 'the first one'

response1 = urllib2.urlopen(url)

print response1.getcode()
print len(response1.read())

print 'the second one'
root_url = "https://www.baidu.com/ssid=3b9064617765696461776569327506/from=844b/s?word=手机管家&ts=0458536&t_kt=0&ie=utf-8&fm_kl=021394be2f&rsv_iqid=3250502319&rsv_t=6aa7DGzacOFkW5GX3wHLB83tbSVQTpyqGRysduf6rJrQm8yx34lOXBau3A&sa=ib&ms=1&rsv_pq=3250502319&rsv_sug4=5661&tj=1&ss=110&inputT=4753"
request = urllib2.Request(root_url)
request.add_header("user-agent","Mozilla/5.0 (Linux; Android 8.0.0;LON-AL00 Build/HUAWEILON-AL00) AppleWebKit/537.36(KHTML, like Gecko) Version/4.0 Mobile Safari/537.36")
response2 = urllib2.urlopen(request)
print response2.getcode()
print response2.read()

print 'the third one'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)

print response3.getcode()
print cj
print len(response3.read())
