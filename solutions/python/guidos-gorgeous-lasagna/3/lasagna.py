EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = ""

def bake_time_remaining(actual_oven_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - actual_oven_time
    return remaining_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the total preparation time in minutes.

        :param number_of_layers: int - number of lasagna layers.
        :return: int - total preparation time (in minutes) based on 2 minutes per layer.

        Function that takes the number of lasagna layers and returns the total
        preparation time assuming each layer takes 2 minutes to prepare.
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time in minutes.

    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - baking time already spent in the oven.
    :return: int - total time (preparation + baking) elapsed so far.

    Function that takes the number of layers and the elapsed bake time
    and returns the sum of preparation time and elapsed baking time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

    

