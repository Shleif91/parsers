from rotating_proxies.policy import BanDetectionPolicy

class MyBanPolicy(BanDetectionPolicy):
    def response_is_ban(self, request, response):
        # use default rules, but also consider HTTP 200 responses
        # a ban if there is 'captcha' word in response body.
        ban = super(MyBanPolicy, self).response_is_ban(request, response)
        print(ban)

        return ban

    def exception_is_ban(self, request, exception):
        print(exception)
        return super(MyBanPolicy, self).exception_is_ban(request, exception)