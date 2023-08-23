katz_deli = []


def line(people):
    if len (people) == 0:
        print("The line is currently empty.")
    else:
         phrase = "The line is currently:"
         for index, name in enumerate(people):
            phrase += f" {index + 1}. {name}"
            
         print(phrase)
            
def take_a_number(katz_deli, person):
    katz_deli.append(person)
    print(f"Welcome, {person}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)

#enumerate ---used to conveniently get both the index and value
# ..from list during iteration
# .append() --add
# .pop() --remove