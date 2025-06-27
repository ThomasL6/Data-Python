def NULL_not_found(object: any) -> int:
    type_map = {
        type(None): "Nothing",
        float: "Cheese",
        int: "Zero",
        bool:  "Fake",
    }
    t = type(object)
    if t == str and object == '':
        print(f"Empty: {object} {t}")
    elif t in type_map:
        print(f"{type_map[t]} : {object} {t}")
    else:
        print("Type not Found")
        return (1)
    return (0)
