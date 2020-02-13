print("HELLO everyone, Welcome to KBC \n")

money =[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]

def win_money(correct_answer):
		print(money[correct_answer-1])
		if money[correct_answer-1]==10000:
			print("\nCongrats! You have cleared the first stage. ")
		elif money[correct_answer-1]==320000:
			print("\nCongrats! You have cleared the second stage. ")
		elif money[correct_answer-1]==10000000:
			print("\nCongrations! You are the winner of this game......i.e have won Rs. 1 crore. ")


def start():
		
		question=[
					  "Which team won IPL in 2018",
					  "On which riverbank is Goa located?",
					  "Where is Fort William located ?",
					  "Which of these formulae is used to calculate the area of a rectangular agriculture field?",
					  "Which one of these festivals is celebrated during winter in India?",
					  "Which non-metallic element has the chemical symbol S?",
					  "In which country is Transylvania?",
					  "Which of the following was once a lifeline on the TV show 'Kaun Banega Crorepati'?",
					  "what time corresponds to 23:23 hours ?",
					  "The south-eastern coast of India is popularly called what ?",
					  "Which of these chief ministers has the middle name of Gangadharrao ?",
					  "Which of these diseases is caused by bacteria, not viruses ?",
					  "Which of these is produced in plants of Narora, Lakrapar and Tarapur ?",
					  "Which of these naval exercises is conducted jointly by India and Singapore?",
					  "Who did Dennis Lillee once reject as a fast bowler, and about whom he later jokingly said, 'I think I did him and game of cricket a favour' ?",

				  ]
		
		first_option=[	
						"RCB","Ganga",
					  	"Chennai","breadth-length",
					  	"Baisakhi","Sodium",
					  	"Germany","Tridev",
					  	"11:23PM",
					  	"Konkan","Manohar Parrikar",
					  	"Typhoid","Atomic Power","Varuna",
					  	"Irfan Pathan"

					 ]
		second_option=[	
						"SRH","Mandovi",
					   	"Goa","length * breadth * height",
					   	"Makar Sankranti","Selenium",
					   	"Libya","Triguni",
					   	"11.11PM","Malabar",
					   	"Siddaramaiah","Dengue","EVMs",
					   	"Malabar","Sourav Ganguly"

					  ]
		third_option=[	
						"KKR","Gomati",
					  	"Kolkata","length * breadth",
					  	"Naag Panchami","Silicon",
					  	"Romania","Trimurti",
					  	"7:23PM","Porbandar",
					  	"Vijay Rupani","Chikungunya","Coins",
					  	"Simbex","Sahin Tendulakar"
					  ]
		fourth_option=[	
						"CSK","Sabarmati",
						"Mysore","breadth/length",
						"Ganesh Chaturthi","Sulphur",
						"Poland", "Trilok",
						"9.11PM",
						"Coromandel", "Devendra Fadnavis",
						"Mumps","Rail Coaches","Slinex",
						"Brett Lee"
						]
		
		all_option=[
					first_option,second_option,
					third_option,fourth_option
					]
		
		wrong_answer=False
		
		correct_answer=0
		
		ans_key=[3,1,2,2,1,3,2,1,0,3,3,0,0,2,2]

		stage = 0

		
		while(wrong_answer!=True):
			
				
			print("\nQ." + question[stage])

			
			for Number,option in enumerate(all_option):
				print (str(Number+1)+". "+option[stage])
			
			answer=int(input("And your answer is.... "))

			key = (ans_key[stage]+1)
			
			if  key == answer:
				print("\nCongrats! You gave the correct answer and now you have won : Rs", end="")
				correct_answer+=1
				win_money(correct_answer)
			else:
				print("Sadly you gave the wrong answer")
				correct_answer=0
				wrong_answer=True
			
			if(correct_answer==15):
				break
			stage+=1
			
            
start()

