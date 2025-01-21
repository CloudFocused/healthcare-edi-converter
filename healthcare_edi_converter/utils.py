def flatten_object(obj, parent_key='', sep='.'):
    """
    Flattens a graph of objects, including dictionaries, lists, and custom objects,
    into a key-value dictionary where the key is the full path to each value.

    :param obj: The input object, which could be a dictionary, list, or a custom object.
    :param parent_key: The base key to prepend (used during recursion).
    :param sep: Separator for keys in the flattened dictionary.
    :return: A flattened dictionary.
    """
    items = []

    if isinstance(obj, dict):
        # Handle dictionary
        for k, v in obj.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.extend(flatten_object(v, new_key, sep=sep).items())
    elif isinstance(obj, list):
        # Handle list
        for i, item in enumerate(obj):
            new_key = f"{parent_key}{sep}{i}" if parent_key else str(i)
            items.extend(flatten_object(item, new_key, sep=sep).items())
    elif hasattr(obj, "__dict__") or hasattr(obj, "__slots__"):
        # Handle objects with attributes
        attr_dict = {}
        if hasattr(obj, "__dict__"):
            # Include attributes from __dict__
            attr_dict.update(vars(obj))
        if hasattr(obj, "__slots__"):
            # Include attributes from __slots__
            for slot in obj.__slots__:
                if hasattr(obj, slot):
                    attr_dict[slot] = getattr(obj, slot)

        # Process attributes, excluding callables and special attributes
        for k, v in attr_dict.items():
            if not callable(v) and not k.startswith('__'):
                new_key = f"{parent_key}{sep}{k}" if parent_key else k
                items.extend(flatten_object(v, new_key, sep=sep).items())
    else:
        # Base case: not a dictionary, list, or object
        items.append((parent_key, obj))

    return dict(items)