# Create User Class
class User:
    # class attributes
    posts = []

    # add specified instance attributes
    def __init__(self, name, email, drivers_license, User_posts=[]):
        self.Name = name
        self.Email = email
        self.Drivers_license = drivers_license
        self.User_posts = User_posts

    # print string representation of objects
    def __repr__(self):
        print(f"All Posts: {User.posts} | User's Posts: {self.User_posts}")

    # instance method to create user post
    def create_a_post(self):
        title = input("Please enter post title: ")
        content = input("Please enter post content: ")
        id = str(len(User.posts) + 1)
        new_post_dict = {id: [title, content]} 
        User.posts.append(new_post_dict)
        self.User_posts.append(new_post_dict)
        print("Posted Successfully!")

     # print all class posts
    def see_all_posts(self):
        if len (User.posts) > 0:
            print(f"{User.posts}")
        else:
            return None

    # print single instance user's posts, NOT all posts
    def see_my_posts(self):
        if len (self.User_posts) > 0:
            print(f"{self.User_posts}")
        else:
            return None


    def delete_a_post(self):
        deleted_post = []
        title = input("Please enter post title you want to delete: ")
        
        try:
            # loops through User.posts and appends the deleted post to deleted_post variable
            for i in range(len(User.posts)):
                #if title and object title matches
                if User.posts[i][(str(i+1))][0] == title:
                    deleted_post.append(User.posts[i])
            # actually deletes post from class and instance variable
            for item in deleted_post:
                while item in User.posts:
                    User.posts.remove(item)
                    self.User_posts.remove(item)
                    print("Post Deleted Successfully")
        except KeyError:
            print("Post not found to delete")
            
# input = iter(["Johns †i†le", "I Just joined OOPX"])
# user = User("John", "john@email.com", "FDUI87")
# user2 = User("Jason", "jason@email.com", "12345")
# user.create_a_post() # creating posts for all User instances, not just current instance
# user2.create_a_post()
# user.see_my_posts() # sees all posts regardless
# user.see_all_posts() # sees all posts
# user.delete_a_post()
# user.see_all_posts()

# FAILED test_User.py::test_delete_post - AssertionError: assert 1 == 0
# FAILED test_User.py::test_see_all_posts - AssertionError: assert 1 == 0
# FAILED test_User.py::test_see_my_posts - AssertionError: assert 1 == 3