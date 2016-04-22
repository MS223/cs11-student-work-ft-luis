a = [1, 2, 4]
b = a
#updating b will not affect a because b is not equal to null
# input: a list of ints
# output: an int
def update_list(a_list):
    a_list[3] = "yo"
    b = a_list[4]
    b = 100
my_list = [1, 2, 3, 4, 5]
update_list(my_list)
print my_list
#I predct that my_list will print out 1,2,3,4,5
var_1 = "kittens"
var_2 = "cookies"
# input: a string
# output: a string
def my_function(my_favorite_things):
    song_lyrics = "rain drops on roses,"
    combined_song = song_lyrics + my_favorite_things
    return combined_song
# input: a string
# output: a string
def my_function_2(item, item2):
    full_lyrics = item + "on " + item2
    full_song = my_function(full_lyrics)
    return full_song
my_song = my_function_2(var_1, var_2)
