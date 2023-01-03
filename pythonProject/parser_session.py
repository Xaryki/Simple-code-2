import requests
from bs4 import BeautifulSoup

url = "https://profile.edx.org/u/KsenyaDerevyanchenko"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
}


cookie = {
    "__hssc": "23171429.7.1651250051956",
     "__hssrc": "1",
     "__hstc": "23171429.3cef03c8d93b7d541eef48619818d376.1651248578110.1651248578110.1651250051956.2",
     "__zlcmid": "19jkt7Az5l3gmee",
     "_fbp": "fb.1.1651248577954.734535185",
     "_ga": "GA1.2.1180162760.1651248571", "_gcl_au": "1.1.824889457.1651248570",
     "_gid": "GA1.2.88365014.1651248571", "_hjAbsoluteSessionInProgress": "1",
     "_hjFirstSeen": "1",
     "_hjSession_1563632": "eyJpZCI6ImI5MDVmNzc2LTU4NGQtNDA1Mi1hYzgwLTY1NDJhYzA1OGNjMiIsImNyZWF0ZWQiOjE2NTEyNDg1NzgwMzUsImluU2FtcGxlIjpmYWxzZX0=",
     "_hjSessionUser_1563632": "eyJpZCI6ImIyZTY2MGRiLWRhMmEtNWJlYi1iMzQwLWYxMWRlMWI1Nzk4NiIsImNyZWF0ZWQiOjE2NTEyNDg1Nzc5ODMsImV4aXN0aW5nIjp0cnVlfQ==",
     "_uetsid": "c1025bf0c7d611ec891e7d89638c3f5e", "_uetvid": "c1028f00c7d611ec9578b39380f16ce8",
     "ab.storage.deviceId.dd7cff88-0bc3-4420-b72b-38f460473479": "{\"g\":\"ad88dc6b-608f-bf08-7d85-c36a9fa92042\",\"c\":1651248597903,\"l\":1651248597903}",
     "ab.storage.sessionId.dd7cff88-0bc3-4420-b72b-38f460473479": "{\"g\":\"b8a61a2a-b28a-ad6f-1099-3f2da52d291c\",\"e\":1651250337625,\"c\":1651250307626,\"l\":1651250307626}",
     "ab.storage.userId.dd7cff88-0bc3-4420-b72b-38f460473479": "{\"g\":\"9859732\",\"c\":1651248600540,\"l\":1651248600540}",
     "ajs_anonymous_id": "\"fbce07e2-0a29-4c05-b4fa-6c220a69c166\"",
     "ajs_user_id": "9859732",
     "edx-jwt-cookie-header-payload": "eyJhbGciOiJSUzUxMiIsImtpZCI6Imxtc3Byb2QwMDIifQ.eyJhdWQiOiAicmlubXlieWVkbnVhdzVwaGxpZENvY0R1ZGJ5bGJPYkRpYkpvZGJvc2dldHNFYmFsZDQiLCAiZXhwIjogMTY1MTI1MzY3MiwgImlhdCI6IDE2NTEyNTAwNzIsICJpc3MiOiAiaHR0cHM6Ly9jb3Vyc2VzLmVkeC5vcmcvb2F1dGgyIiwgInByZWZlcnJlZF91c2VybmFtZSI6ICJLc2VueWFEZXJldnlhbmNoZW5rbyIsICJzY29wZXMiOiBbInVzZXJfaWQiLCAiZW1haWwiLCAicHJvZmlsZSJdLCAidmVyc2lvbiI6ICIxLjIuMCIsICJzdWIiOiAiMmFiOTIxMmM5Yzg5OGI0OGY4NTQ0MjUwZmI4OTMxYmMiLCAiZmlsdGVycyI6IFsidXNlcjptZSJdLCAiaXNfcmVzdHJpY3RlZCI6IGZhbHNlLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAidXNlcl9pZCI6IDk4NTk3MzIsICJlbWFpbCI6ICJrc3UubXlzdGVyeUBnbWFpbC5jb20iLCAibmFtZSI6ICJLc2VueWEgIERlcmV2eWFuY2hlbmtvIiwgImZhbWlseV9uYW1lIjogIlx1MDQxNFx1MDQzNVx1MDQ0MFx1MDQzNVx1MDQzMlx1MDQ0Zlx1MDQzZFx1MDQ0N1x1MDQzNVx1MDQzZFx1MDQzYVx1MDQzZSIsICJnaXZlbl9uYW1lIjogIlx1MDQxYVx1MDQ0MVx1MDQzNVx1MDQzZFx1MDQzOFx1MDQ0ZiIsICJhZG1pbmlzdHJhdG9yIjogZmFsc2UsICJzdXBlcnVzZXIiOiBmYWxzZX0",
     "edx-jwt-cookie-signature": "AJHb11mlyac33RQjuFvtkJolu7UjE_aI9CmkTWYNCAC_N6Fx84faZ2EZff1HvrSUh8Po_d59uxF1YHQtK7exomunZKxY7KEBEQ5EsFVux-h4BnLFhJzYn-CClOpo7JzMVHje-bFXjvpjUoR7Yhtkk1i6ITMZuZBSvN_9x4c5GyRbL_dwfeNP4wIbnS73z4CbvvUJjgmnYfyYhXEvbjlHbKybnBJEKiA3N4QwNfzPc2ZRpS2e5DIA1sWEk_uGbdNg0_086GN8mRou3uUmwbYYoZrcnoWAOVtZVZLP7hh_NV-IzIEJNaDR8ZJOe-lclxgZ-pH71nDCEBQIvuSxpLmWRQ",
     "edxloggedin": "true", "hubspotutk": "3cef03c8d93b7d541eef48619818d376",
     "optimizelyEndUserId": "oeu1651248566853r0.23145571430480583", "prod-edx-cf-loc": "RU",
     "prod-edx-cookie-policy-viewed": "true", "prod-edx-language-preference": "en",
     "prod-edx-user-info": "\"{\\\"version\\\": 1\\054 \\\"username\\\": \\\"KsenyaDerevyanchenko\\\"\\054 \\\"email\\\": \\\"ksu.mystery@gmail.com\\\"\\054 \\\"header_urls\\\": {\\\"logout\\\": \\\"https://courses.edx.org/logout\\\"\\054 \\\"account_settings\\\": \\\"https://courses.edx.org/account/settings\\\"\\054 \\\"learner_profile\\\": \\\"https://courses.edx.org/u/KsenyaDerevyanchenko\\\"\\054 \\\"resume_block\\\": \\\"https://courses.edx.org/courses/course-v1:MITx+CTL.SC3x+1T2022/jump_to/block-v1:MITx+CTL.SC3x+1T2022+type@html+block@f3c0d64a1d27485c822ae28e7e215aee\\\"}\\054 \\\"user_image_urls\\\": {\\\"full\\\": \\\"https://prod-edx-edxapp-assets.edx-cdn.org/static/edx.org-next/images/profiles/default_500.3292bbf079b8.png\\\"\\054 \\\"large\\\": \\\"https://prod-edx-edxapp-assets.edx-cdn.org/static/edx.org-next/images/profiles/default_120.7c4c5c6b90a1.png\\\"\\054 \\\"medium\\\": \\\"https://prod-edx-edxapp-assets.edx-cdn.org/static/edx.org-next/images/profiles/default_50.d29941819645.png\\\"\\054 \\\"small\\\": \\\"https://prod-edx-edxapp-assets.edx-cdn.org/static/edx.org-next/images/profiles/default_30.ee82223aa027.png\\\"}}\""}

session = requests.Session()
session.cookies.update(cookie)
response = session.get(url, headers=headers)
print(response)
