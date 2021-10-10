#
# Let's create a function that simply prints an argument
#

def print_greeting(to_what):
    print(f"hello {to_what}")

#
# and then creating something use that greeting
#
def main():
    print_greeting("world")

#
# greet all the planets
#
def greet_all_planets():
    for planet in ["Mercury", "Venus",
                   "Earth", "Mars",
                   "Jupiter", "Saturn",
                   "Uranus", "Neptune"]:
        print_greeting(planet)

#
# and call it
#
main()
greet_all_planets()
