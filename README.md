# 🎯 "TRUTHY" AND "FALSEY" VALUES 
"Truthy" and "Falsey" refer to how Python evaluates objects in Boolean contexts, such as in if or while statements.

The basic rules are:
- Values that evaluate to False are considered **Falsey**.
- Values that evaluate to True are considered **Truthy**.

"Conditions will consider some values in other data types equivalent to True and False. 
When used in conditions, 0, 0.0, and '' (the empty string) are considered False, while all other values are considered True."         
**Source: Automate the Boring Stuff with Python**

*You can check if a value is either truthy or falsy with the built-in `bool()` function.*

  According to the **Python Documentation**, this function:

      Returns a Boolean value, i.e. one of `True` or `False`. x (the argument) is converted using the standard truth testing procedure.

*With the special method `__bool__()`, you can set a "customized" condition that will determine when an object of your class will evaluate to `True` or `False`.*

  According to the **Python Documentation**:

      By default, an object is considered true unless its class defines either a __bool__() method that returns False or a __len__() method that returns zero, when called with the object.

## ❌ Falsy Values

These values evaluate to False:

- `None`
- `False`
- Zero of any numeric type: `0, 0.0, 0j`
- Empty sequences and collections: `'', [], (), {}, set(), range(0)`

## ✅ Truthy Values

These values **evaluate to `True`** in a Boolean context:

- Non-empty strings : `"hello"`, `"0"`
- Non-zero numbers : `1`, `-3.14`
- Non-empty lists : `[1, 2]`
- Non-empty lists, tuples, sets, and dictionaries : ` ``, (0,), {'a': 1}, {'key': 'value'} `
- `True`

## 📘 Why It Matters

Understanding truthy and falsy values helps with:

- Writing cleaner and concise code
- Avoiding unnecessary comparisons
- Debugging control flow issues
