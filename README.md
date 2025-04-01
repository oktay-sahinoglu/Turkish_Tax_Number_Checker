# Turkish_Tax_Number_Checker
Extract Turkiye Tax Number from text.

## Installation
Just add `src/vkn_checker.py` file to your project.

## Usage
Assuming it is run from the path contains `vkn_checker.py`.

```
>>> from vkn_checker import VKN_Checker

```

```
>>> VKN_Checker.find_vkn("I want to apply and my Tax ID is 1234567890.")
['1234567890']

```

Let's change one digit to make Tax ID number invalid.

```
>>> VKN_Checker.find_vkn("I want to apply and my Tax ID is 1234567895.")
[]

```

You can also perform validation check.
```
>>> VKN_Checker.validate_vkn("1234567890")
True

>>> VKN_Checker.validate_vkn("1234567895")
False
```
