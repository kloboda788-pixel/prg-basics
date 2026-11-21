import queue

###
# Simulates the Back key in a web browser
#

# a stack of previously visited websites
visited_websites = queue.LifoQueue()

# some previously visited websites
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

# the website you are viewing now
current_website = ''

while True:
    website = input('Enter website name (0 for back): ')

    if website == '0':
        if visited_websites.empty():
            print('No more previously visited websites.')
            break
        else:
            print('<-- Going back to a previously visited website')
            # take the most recently visited website from the top of the stack
            current_website = visited_websites.get()
    elif website != "":
        # before opening a new website, remember the current one on the stack
        if current_website != '':
            visited_websites.put(current_website)
        current_website = website

    # print name of website you are currently viewing
    print('You are currently viewing:', current_website)
    print()