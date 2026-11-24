###
# Class modelling a social media profile
#
class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        # every profile starts with an empty list of posts
        self.posts = []

    # Adds a post at the end of the list
    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    # Prints the user's name and the numbered list of posts
    def display_timeline(self):
        print()
        print(f"{self.username}'s timeline:")
        # enumerate(..., start=1) gives pairs: number, post
        for number, post in enumerate(self.posts, start=1):
            print(f'{number}. {post}')


def main():
    user = SocialMediaProfile('johndoe')
    user.add_post('Hello, world!')
    user.add_post('Had a great day at the park!')
    user.add_post("What's up, Natalie? How are you?")
    user.display_timeline()

if __name__ == "__main__":
    main()