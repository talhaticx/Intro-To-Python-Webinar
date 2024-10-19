#################################
#      ### STR TO INT ###       #
#################################

str_num = "987"
int_num = int(str_num)  # Converts string "100" to integer 100

#################################
#      ### INT TO FLOAT ###     #
#################################

int_val =78
float_val = float(int_val)  # Converts integer 5 to float 5.0

#################################
#      ### FLOAT TO INT ###     #
#################################

float_num = 3.9
int_from_float = int(float_num)  # Converts float 3.99 to integer 3 

#################################
#     ### INT TO STR ###        #
#################################

num = 1919
str_from_int = str(num)  # Converts integer 1919 to string "1919"

#################################
#    ### BOOL TO INT ###        #
#################################

bool_val = False
int_from_bool = int(bool_val)  # Converts True to 1, and False to 0

#################################
#    ### PRINT OUTPUT ###       #
#################################

print(f"Original str_num: {str_num}, Converted to int: {int_num}, type: {type(int_num)}")
print(f"Original int_val: {int_val}, Converted to float: {float_val}, type: {type(float_val)}")
print(f"Original float_num: {float_num}, Converted to int: {int_from_float}, type: {type(int_from_float)}")
print(f"Original num: {num}, Converted to str: {str_from_int}, type: {type(str_from_int)}")
print(f"Original bool_val: {bool_val}, Converted to int: {int_from_bool}, type: {type(int_from_bool)}")
