#Wendy Pham
import python1_data
import project6view

#data set 
global bjh_movies
bjh_movies = (python1_data.string_films)

#Function returns a line of data
def return_line(bjh_movies : str) -> str:
    ''' Converts data set into list. 
        Returns the data found on specified line.'''
    data = (python1_data.string_films)
    global line
    line = data.splitlines()
assert return_line(1) != ''
assert return_line(0) != 0

#Function to display info for Barking Dogs Never Bite
def barkingChoice():
    ''' Prints specified data line.
        Prints correlating movie ratings.
        Prints correlating watch options.'''
    return_line(print(line[1], '\n'))
    print('Rotten Tomatoes Rating: 87%'
        '\nIMBd: 7/10'
        '\nMetacritic: 66%'
        '\nGoogle users: 83% liked this movie')
    print("Premium Subscription: Hulu, Amazon Prime, Tubi, Sling TV")
    print("For Purchase: Vudu{$2.99}, iTunes{$3.99}")
    print("♡"*60)
#assert barkingChoice() != ''


#Function to display info for The Host
def hostChoice():
    ''' Prints specified data line.
        Prints correlating movie ratings.
        Prints correlating watch options.'''
    return_line(print(line[2], '\n'))
    print('Rotten Tomatoes Rating: 93%'
        '\nIMBd: 7.1/10'
        '\nMetacritic: 85%'
        '\nGoogle users: 87% liked this movie')
    print("Premium Subscription: Hulu, Amazon Prime, Tubi, Pluto TV, Vudu")
    print("For Purchase: Youtube{$2.99}, Google{$2.99}, iTunes{$3.99}")
    print("♡"*60)
#assert hostChoice() != ''

#Function to display info for Memories of Murder    
def momChoice():
    ''' Prints specified data line.
        Prints correlating movie ratings.
        Prints correlating watch options.'''
    return_line(print(line[3], '\n'))
    print('Rotten Tomatoes Rating: 91%'
        '\nIMBd: 8.1/10'
        '\nMetacritic: 82%'
        '\nGoogle users: 93% liked this movie')
    print("Premium Subscription: Not Available")
    print("For Purchase: iTunes{$3.99}")
    print("♡"*60)
#assert momChoice() != ''

#Function to display info for Mother    
def motherChoice():
    ''' Prints specified data line.
        Prints correlating movie ratings.
        Prints correlating watch options.'''
    return_line(print(line[4], '\n'))
    print('Rotten Tomatoes Rating: 96%'
        '\nIMBd: 7.8/10'
        '\nMetacritic: 79%'
        '\nGoogle users: 89% liked this movie')
    print("Premium Subscription: Hulu, Amazon Prime, Tubi, Vudu")
    print("For Purchase: Not Available")
    print("♡"*60)
#assert motherChoice() != ''

#Function to display info for Okja    
def okjaChoice():
    ''' Prints specified data line.
        Prints correlating movie ratings.
        Prints correlating watch options.'''
    return_line(print(line[5], '\n'))
    print('Rotten Tomatoes Rating: 86%'
        '\nIMBd: 7.3/10'
        '\nMetacritic: 75%'
        '\nGoogle users: 89% liked this movie')
    print("Premium Subscription: Netflix")
    print("For Purchase: Not Available")
    print("♡"*60)
#assert okjaChoice() != ''

#Function to display info for Parasite    
def parasiteChoice():
    ''' Prints specified data line.
        Prints correlating movie ratings.
        Prints correlating watch options.'''
    return_line(print(line[6], '\n'))
    print('Rotten Tomatoes Rating: 98%'
        '\nIMBd: 8.6/10'
        '\nMetacritic: 96%'
        '\nGoogle users: 90% liked this movie')
    print("Premium Subscription: Hulu")
    print("For Purchase: Vudu{$3.99}, Amazon{$3.99}, Google{$3.99}, Youtube{$3.99}")
    print("♡"*60)
#assert parasiteChoice() != ''

#Function to display info for Snowpiercer    
def snowChoice():
    ''' Prints specified data line.
        Prints correlating movie ratings.
        Prints correlating watch options.'''
    return_line(print(line[7], '\n'))
    print('Rotten Tomatoes Rating: 94%'
        '\nIMBd: 7.1/10'
        '\nMetacritic: 84%'
        '\nGoogle users: 85% liked this movie')
    print("Premium Subscription: Netflix")
    print("For Purchase: Vudu{$3.99}, iTunes{$3.99}, Amazon{$3.99}")
    print("♡"*60)
#assert snowChoice() != ''

#Function to display info for Tokyo!    
def tokyoChoice():
    ''' Prints specified data line.
        Prints correlating movie ratings.
        Prints correlating watch options.'''
    return_line(print(line[8], '\n'))
    print('Rotten Tomatoes Rating: 76%'
        'IMBd: 7.1/10'
        'Metacritic: 63%'
        'Google users: 83% liked this movie')
    print("Premium Subscription: Tubi")
    print("For Purchase: Not Available")
    print("♡"*60)
#assert tokyoChoice() != ''

