from my_proj.sum_func import add, add_positive

# Implement your tests here.
def tests_sum_positive():
  assert add_positive(7,9)==16

def tests_sum_positive_negative():
  assert add_positive(-7,9)==None

def tests_sum_negative():
  assert add_positive(7,-9)==None

def tests_sum_both_negative():
  assert add_positive(-7,-9)==None

def tests_sum_less_than__or_equal_zero():
  assert add_positive(0,-9)==None

def tests_sum_if_a_and_b_are_not_equal():
  assert add_positive(5,-9)==None

def tests_type_check():
  assert type(add_positive(5,9))==int


#now add func

def tests_sum():
  assert add(3,2) == 5

def tests_sum_neg_number():
  assert add(-3,-2) == -5

def tests_sum_one_neg_one_positive_number():
  assert add(-3,2) == -1
def tests_add_type_check():
  assert type(add(3,2))==int

