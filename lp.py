import inspect

# import to_comment

# TODO: use the decorator to find functions that we actually want to parse instead of importing them manually
from example import is_palindrome

  

def function_to_md(code: str):
  
  is_code = False
  
  for line in code.split("\n"):
    # Remove leading whitespace
    stripped = line.lstrip()

    # If this is a comment, turn it into markdown
    if not stripped:
      print("")
    elif stripped.startswith("#"):
      # Handle comment
      if is_code:
        is_code = False
        print("```")
      print(stripped[1:])
    else:
      # Handle code
      if not is_code:
        is_code = True
        print("```python")
      print(line)

  if is_code:
    print("```")
      
code = inspect.getsource(is_palindrome)
function_to_md(code)
