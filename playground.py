import requests
from post import Post

BLOG_API = "https://api.npoint.io/4af156202f984d3464c3"

blogs = requests.get(BLOG_API).json()
#
# print(blogs[0]["title"])
# print(blogs[0]["subtitle"])

blog_objects = []

for blogs in blogs:
    post = Post(post_id=blogs["id"], body=blogs["body"], title=blogs["title"], subtitle=blogs["subtitle"])
    blog_objects.append(post)

print(blog_objects[1].id, blog_objects[1].title)