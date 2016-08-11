from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_basic(self):
        self.open('http://questionpro.com')                       # Opens the url
        self.click_link_text('LOGIN')
        self.update_text('input#EmailAddress', 'anup.surendran@gmail.com')

        self.update_text('input#Password','Questionpro5#')
        i = u'\u00BB'
        login = 'LOG IN '+ i.encode('utf-8')
        ## self.find_element('//*[@value='" + login + "']')
        self.click('input[class*="btn-user-login"]')
        self.assert_element('img[alt="QuestionPro1"]')

