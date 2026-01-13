# python notes

## virtual env

    - When you have two projects, and want same package with different versions, then venv helps.
    - It creates the virtaul env, where you can install the packages with that specific verison and you can use that directly into your code.
    - command to create a venv :
      - You can do that using ctrl+shift+P -> create virtual env -> select python version.
      - In terminal
        - `python -m venv .venv` & `source .venv/bin/activate` [Remember to put exact path what you've named your venv folder]
          - To check if venv is activated:
            - `which python` || `which pip`
        - And to deactivate `deactivate`
        - And it should be active:
          - If it doesn't show any .venv on terminal you can kill that terminal and open new.
          - You can view that right hand side of your vscode right below to your terminal written 3.12.3 (.venv) if its there, then you can continue to install the packages.
          - If you can't then click on that version and then select the .venv.
    - Same for this we have anaconda for managing python distributions and virtual env on your machine
    - Very popular, in Data Science.

## Packages

    - pip install is used to install the dependencies.
    - To upgrade the pip inside venv
      - `pip install --upgrade pip`

## Python inner working

    -

## strings

    - You can use both "name" & 'name'

## Identation is important in python

    - other programming languages use {} python use identation
      ```js
      - if score > 90
        - print("A grade")
      - else
        - print ("B grade")
      ```

    - In PEP8
      - Using 4 spaces for indentation (not tabs)
      - Naming conventions like user_name not userName
      - Where to put spaces around operators

## numbers
