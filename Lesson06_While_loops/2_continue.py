#Continue statement
'''
continue - skips to next iteration

break - exit completely
continue - skips current iteration, keeps looping

'''

count = 0
while count < 5:
    count +=1
    if count == 3: 
        continue
    print(count)