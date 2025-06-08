# 🎯 "TRUTHY" AND "FALSEY" VALUES 
"Truthy" and "Falsey" refer to how Python evaluates objects in Boolean contexts, such as in if or while statements.

The basic rules are:
- Values that evaluate to False are considered **Falsey**.
- Values that evaluate to True are considered **Truthy**.

"Conditions will consider some values in other data types equivalent to True and False. 
When used in conditions, 0, 0.0, and '' (the empty string) are considered False, while all other values are considered True."         
**Source: Automate the Boring Stuff with Python**


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

- Writing cleaner if conditions
- Avoiding unnecessary comparisons
- Debugging control flow issues
