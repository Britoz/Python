# TODO: import string template
from string import Template

# TODO: create main definition
def main():
    # Usual string formatting with format()
    str1 = "Your name is {0} and age is {1}".format("Vinh", 26)
    print(str1)
    '''
    format is used to format {0} and {1} inside the string
    '''
    # TODO: create a template with placeholders
    templ = Template("You are watching ${title} by ${author}")
    # TODO: use the substitute method with keyword arguments
    str2 = templ.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)

    # TODO: use the substitute method with a dictionary
    data = {
        "author": "Vinh",
        "title": "new data"
    }
    str3 = templ.substitute(data)
    print(str3)

if __name__ == "__main__":
    main()