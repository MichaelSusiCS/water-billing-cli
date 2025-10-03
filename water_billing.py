customer_code = str(input('Enter customer code (R, C, or I):')) # Get the customer code
if (not(customer_code == 'R')) and (not(customer_code == 'C')) and (not(customer_code == 'I')): # Check if customer_code is valid
    print('Invalid input (customer code)')
else:
    start_reading = int(input('Enter beginning reading ( between 0 and 999999999):')) # Get input for beginning reading
    end_reading = int(input('Enter ending reading ( between 0 and 999999999):')) # Get input for end reading

    if (not(0 <= start_reading <= 999999999)) or (not(0 <= end_reading <= 999999999)): # Check if readings are in range
        print('Invalid input (beginning or ending reading value is out of the range)')
    else:
        start_reading /= 10 # convert to gallons
        end_reading /= 10 # convert to gallons
        old_end_reading = end_reading # set old_end_reading to end_reading to be shown later as the original end_reading before modifications
        old_start_reading = start_reading # set start_end_reading to start_reading to be shown later as the original start_reading before modifications
        if end_reading < start_reading: # add 100,000,000 to end_reading if it's less than start_reading
            end_reading = 100000000 + end_reading # Loop start_reading back around
            #used_gallons = end_reading + start_reading # add end and start reading together to used_gallons

        used_gallons = end_reading - start_reading # calc how many gallons are used

        if customer_code == 'R': # check if customer code is R
            to_bill = (used_gallons * 0.0005) + 5 # charge $0.0005 per gallon + $5
        elif customer_code == 'C': # check if customer code is C
            if used_gallons <= 4000000: # check if used_gallons is less than or equal to 4000000
                to_bill = 1000.00 # charge a flat rate of 1000
            else:
                to_bill = used_gallons * .00025 + 1000 # charge $0.00025 per gallon + $1000
        elif customer_code == 'I': # check if customer code is I
            if used_gallons <= 4000000:
                to_bill = 1000.00 # charge a flat rate of 1000
            elif 4000000 < used_gallons <= 10000000:
                to_bill = 2000.00 # charge a flat rate of 2000
            else:
                to_bill = (used_gallons * 0.00025) + 2000 # charge $0.00025 per gallon + $2000
        print('Customer code:', customer_code) # Print customer_code
        print('Beginning reading value in gallons and tenths of gallon', old_start_reading) # Print start_reading
        print('Ending reading value in gallons and tenths of gallon', old_end_reading) # Print end_reading
        print('Gallons of water used:', used_gallons) # Print used_gallons
        print(f'Amount billed: ${to_bill:.2f}') # Print to_bill




