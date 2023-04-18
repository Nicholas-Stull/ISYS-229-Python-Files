import string


def resources_scanner(package):
    resources_list = dir(package)
    for resource in resources_list:
        if not resource.startswith('__'):  # check for hidden attributes
            print(resource)



# testing the function with string package
resources_scanner(string)
