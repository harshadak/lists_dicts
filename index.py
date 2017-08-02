def list_dicts(arr1, arr2):
    if len(arr1) > len(arr2):
        new_dict = zip(arr1, arr2)
    else:
        new_dict = zip(arr2, arr1)
    return new_dict
    #Result is...
    #[('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]
    

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "dog"]

print list_dicts(name, favorite_animal)