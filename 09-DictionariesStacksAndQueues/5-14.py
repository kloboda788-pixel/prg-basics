import queue

###
# Customer service in an office using a queue
#
customers = queue.Queue()

# the next ticket number to give out
next_ticket = 1

while True:
    print('1. New customer (take a ticket)')
    print('2. Serve next customer')
    print('0. Quit')
    option = input('Select an option: ')

    if option == '1':
        # a new customer gets the next number and goes to the end of the queue
        customers.put(next_ticket)
        print(f'Your ticket number: {next_ticket}. Customers waiting: {customers.qsize()}')
        next_ticket += 1

    elif option == '2':
        if customers.empty():
            print('No customers in the queue.')
        else:
            # the customer from the beginning of the queue is served
            ticket = customers.get()
            print(f'Now serving ticket number {ticket}')

    elif option == '0':
        break

    print()