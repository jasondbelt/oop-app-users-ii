# your improved User class goes here
class User:
    posts=[]
    
    def __init__(self,name, email, drivers_license):
        self.Name=name
        self.Email=email
        self.Drivers_license=drivers_license
        self.User_posts=[]
        
        
    def create_a_post(self):
        id=len(self.posts)+1
        user_title=input("Please enter the title of your post:\n")
        user_body=input("Please enter the content of your post:\n")
        self.posts.append({"id":id,"title":user_title, "content":user_body})
        self.User_posts.append({"id":id,"title":user_title, "content":user_body})
        
        
    def delete_a_post(self):
        id=input("Please enter the ID of the post you would like to delete:\n")
        for i in range(len(self.User_posts)):
            if self.User_posts[i]['id']== id:
                self.User_posts.pop(i)
        for j in range(len(self.posts)):
            if self.posts[j]['id']==id:
                self.posts.pop(j)
                
    @classmethod
    def see_all_posts(self):
        for i in self.posts:
            print(f"Title: {i['title']}\nContent:\n{i['content']}")
        
    def see_my_posts(self):
        for i in self.User_posts:
            print(f"Title: {i['title']}\nContent:\n{i['content']}")
            
            
def createUsers():
    user_instances=[]
    users=[
        {"name":"John", "email":"john@email.com", "drivers_license":"FDUI87"},
        {"name":"Mike", "email":"mike@email.com", "drivers_license":"FDUI87"},
        {"name":"Zack", "email":"zack@email.com", "drivers_license":"FDUI87"}
    ]
    for user in users:
        user_instances.append(User(**user))
    for i in user_instances:
        i.create_a_post()
    User.see_all_posts()
    for i in user_instances:
        i.see_my_posts()

# This is for dev purposes. Pytest will FAIL if this line isn't commented out b/c it messes with monkeypatch in a bad way.
createUsers()