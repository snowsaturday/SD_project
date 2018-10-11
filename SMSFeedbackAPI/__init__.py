# coding: utf-8

import urllib
import urllib2
import base64

API_URL_SEND = "http://api.smsfeedback.ru/send/"
API_URL_CREDITS = "http://api.smsfeedback.ru/credits/"
API_URL_STATUS = "http://api.smsfeedback.ru/status/"


class SmsFeedBack(object):
	# "Класс для работы с smsfeedback.ru"

	def __init__(self, login, password):
		self.base64auth = base64.encodestring('%s:%s' % (login, password))

	def _request(self, url, params={}):
		if params:
			params_encoded = urllib.urlencode(params)
		else:
			params_encoded = ""
		request = urllib2.Request("%s?%s" % (url, params_encoded))
		request.add_header("Authorization", "Basic %s" % self.base64auth)
		result = urllib2.urlopen(request)
		response = result.read()
		return response

	def send_sms(self, phone_number, msg):
		# "Отправка смс сообщения"
		response = self._request(API_URL_SEND, {"phone": phone_number, "text": msg})
		return response

	def credits(self):
		# "Проверка состояния счета"
		response = self._request(API_URL_CREDITS)
		return response

	def status(self, id_msg):
		# "Проверка состояния сообщения"
		response = self._request(API_URL_STATUS, {"id": id_msg})
		return response
