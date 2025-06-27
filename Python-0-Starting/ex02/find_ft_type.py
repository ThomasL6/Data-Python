def all_thing_is_obj(object: any) -> int:
    type_map = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
    }
    t = type(object)
    if type(object) in type_map:
        print(f"{type_map[t]} : {t}")
    elif type(object) is str:
        print(f"{object} is in the kichen : {type(object)}")
    else:
        print("Type not found")
        return (42)
    return (0)
