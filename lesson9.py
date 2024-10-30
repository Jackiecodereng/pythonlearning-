#loops helps program to run until stop is typed
while True: # hello loops will run infinitly
    print('hello,loops') # press the red box to stop
    break # stops the loop from running


    # u have a list of numbers
scores = [90,87,67,57,21,52,32,15,45,85,42,32,62,41,62,85,89,91,94]

for score in scores: # prints one score at a time
    if score >=50 and score <=70 and score % 2 ==0: # prints any score above 50 , % this one is modulus which divides by 2 and gives  remainder if remainder is 0 that is even
     print(score)