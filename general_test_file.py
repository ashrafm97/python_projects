from general_run_file import return_formatted_name

# test set up

known_input = '   Ashraf     '
expected_output = 'Ashraf'

#testing execution

print("testing function return_formatted_name() with '   Ashraf     ' ---> 'Ashraf'")
print(return_formatted_name(known_input)) == (expected_output)

from general_run_file import say_hello_name

known_input_say_hello = 'Hussain'
expected_output_say_hello = 'hello Hussain'

print("Testing function say_hello_name() with 'hello Hussain   ' ---> 'hello Hussain'")
print(say_hello_name(known_input_say_hello) == (expected_output_say_hello))

print(say_hello_name(known_input_say_hello))


