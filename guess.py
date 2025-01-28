# guess words

data = {
    "animal": {
        "small": [{"black": ["ant"]}, {"floffy":["cat"]}, {"eats cheese":["mouse"]}],
        "cute": [{"floffy":["cat"]}, {"eats cheese":["mouse"]}, {"long ears": ["rabbit"]}],
        "big": [{"tall": ["giraffe"]}, {"gray":["elephant", "rhino"]}, {"extinct":["dino"]}],
        "long": [{"scarry": ["snake", "lizard"]}, {"sea animal": ["whale", "shark"]}, {"long neck": ["giraffe"]}],
    },
    "color": {},
    # "object": {},
}
keys = list(data.keys())

print("choose one of these categories: ", tuple(data.keys()))
choice = input(">>> ")

if choice in data:
    category_data = data[choice]

flag = False
count = 0
while True:
    if choice == 'animal':
        for i in data["animal"]:
            if flag: break
            answer = input(f"Does your animal has the attribute {i}(yes/no)? ")

            count += 1
            if count > 10: 
                flag = True
                print("Too many attempts! Let's extend the dictionary.")
                new_item = input("What is your animal? ").strip()
                main_attribute = input("What is its main attribute? ").strip()
                other_attribute = input("Please write another attribute for it: ").strip()

                 # Extend the dictionary
                if main_attribute in category_data:
                    category_data[main_attribute].append({other_attribute: [new_item]})
                else:
                    category_data[main_attribute] = [{other_attribute: [new_item]}]

                print("Thanks for teaching me! I'll remember this.")
                break
               
            if answer == 'yes':
                for option in data["animal"][i]: 
                    if flag: break
                    answer = input(f"Does your animal has the attribute {list(option.keys())}(yes/no)? ")
                    count += 1
                    if count > 10: flag = True; break
                    if answer == 'yes':
                        for value in option.values():
                            if flag: break  
                            for item in value:
                                if flag: break  
                                answer = input(f"Is it {item}(yes/no)? ")
                                if answer == 'yes':
                                    print(f"I find it, your animal is {item}!!!")
                                    flag = True; break
        if flag: break



print("\n\n\n*********************\n", data)


"""
As you see this is like a basic mini AI. 
I want to create a system which extends its dictionary by users.

note: I know that changes in data is not permanent, 
so I should work with 'files' which I rather not, cause I haven't studied that part yet!
First season of learning python is done. Thank you me!

contact: gholamnejadmahdi737@gmail.com
"""