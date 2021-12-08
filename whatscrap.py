# whatscrap class for scraping data from whatsapp web

class Whatsapp:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://web.whatsapp.com/')
        self.driver.implicitly_wait(30)

    def get_chat_list(self):
        # get chat list
        chat_list = self.driver.find_elements_by_class_name('_2zCfw')
        return chat_list

    def get_chat_name(self, chat_list):
        # get chat name
        chat_name = []
        for i in chat_list:
            chat_name.append(i.find_element_by_class_name('_3ko75').text)
        return chat_name

    def get_chat_message(self, chat_list):
        # get chat message
        chat_message = []
        for i in chat_list:
            chat_message.append(i.find_element_by_class_name('_3FRCZ').text)
        return chat_message

    def get_chat_time(self, chat_list):
        # get chat time
        chat_time = []
        for i in chat_list:
            chat_time.append(i.find_element_by_class_name('_3_7SH').text)
        return chat_time

    def get_chat_image(self, chat_list):
        # get chat image
        chat_image = []
        for i in chat_list:
            try:
                chat_image.append(i.find_element_by_class_name(
                    '_3_7SH').find_element_by_tag_name('img').get_attribute('src'))
            except:
                chat_image.append(None)
        return chat_image

    # def get_chat_video(self, chat_list):
    #     # get chat video
    #     chat_video = []
    #     for i in chat_list:
    #         try:
    #             chat_video.append(i.find_element_by_class_name('_3_7SH').find_element_by_tag_name('video
