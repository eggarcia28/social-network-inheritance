from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.user = None
        self.timestamp = timestamp

    def set_user(self, user):
        self.user = user
        user.posts.append(self)

class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)

    def __str__(self):
        return '@{fname} {lname}: "{post}"\n\t{time}'.format(fname= self.user.first_name, lname= self.user.last_name, 
        post=self.text, time=self.timestamp.strftime('%A, %b %d, %Y'))

class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url
        
    def __str__(self):
        return '@{fname} {lname}: "{post}"\n\t{image}\n\t{time}'.format(fname= self.user.first_name, lname= self.user.last_name, 
        post=self.text, image = self.image_url, time=self.timestamp.strftime('%A, %b %d, %Y'))

class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '@{fname} Checked In: "{post}"\n\t{lat}, {lon}\n\t{time}'.format(fname= self.user.first_name, lname= self.user.last_name, 
        post=self.text, lat = self.latitude, lon = self.longitude, time=self.timestamp.strftime('%A, %b %d, %Y'))
