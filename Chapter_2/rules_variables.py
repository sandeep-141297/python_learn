# A variable name can contain alphabets, digits, and underscores.
# A variable name can only start with an alphabet and underscores.
# A variable name can’t start with a digit.
# No while space is allowed to be used inside a variable name

you = 5
_me = 10

#22 = 'sandeep' #invalid
#san deep = '22' #invalid
#@name = 'sandeep' #invalid
#my@name = 'sandeep' #invalid

### ✅ **Valid Rules:**

#1. **Start with a letter or underscore (\_)**
name = "John"
_name = "John"
   

#2. **Followed by letters, digits (0–9), or underscores**
user1 = "Alice"
user_name2 = "Bob"
   

#3. **Case-sensitive**
name = "John"
Name = "Doe"  # different variable
   

#4. **No spaces allowed** (use `_` instead)
   #❌ `first name = "Tom"`
   #✅ `first_name = "Tom"`

#5. **Cannot use  keywords**
   #(like `if`, `for`, `while`, `class`, `def`, etc.)

   #❌ `if = 10`
   #✅ `my_if = 10`



### ❌ **Invalid Examples:**

#* `1name = "Sam"`  → ❌ starts with a digit
#* `user-name = "Max"`  → ❌ contains `-`
#* `class = "A"`  → ❌ `class` is a keyword



### ✅ **Best Practices (not rules but good to follow):**

#* Use **descriptive names**
  #`score`, `total_amount`, `user_email`

#* Use **lowercase\_with\_underscores** for variables
  #`student_name`, `total_marks`