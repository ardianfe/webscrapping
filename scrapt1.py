import requests, lxml.html

s = requests.session()

login = s.get('https://peerreview.jabarprov.go.id/api-siap-mobile-gtk/api/login?kinerja_session_id=b8zv43d8shfrqi73ciafij5gyd2elmd8v008wcapgw_2880x1800&browser_id=97fba28291f78adcd204e6b389a69203')
login_html = lxml.html.fromstring(login.text)
hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
form = {x.attrib["username"]: x.attrib["value"] for x in hidden_inputs}

form['username'] = 'user10'
form['password'] = '123456'
response = s.post('https://peerreview.jabarprov.go.id/api-siap-mobile-gtk/api/login?kinerja_session_id=b8zv43d8shfrqi73ciafij5gyd2elmd8v008wcapgw_2880x1800&browser_id=97fba28291f78adcd204e6b389a69203',
                    data=form)
print(response)
print('user10' in response.text)