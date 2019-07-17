"""Typed Tuple
An augmentation to NamedTuple, which allows for constraining arguments

@CREDIT: David Downes | https://github.com/TheUKDave
"""
from collections import namedtuple
import inspect


class TypedTuple:
    _coerce_types = True

    def __new__(cls, *args, **kwargs):
        # Get the specified public attributes on the class definition
        typed_attrs = cls._get_typed_attrs()

        # For each positional argument, get the typed attribute,
        # and check it's validity
        new_args = []
        for i, attr_value in enumerate(args):
            typed_attr = typed_attrs[i]
            new_value = cls.__parse_attribute(typed_attr, attr_value)
            # Build a new args list to construct the namedtuple with
            new_args.append(new_value)

        # For each keyword argument, get the typed attribute, and
        # check it's validity
        new_kwargs = {}
        for attr_name, attr_value in kwargs.items():
            typed_attr = (attr_name, getattr(cls, attr_name))
            new_value = cls.__parse_attribute(typed_attr, attr_value)
            # Build a new kwargs object to construct the namedtuple with
            new_kwargs[attr_name] = new_value

        # Return a constructed named tuple using the named attribute, and the
        # supplied arguments
        return namedtuple(cls.__name__,
                          [attr[0] for attr in typed_attrs])(*new_args,
                                                             **new_kwargs)

    @classmethod
    def __parse_attribute(cls, typed_attr, attr_value):
        # Try to find a function defined on the class to do
        # checks on the supplied value
        check_func = getattr(cls, f'_parse_{typed_attr[0]}', None)

        if inspect.isroutine(check_func):
            attr_value = check_func(attr_value)
        else:
            # If the supplied value is not the correct type, attempt to
            # coerce it if _coerce_type is True
            if not isinstance(attr_value, typed_attr[1]):
                if cls._coerce_types:
                    # Coerce the value to the type, and assign back to the
                    # attr_value for further validation
                    attr_value = typed_attr[1](attr_value)
                else:
                    raise TypeError(
                        f'{typed_attr[0]} is not of type {typed_attr[1]}')

        # Return the original value
        return attr_value

    @classmethod
    def _get_typed_attrs(cls) -> tuple:
        all_items = cls.__dict__.items()
        public_items = filter(lambda attr: not attr[0].startswith(
            '_') and not attr[0].endswith('_'), all_items)
        public_attrs = filter(
            lambda attr: not inspect.isroutine(attr[1]), public_items)
        return [attr for attr in public_attrs if isinstance(attr[1], type)]
