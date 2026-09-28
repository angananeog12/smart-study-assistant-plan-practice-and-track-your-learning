class Practice:
   def start(self,subject):
      print("\n-------------------------")
      print(subject,"PRACTICE TEST")
      print("-------------------------")

      #CALCULUS

      if subject.lower()=="calculus":

         questions=[
           ("what is the derivative of x^2?","2x"),
           ("what is the derivative of x^3?","3x^2"),
           ("what is the integral of 2x?","x^2+C"),
           ("what is the derivative of sin(x)","cos(x)")
         ]

      #PYTHON
      
      elif subject.lower()=="python":
      
          questions=[
            ("which keyword is used to define a function in python?","def"),
            ("which data type stores multiple values in a ordered way?","list"),
            ("which symbol is used for comments in python?","#"),
            ("wnich function is used to get the length of data type","len")
         ]
            
      #EVS
      
      elif subject.lower()=="evs":

         print("IN YOUR ANSWER THE FISRT LETTER SHOULD BE CAPITAL AND THE OTHER IN SMALL")
         
         questions=[
            ("what is the main source of engergy for earth?","Sun"),
            ("which gas is mainly responsible for global warming?","Carbon dioxide"),
            ("which layer protects Earth from harmful UV rays?","Ozone layer"),
            ("what is the process of planting trees called","Afforestation")
         ]

   #ENGLISH
   
      elif subject.lower()=="english":

         print("IN YOUR ANSWER THE FISRT LETTER SHOULD BE CAPITAL AND THE OTHER IN SMALL")
   
         questions=[
            ("what is the antonym of stern?","Lenient"),
            ("what is the antonym of Reorganise?","Disorganize"),
            ("what is the antonym of Filter?","Contaminate"),
            ("what is the antonym of Rarefy","Solidify")
            ]

      else:
         print("No test available for this subject.")
         return 0

# VERIFICATION

      score=0

      for i,(question, answer) in enumerate(questions,start=1):
         print("\nQ",i,".",question)

         user_answer = input("Your answer:")

         if user_answer.lower().strip()==answer.lower().strip():

            print("Correct.")
            score+=1
         else:
            print("Wrong.") 
            print("Correct answer:",answer)  

      print("\n.....TEST COMPLETED.....")    
      print("Subject:",subject)
      print("score:",score,"/",len(questions)) 
      print("..................................") 

      return score

                              
      