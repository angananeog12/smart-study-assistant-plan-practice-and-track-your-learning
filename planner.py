from datetime import datetime,timedelta

class Planner:
    def __init__(self):
        self.completed_subjects=[]

    def create(self,details):
        print("\n ......CREATE STUDY TIME TABLE......")
        print("\n ACCORDING TO YOUR DETAILS THAT YOU GAVE IN SIGN IN :")
        print("\n YOUR SUBJECT IS CALCULUS,PYTHON,EVS,ENGLISH")

        print("\nENTER THE SUBJECT IN SMALL LETTER (ALL LETTER SHOULD BE IN SMALL) ")
        
        details.sub1 = input("Enter the subject number one:")
        time1=int(input(f"Enter the study time for {details.sub1}(minutes):"))
        details.sub2 = input("Enter the subject number two:")
        time2=int(input(f"Enter the study time for {details.sub2}(minutes):"))
        details.sub3 = input("Enter the subject number three:")
        time3=int(input(f"Enter the study time for {details.sub3}(minutes):"))
        details.sub4 = input("Enter the subject number four:")
        time4=int(input(f"Enter the study time for {details.sub4}(minutes):"))

        start=input("\nEnter the starting time(HH:MM):")

        #convert starting time
        current_time = datetime.strptime(start,"%H:%M")

        subjects=[
            (details.sub1, time1),    
            (details.sub2, time2),
            (details.sub3, time3),    
            (details.sub4, time4),        
        ]

        print("\n...TIME TABLE CREATED...")

        print("Start Time:",current_time.strftime("%H:%M"))
        print()

        for subject,duration in subjects:

            start_time = current_time
            end_time = current_time + timedelta(minutes=duration)

            print(
                start_time.strftime("%I:%M %p"),"-",
                end_time.strftime("%I:%M %p"),"-",
                subject
                 )

            current_time=end_time

            # 15 minute break after every subject
            break_start= current_time
            break_end=current_time + timedelta(minutes=15)
            print(
                  break_start.strftime("%I:%M %p"),"-",
                  break_end.strftime("%I:%M %p"),"- BREAK"
                 )
            current_time=break_end
        return subjects

    #STUDY SESSION
    def session(self,subject,duration):
        print("----STUDY SESSION----")

        print("Subject:",subject)
        print("scheduled study time:",duration,"minutes")

        completed= input("Did you completed the scheduled study time?(yes/no):")  

        if completed.lower()=="yes":
            self.completed_subjects.append(subject)

            print("\nStudy session completed.")
            return True
        else:
            print("\nStudy session not completed")
            return False

       # unclock test
    def unlock(self,subject):   
        if subject in self.completed_subjects:
            print(f"\n{subject} TEST UNLOCKED.")

            return True
        else:
            print(f"\n{subject} TEST IS STILL LOCKED")

        # TEST UNLOCK    
    def show(self):
        print("\n....AVAILABLE TEST....")

        if len(self.completed_subjects)==0:

            print("NO test is unlocked yet.")

        else:

            for subject in self.completed_subjects:

                print("-",subject)       
