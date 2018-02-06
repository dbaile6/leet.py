
#Creates a class "Person"

class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_counter = 0
        self.met = set()

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_counter += 1
        if other_person not in self.met:
            self.met.add(other_person)
            other_person.met.add(self)

    def num_unique_people_greeted(self):
        return len(self.met)

    def print_contact_info(self):
        print "%s's email: %s, %s's phone is %s" % (
            self.name,
            self.email,
            self.name,
            self.phone
    )

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        return len(self.friends)

    def __repr__(self):
        return 'Person(%s, %s)' % (self.name, self.email)

sonny = Person('Sonny', 'sonny@hotmail.com', '404-441-4471')
jordan = Person('Jordan', 'jordan@hotmail.com', '412-021-1231')

sonny.greet(jordan)
jordan.greet(sonny)
jordan.greet(jordan)

print jordan.num_unique_people_greeted()
