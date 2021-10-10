#
# Let's create a function that simply prints an argument
#

def print_greeting(to_what, from_who):
    print(f"hello {to_what}, I'm {from_who}")

#
# and then creating something use that greeting
#
def main():
    print_greeting("world", "1678")

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
