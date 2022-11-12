import datetime as dt 
import pytz 
import pywhatkit as pwk
import time as t  





def sending_same_messages_to_people(count_no_of_people,time_in_hrs,time_in_mins,contacts_list,contact_names):


    message_to_be_sent = input("Enter what message to be sent: ")

    for i in range(0,count_no_of_people):
        sleep_time = 0


        difference_in_hrs = time_in_hrs[i] - dt.datetime.now(pytz.timezone('asia/kolkata')).hour
        difference_in_mins = time_in_mins[i] - dt.datetime.now(pytz.timezone('asia/kolkata')).minute

        print(f"Differnce in hrs is {difference_in_hrs} ")
        print(f"Differnce in mins is {difference_in_mins}")

        sleep_time = (((difference_in_hrs * 60 * 60)+(difference_in_mins * 60)) - 130)
        print(f'''The message is scheduled for {sleep_time} seconds i.e., {sleep_time/60} minutes and {(sleep_time)/(60*60)} Hours
        for {contacts_list[i]} named {contact_names[i]} ''')
        t.sleep(sleep_time)
        pwk.sendwhatmsg(("+91"+contacts_list[i]), message_to_be_sent,time_in_hrs[i], (abs(time_in_mins[i])),True)




def sending_different_messages_to_people(count_no_of_people,time_in_hrs,time_in_mins,contacts_list,contact_names):



    messages_to_be_sent = []
    for i in range(0,count_no_of_people):
        msgs = input(f"Enter what message do you want to send for {contacts_list[i]} named {contact_names[i]} :")
        messages_to_be_sent.append(msgs)

    for i in range(0,count_no_of_people):
        sleep_time = 0


        difference_in_hrs = time_in_hrs[i] - dt.datetime.now(pytz.timezone('asia/kolkata')).hour
        difference_in_mins = time_in_mins[i] - dt.datetime.now(pytz.timezone('asia/kolkata')).minute

        print(f"Differnce in hrs is {difference_in_hrs} ")
        print(f"Differnce in mins is {difference_in_mins}")

        sleep_time = (((difference_in_hrs * 60 * 60)+(difference_in_mins * 60)) - 130)
        print(f'''The message is scheduled for {sleep_time} seconds i.e., {sleep_time/60} minutes and {(sleep_time)/(60*60)} Hours
        for {contacts_list[i]} named {contact_names[i]} ''')
        t.sleep(sleep_time)
        pwk.sendwhatmsg(("+91"+contacts_list[i]), messages_to_be_sent[i],time_in_hrs[i], (abs(time_in_mins[i])),True)






if __name__ == '__main__':
    contacts_list = []
    contact_names = []
    time_in_hrs = []
    time_in_mins = []

    while(True):
        try:
            count_no_of_people = int(input("Enter to how many people do you want to send a message: "))
            break
        except: 
            print("Please Enter an integer number only ! ")
        
    
    print("NOTE: Please follow 24Hrs format TIme ! ")    
    for i in range(0,count_no_of_people):
        while(True):
            try:
                time_in_hrs_var = int(input(f"Enter the time in hrs for person {i+1}: "))
                time_in_hrs.append(time_in_hrs_var)
                
            except: 
                print("Please enter an integer value ")
                continue
            try:
                time_in_mins_var = int(input(f"Enter the time in mins for person {i+1}:  "))
                time_in_mins.append(time_in_mins_var)
                if((type(time_in_hrs_var) == type(10)) and (type(time_in_mins_var) == type(10))):
                    break
            except: 
                print("Please enter an integer value ")
                continue
                

    # tab_close_or_not = bool(input("Enter 'True' if you want to close the tab after sending the message \n or\nEnter 'False' if you dont want to close the whatsapp web tab: "))
    # if(tab_close_or_not == True):
        # tab_close_time = int(input("Enter after how many seconds do you want to close the tab, sending the message: "))

    for i in range(0,count_no_of_people):
        contact_num = input(f"Enter the contact {i+1}: ")
        contacts_list.append(contact_num)
        contact_name = input(f"Enter the contact name of {contact_num}: ")
        contact_names.append(contact_name)

    for i in range(0,count_no_of_people):
        print(f"The name of the contact {contacts_list[i]} is {contact_names[i]} ")





    print(f"Time in hrs list {time_in_hrs} :" )
    print(f"Time in mins list {time_in_mins} :" )

    print(f"Contact numbers list: {contacts_list } :")
    print(f"Contact names list: {contact_names } :")

    while(True):
        same_msgs_or_not = (input("Do you wanted to send same messages or unique messages?\nEnter 'same' to send same  message to all the persons or Enter 'different' to send different messages to each person : "))

        if(same_msgs_or_not  == 'same' or same_msgs_or_not == 'different'):
            flag = 1
            
        if(flag == 1):
            if(same_msgs_or_not.lower() == 'same'):
                sending_same_messages_to_people(count_no_of_people,time_in_hrs,time_in_mins,contacts_list,contact_names)

            elif(same_msgs_or_not.lower() == 'different'):
                sending_different_messages_to_people(count_no_of_people,time_in_hrs,time_in_mins,contacts_list,contact_names)
        else:
            continue

















