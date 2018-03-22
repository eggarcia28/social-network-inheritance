
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = [] 

    def add_post(self, post):
        self.posts.append(post)
    
    def get_timeline(self):
        self.timeline = []
        for user in self.following:
            for post in user.posts:
                self.timeline.append(post)
        return sorted(self.timeline,key=lambda post: post.timestamp)

    def follow(self, other):
        self.following.append(other)
