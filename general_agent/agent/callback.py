

def make_decorator(decorator):
    """
    Credit to Dacav on StackOverflow
    https://stackoverflow.com/questions/5929107/decorators-with-parameters

    Decorators, these little "@python_things" that go above other functions
    are weird to work with, and even more confusing when you need arguments

    The code below lets us do this to *any* function to make it a decorator
    ```python
    
    @make_decorator
    def multiply_result_by(parent_function, number: int):

        # `*args` and `**kwargs` come from **this files code** they are not
        # your custom functions arguments!
        #
        # These arguments are from the function you are applying *your* decorator
        # to, in this case `uh_math_stuff(foo: int=42)`
        # So `foo` is a part of `*args`
        def auxiliary(*args, **kwargs):
            # Perform code things here not in `multiply_result_by`!

            # Think of `parent_function` almost like `self` but for decorators...
            # You also don't need to put arguments in here if it does not take any
            parent_function_result = parent_function(*args, **kwargs)
            return parent_function_result * number
        return auxiliary

    @multiply_result_by(5)
    def uh_math_stuff(foo: int=42):
        bar: int = 32
        return foo - bar

    # The result:
    # 42 - 32 = 10
    # 10 * 5  = 50
    ```
    """
    def layer(*args, **kwargs):
        def repl(function):
            return decorator(function, *args, **kwargs)
        return repl
    return layer

@make_decorator
def new(
    parent_func,
    description: str,
    return_type: type,
    *function_args  # This is automatically processed with `new_arg`
):
    """
    Used as a decorated like so:
    ```python
    import callback

    @callback.new(
        "Industrial society and its consequences",
        str,
        callback.new_arg("in_n_days", int, "How long until we take it over?")
        callback.new_arg(...)
        ...
    )
    def world_domination(in_n_days: int) -> str:
        print("Take over the world!!!")
        print(f"Only {in_n_days} left")
        return "returning a value here"
    ```
    """

    # The decorator
    def auxiliary(*args, **kwargs):

        # Build the JSON dictionary that describes the function
        # for OpenAI's `ChatCompetion` API. More info here:
        # https://platform.openai.com/docs/guides/gpt/function-calling
        return_type_str = "None"
        if return_type is not None:
            return_type_str: str = return_type.__name__

        openai_json: dict = {
            "name": parent_func.__name__,
            "description": description,
            "parameters": {
                "type": return_type_str,
                "required": [],   # All required functions arguments go here for some reason
                "properties": {}  # Function arguments go here
            }
        }

        # Add every function argument to the OpenAI function JSON file
        for arg in function_args:
            if arg["arg_required"]:
                openai_json["parameters"]["required"].append(arg["arg_name"])

            # Create a new function argument at `parameters -> properties -> <arg_name>`
            openai_json["parameters"]["properties"][arg["arg_name"]] = {
                "type"       : arg["arg_type"],
                "description": arg["arg_desc"]
            }

            # If we have a enum, add it at `parameters -> properties -> enum`
            if arg["arg_enum"] is not None:
                openai_json["parameters"]["properties"][arg["arg_name"]]["enum"] = arg["arg_enum"]

        # Run the actual function with the args the user has
        # Even if we have no regular or keyword arguments it still works fine
        output = parent_func(*args, **kwargs)

        return output, openai_json

    # `new` returning the decorator
    return auxiliary


def new_arg(
    arg_name: str,
    arg_type: type,
    arg_desc: str,
    enum: list[str]=None,
    required: bool=True,
) -> dict:
    """
    Mostly just meant for the decorator `new(...)`, to make it easier to read.
    Used like so:
    ```python
    import callback

    @callback.new(
        <function description>
        <function return type>
        callback.new_arg("text", type=str, enum=None, required=True)
        callback.new_arg(...)
        ...
    )
    def create_md_file(text: str) -> None:
        do_the_thing
    ```
    """
    assert (type(enum) is not None) or (type(enum) is not list[str]), \
            "`enum` must be either None or a list of strings"
        
    arg_type_str: str = "None"
    if arg_type is not None:
        arg_type_str = arg_type.__name__

    argument: dict = {
        "arg_name": arg_name,
        "arg_type": arg_type_str,
        "arg_desc": arg_desc,
        "arg_enum": enum,
        "arg_required": required,
    }
    return argument
