#### Conditional test
* ##### how to ignore the case
    ```python
    car = 'Audi'
    car.lower() == 'audi'
    ```
    This will not affect the original `car`

* ##### find sth in or not in a list use `in` `not in`
    ```python
    'mushrooms' in requested_toppings
    ```
    ```python
    banned_users = ['andrew', 'carolina', 'david']
    user = 'marie'
    if user not in banned_users:
        print(f"{user.title()}, you can post a response if you wish.")
    ```
* ##### boolean expressions   
    ```python
    game_active = True
    can_edit = False
    ```

#### things about `if`
* ##### if-else chain: execute one of two possible situations
* ##### if-elif-else chain: ituations involve more than two possible conditions
    ```python
    age = 12
    if age < 4:
        print("Your admission cost is $0.")
    elif age < 18:
        print("Your admission cost is $25.")
    else:
        print("Your admission cost is $40.")
    ```
    * A better way: ==efficient== and easy to ==change== the ouput
    ```python
    age = 12
    if age < 4:
        price = 0
    elif age < 18:
        price = 25
    else:
        price = 40
    print(f"Your admission cost is ${price}.")
    ```
* ###### Omitting the else Block: kind of catshall statement
    * The else block is a **catchall** statement. It matches any condition that wasn’t matched by a specific if or elif test, and that can sometimes include invalid or even malicious data.

    * If you have a specific final condition you are testing for, consider using a final elif block and **omit** the else block.

    * As a result, you’ll gain extra confidence that your code will run only under the correct conditions.

* ###### Testing Multiple Conditions:
  * The if-elif-else chain is powerful, but it’s only appropriate to use when you just need one test to pass.
  As soon as Python finds one test that passes, it skips the rest of the tests. This behavior is beneficial, becakvuse it’s efficient and allows you to test for one specific condition.

  * However, sometimes **it’s important to check all of the conditions of interest. In this case, you should use a series of simple if statements with no elif or else blocks.**
  This technique makes sense **when more than one condition could be True, and you want to act on every condition that is True.**
      ```python
      requested_toppings = ['mushrooms', 'extra cheese']
      if 'mushrooms' in requested_toppings:
          print("Adding mushrooms.")
      if 'pepperoni' in requested_toppings:
          print("Adding pepperoni.")
      if 'extra cheese' in requested_toppings:
          print("Adding extra cheese.")
      print("\nFinished making your pizza!")
      ```
  * In summary, **if you want ==only one block== of code to run, use an ==if-elif-else== chain. If ==more than one block== of code needs to run, use a series of independent ==if== statements.**

#### Using `if` Statements with list
* ##### Checking for special items:
    ```python
    requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
            print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!") 
    ```
* ##### Checking That a List Is Not Empty:
    ```python
    requested_toppings = []
    if requested_toppings:
        for requested_topping in requested_toppings:
            print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
    else:
        print("Are you sure you want a plain pizza?")
    ```
* ##### Using Multiple Lists:
    ```python
    available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
    requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry, we don't have {requested_topping}.")       
    print("\nFinished making your pizza!")
    ```