# STUDYSYNC: STUDY PLANNER AND TEST PRACTICE SYSTEM
from student import Student
from planner import Planner
from test import Practice
from performance import analysis
from Marks import recommendation

print("------SMART STUDY ASSISTANT: PLAN, PRACTICE & TRACK YOUR LEARNING------")

# student module
student = Student()
student.set()
student.show()

#planner module
planner=Planner()
subjects = planner.create(student)
subject=input("\nEnter the subject to study:")
for name,duration in subjects:
    if name.lower()==subject.lower():
        planner.session(name,duration)
        planner.unlock(name)
        break

planner.show()

#Test module
test = Practice()
score=test.start(subject)

#performance module
performance= analysis()
performance.analyze(score)

#Marks module
Marks=recommendation()
Marks.perform(score)


print(".....THANK YOU FOR USING THE SMART STUDY ASSISTANT: PLAN, PRACTICE & TRACK YOUR LEARNING.....")

