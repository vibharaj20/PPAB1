class Hotel_Manager:
	def __init__(self,name='', phno='', check_in='', check_out='',

		         total_room_bill=0, total_food_bill=0,

		         total_laundry_bill=0, total_game_bill=0, sub_total=0,

		         total=0, tax=800, room_no=101):


		print("-------------------WELCOME TO FOUR SEASONS-------------------")

		self.name = name

		self.phno = phno

		self.check_in = check_in

		self.check_out = check_out

		self.total_room_bill = total_room_bill

		self.total_food_bill = total_food_bill

		self.total_laundry_bill = total_laundry_bill

		self.total_game_bill = total_game_bill

		self.sub_total = sub_total

		self.total = total

		self.tax = tax

		self.room_no = room_no


	def coustmer_details(self):

		self.name=input("Enter your name")

		self.phno=float(input("Enter your ph. no"))

		self.check_in=str(input("Enter check in date"))

		self.check_out=str(input("Enter check out date"))

		print("your room no:", self.room_no)

		

	def room_bill(self):

		print("We have the following room options available")

		r = int(input("Enter the room you stayed in:\n1.Single room :2000 per night\n2.Double room:4000 per night\n3.Mini Suite:5000 per night\n4.Presidential Suite:10000 per night"))

		n = input("Enter the number of nights you stayed")

	


		if (r==1):
			print("You have opted for a Single room ")
			self.total_room_bill = 2000 * n



		if (r==2):
			print("You have opted for a Double room")
			self.total_room_bill = 4000 * n



		if (r==3):
			print("You have opted for a Mini Suite")
			self.total_room_bill = 5000 * n


		if (r==4):
			print("You have opted for a Presidential Suite")
			self.total_room_bill = 10000 * n


		else:
			print("Please choose a room")

		print("your total room bill is:", self.total_room_bill)	
	



	def food_bill(self):

		print("-------------------------FOOD MENU--------------------")
		
		f=int(input("1.water:20rs\n2.coffee:10rs\n3.tea:10rs\n4.breakfast buffet:250rs\n5.brunch buffet:300 rs\n6.lunch buffet:500rs\n7.dinner buffet:1000rs\n8.exit"))

		print("Enter your choice\n")	

            
		if (f==1):
			q = int(input("Enter quantity:"))
			self.total_food_bill = self.total_food_bill + 20 * q



		elif (f==2):
			q = int(input("Enter quantity:"))
			self.total_food_bill = self.total_food_bill + 10 * q



		elif (f==3):
			q = int(input("Enter quantity:"))
			self.total_food_bill = self.total_food_bill + 10 * q


			
		elif (f==4):
			q = int(input("Enter quantity:"))
			self.total_food_bill = self.total_food_bill + 250 * q


			
		elif (f==5):
			q = int(input("Enter quantity:"))
			self.total_food_bill = self.total_food_bill + 300 * q


			
		elif (f==6):
			q = int(input("Enter quantity:"))
			self.total_food_bill = self.total_food_bill + 500 * q


			
		elif (f==7):
			q = int(input("Enter quantity:"))
			self.total_food_bill = self.total_food_bill + 1000 * q

		else:
			print("Invalid choice")

		
		print("The total food bill is:",self.total_food_bill)

		
	def laundry_bill(self):


		print("------------------------LAUNDRY OPTIONS-------------------------------")

		l = int(input("1.shorts:10rs\n2.trousers:20rs\n3.shirt:20rs\n4.saree:30rs\n4.exit"))

		print("Enter your choice")


		if (l==1):
			n = int(input("Enter quantity:"))
			self.total_laundry_bill = self.total_laundry_bill + 10 * n

		elif (l==2):
			n = int(input("Enter quantity:"))
			self.total_laundry_bill = self.total_laundry_bill + 20 * n

			
		elif (l==3):
			n = int(input("Enter quantity:"))
			self.total_laundry_bill = self.total_laundry_bill + 20 * n


		elif (l==4):
			n = int(input("Enter quantity:"))
			self.total_laundry_bill = self.total_laundry_bill + 30 * n	
				

		else:
			print("Enter valid choice")


		print("The total laundry bill is:", self.total_laundry_bill)	



	def game_bill(self):


		print("------------------GAMING OPTIONS----------------------------")


		g = int(input("1.table tennis:100rs\n2.snooker:100rs\n3.bowling:250rs\n4.pool:300rs\n5.exit"))



		if (g==1):
			y = int(input("Enter number of hours:"))
			self.total_game_bill = self.total_game_bill + 100 * y



		elif (g==2):
			y = int(input("Enter number of hours:"))
			self.total_game_bill = self.total_game_bill + 100 * y



		elif (g==3):
			y = int(input("Enter number of hours:"))
			self.total_game_bill = self.total_game_bill + 250 * y



		elif (g==4):
			y = int(input("Enter number of hours:"))
			self.total_game_bill = self.total_game_bill + 300 * y

		else:
			print("invalid choice")
				
			
		print("The total gaming bill is:", self.total_game_bill)


	def display(self):

		print("--------------------HOTEL RECIEPT-------------------")

		print("Coustmer Details:")

		print("Coustmer Name:",self.name)

		print("Coustmer phone number:",self.phno)

		print("Chek in date:",self.check_in)

		print("Check out date",self.check_out)

		print("The total room bill is:",self.total_room_bill)

		print("The total restraunt bill is:",self.total_food_bill)

		print("The total laundry bill is:",self.total_laundry_bill)

		print("The total game bill is:",self.total_game_bill)

		self.sub_total=self.total_room_bill+self.total_food_bill+self.total_laundry_bill+self.total_game_bill

		print("The sub total is:",self.sub_total)

		print("The tax is:",self.tax)

		self.total=self.sub_total+self.tax

		print("The total amount is:",self.total)



