from blog import Blog
from post import Post
MENU = '''Enter c to create a blog,
                l to list blogs
                p to create a post
                r to read
                or q to quit '''

blogs = dict()


def menu():
    #lists the available blogs , let the user to make choice
    #process the choice , exits

    print_blogs()
    selection = input(MENU)

    while selection != 'q':
        if selection == 'c':
            create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            read_blog()
        elif selection == 'p':
            create_post()
        selection = input(MENU)

def print_blogs():
    for _,value in blogs.items():     
        print(value.__repr__())

def create_blog():
        title = input('Enter the title: ')
        name = input('Enter authors name: ')
        
        blogs[title] = Blog(title,name)
        
def read_blog():
        get_title = input('Enter the name of the post you want to read: ')
        print_posts(blogs[get_title])

def print_posts(blog):
        for post in blog.posts:
                print_posts(post)

def print_posts(post):
        print('''--------{}------
        {} '''.format(post.title,post.content))
def create_post():
        posttitle = input('Enter post title: ')
        postcontent = input('Enter post content: ')
        post[posttitle]= Post(posttitle,postcontent)
        # post[posttitle]=postcontent
        print(post)
menu()
