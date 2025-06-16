#Use REPL and print the table of 5 using it. 

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")



'''
Let's break down how the following Python code works:

```python
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
```

### 🔁 Step-by-step Explanation:

---

### `for i in range(1, 11):`

* This is a **for loop**.
* `range(1, 11)` generates a sequence of numbers starting from **1** up to **10** (the `11` is **not included**).
* So `i` will take values: `1, 2, 3, ..., 10` one at a time.

---

### `print(f"5 x {i} = {5 * i}")`

* This is a **formatted string** (also called an **f-string**) that lets you embed Python expressions inside curly braces `{}`.
* Inside the string:

  * `{i}` will be replaced by the current value of `i`.
  * `{5 * i}` will calculate the product of 5 and `i`, then insert the result into the string.
* Example when `i = 3`:
  `print(f"5 x {i} = {5 * i}")` becomes
  `print("5 x 3 = 15")`

---

### 🔁 So what happens overall?

The loop runs 10 times, with `i` from 1 to 10, and each time it prints the line:

```
5 x i = result
```

### ✅ Final Output:

```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```
'''




