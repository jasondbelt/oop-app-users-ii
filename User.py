# your improved User class goes here
class User:
    posts=[]
    
    def __init__(self,name, email, drivers_license):
        self.Name=name
        self.Email=email
        self.Drivers_license=drivers_license
        self.User_posts=[]
        
        
    def create_a_post(self):
        id=len(self.posts)
        user_title=input("Please enter the title of your post:\n")
        user_body=input("Please enter the content of your post:\n")
        self.posts.append({"id":id,"title":user_title, "content":user_body})
        self.User_posts.append({"id":id,"title":user_title, "content":user_body})
        
        
    def delete_a_post(self):
        id=int(input("Please enter the ID of the post you would like to delete:\n"))
        for p in self.User_posts:
            print(f'user posts {p}')
            if p['id']== id:
                print(f'inside if User_posts')
                x = self.User_posts.remove(p)
                print(x)
        for p in self.posts:
            print(f'posts {p}')
            if p['id']==id:
                print(f'inside if posts')
                y = self.posts.remove(p)
                print(y)
        
      
         
    @classmethod
    def see_all_posts(self):
        for i in self.posts:
            print(f"ID: [{i['id']}] Title: {i['title']}\nContent:\n{i['content']}")
        
    def see_my_posts(self):
        for i in self.User_posts:
            print(f"ID: [{i['id']}] Title: {i['title']}\nContent:\n{i['content']}")
            
            
# user = User("John", "john@email.com", "FDUI87")
# user_two = User("Adam", "adam@email.com", "123")
# # # # # input = iter(["Johns †i†le", "I Just joined OOPX"])
# user.create_a_post()
# user_two.create_a_post()
# user.see_my_posts()
# user.see_all_posts()
# # # # # input = iter([1])
# user.delete_a_post()
# user.see_my_posts()
# user.see_all_posts()

# user2 = User(**{"name":"Mike", "email":"mike@email.com", "drivers_license":"FDUI87"})
# user3 = User(**{"name":"Zack", "email":"zack@email.com", "drivers_license":"FDUI87"}) 

# user.see_all_posts()
# # input = iter(["Zack åttåck", "B1@ck H@t"])
# user3.create_a_post()
# # input = iter(["Mikes πost", "OOPX Founder"])
# user2.create_a_post()
# # input = iter(["Johns †i†le", "I Just joined OOPX"])
# user.create_a_post()
# # input = iter(["Zack åttåck", "B1@ck H@t"])
# user.create_a_post()
# # input = iter(["Mikes πost", "OOPX Founder"])
# user.create_a_post()
# # input = iter(["Johns †i†le", "I Just joined OOPX"])
# user.create_a_post()
# user.see_all_posts()

