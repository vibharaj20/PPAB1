from hotel_manager import Hotel_Manager

z = Hotel_Manager()

while True:

        ch = input("1.Enter Coustmer Details\n2.Calculate room bill\n3.Calculate Restraunt bill\n4.Calculate Laundry bill\n5.Calculate Gaming bill\n6.Display\n7.Exit")

        if ch=='1': 
        	z.coustmer_details()

        elif ch=='2':
        	z.room_bill()

        elif ch=='3':
        	z.food_bill()

        elif ch=='4':
        	z.laundry_bill()

        elif ch=='5':
        	z.game_bill()

        elif ch=='6':
        	z.display()

        else:
            print("Invalid")        

     		






	

		
		
			
			