


# The "pass" command tells Python to "do nothing".
# It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.
# Replace them with your own code as you complete the assignment.


# Import the json module to allow us to read and write data in JSON format.
import json,os

#global current_ques_list
#current_ques_list = []

# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
# CSP5110 Requirement: Also enforce a minimum value of 1.
def inputInt(prompt):
    while True:
        try:
            temp = int(input(prompt))    
            return temp
        except:
            continue


# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" of the brief
def inputSomething(prompt):
    global data_list
    question = input(prompt)
    return question
        
# This function opens "data.txt" in write mode and writes dataList to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the  brief.
def saveChanges(dataList):
    with open('data.txt', 'w') as outfile:
        json.dump(dataList, outfile)
    


# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the  brief.




# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the  brief.
# The rest is up to you.


print('Welcome to the Quizle Admin Program.')

            

with open('data.txt','r') as data_file:    
    data_text_file = json.load(data_file)
current_ques_list = []
while True:

    data_list = []
    print('Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').strip()
    try:
        if(type(choice)!='str'):
            raise Exception
    except Exception:
        if choice == 'a':
            # Add a new question.
            # See Point 3 of the "Requirements of admin.py" section of the  brief.
            
            question = str(inputSomething("Enter the question: ").strip()).lower()
            while True:
                if(question == ""):
                    question =str(inputSomething("Enter the question: ").strip()).lower()
                else:
                    break


            answer = []
            while True:
                x = str(input("Enter a valid answer (enter 'q' when done):").strip()).lower()
                if(x==''):
                    continue
                elif(x!='' and x!='q'):
                    answer.append(x)
                elif(x=='q' and len(answer)!=0):
                    break
                
            temp = inputInt('Enter question difficulty (1-5)')
            while True:
                if(temp < 1 or temp >5):

                    print("Invalid value. Must be an integer between 1 and 5")
                    temp = inputInt('Enter question difficulty (1-5)')
                else:
                    break

            
            diff = temp
        
            final_object = {'question':question,'answer':answer,'diff_level':diff}
            data_list.append(final_object)
            current_ques_list.append(final_object)
            if(os.stat("data.txt").st_size == 0):
                saveChanges(data_list)
            else:
                #with open('data.txt','r') as data_file:    
                #    data = json.load(data_file)

                #print(data_text_file)
                for i in data_list:
                    data_text_file.append(i)
                saveChanges(data_text_file)
            
        
        elif choice == 'l':
            # List the current questions.
            # See Point 4 of the "Requirements of admin.py" section of the  brief.
            if(len(current_ques_list)==0):
                print("No questions saved")
            else:
                print("Current Question:")
                for i in range(0,len(current_ques_list)):
                    print('\t',i+1,")",current_ques_list[i]['question'])    



        elif choice == 's':
            # Search the current questions.
            # See Point 5 of the "Requirements of admin.py" section of the  brief.
            search_term = inputSomething("Enter a search term: ").strip()
            
            
            for i in range(len(current_ques_list)):
                if search_term in current_ques_list[i]['question']:
                    print("Search results:")
                    print('\t',i+1,')',current_ques_list[i]['question'])
        


        elif choice == 'v':
            # View a question.
            # See Point 6 of the "Requirements of admin.py" section of the  brief.
            view_index = inputInt('Question number to view: ')
            
            try:
                req_data = current_ques_list[view_index-1]
                print("Question:")
                print("\t",req_data['question'])
                print("\t","Valid Answers: ",', '.join(req_data['answer']))
                print("\t","Difficulty: ",req_data["diff_level"])
                
            except:
                print("Invalid index number")

            

        elif choice == 'd':
            # Delete a question.
            # See Point 7 of the "Requirements of admin.py" section of the  brief.
            try:
                del_index = int(inputInt('Question number to delete: '))-1
                if(del_index+1>len(current_ques_list)):
                    print("Invalid index number")
                else:
                    del_question = current_ques_list.pop(del_index)
                    
                    #saveChanges(current_ques_list)
                    
                    #with open('data.txt','r') as data_file:    
                    #    temp_list = json.load(data_file)
                    #print(data_text_file)
                    for i in range(len(data_text_file)):
                        if(data_text_file[i]['question']==del_question['question']):
                            del data_text_file[i]
                    
                    
                    
                    try:
                        #print('try',data_text_file)
                        with open('data.txt', 'w') as outfile:
                            json.dump(data_text_file, outfile)
                    
                    except:
                        print("Invalid index number")
            except:
                pass



        elif choice == 'q':
            # Quit the program.
            # See Point 8 of the "Requirements of admin.py" section of the  brief.
            print("GoodBye!")
            break



        else:
            # Print "invalid choice" message.
            # See Point 9 of the "Requirements of admin.py" section of the  brief.
            print("Invalid choice")
            continue
