import re
class User:
    match_tickets=[[111,100,0],[789,500,0],[234,250,0],[456,300,0],[845,500,0]]
    list1=["Bangalore","Chennai","Kolkata"]
    cities=[(101,"Chinnaswamy stadium","Bangalore"),(102,"Chidhambaram stadium","Chennai"),(103,"Eden Garden","Kolkata")]
    match_list=[(101,111,"Ind vs Pak","25-05-2023","7.00pm"),(101,789,"Aus vs Srilanka","14-07-2023","10.00am"),(102,234,"Ind vs South Africa","14-05-2023","12.00am"),(102,456,"Chennai vs Bangalore","13-07-2023","09.30pm"),(103,845,"Ind vs West indies","14-11-2023","11.00am")]
    values= None
    values1=None
    contacts={'priya': {'phone': '9874563210', 'email': 'p@gmail.com', 'password': '123'},'surya': {'phone': '7896541230', 'email': 's@gmail.com', 'password': '987'}}

    def reg(self,user_name,phone_number,email_id,password):
        self.__user_name=user_name
        self.__phone_number=phone_number
        self.__email_id=email_id
        self.__password=password
        contact=dict(phone=self.__phone_number,email=self.__email_id,password=self.__password)
        User.contacts[self.__user_name]=contact
        print(User.contacts)
        print("Registration is successfull")
    
    def select_venue(self,city):
        self.city=city
        #print(self.cities)
        for i in User.cities:
            if i[2]==self.city:
                print(f"You select the venue {i[0]},{i[1]},{i[2]}")
                User.values1=i   #(101,"Chinnaswamy stadium","Bangalore")
                return i
    
    def select_match(self,venue_id,date):
        self.venue_id=venue_id
        self.date=date
        for i in User.match_list:
            if i[0]==self.venue_id:
                if i[3]==self.date:
                    print(f"You select the match {i[1]},{i[2]},{i[3]},{i[4]}")
                    User.values=i  #(101,111,"Ind vs Pak","25-05-2023","7.00pm")
                    #print("hai",User.values)
                    return i
    def check_tickets(self,match_id):
        self.match_id=match_id
        for i in User.match_tickets:
            if i[0]==match_id:
                print("Available tickets are",i[1])
                return i
    def view(self):
        any=input("Do you see the venue and matches available (yes/no)")
        
        i=0
        while i<2:
            if any=="yes":
                print(f"These are the available cities\n1.{User.list1[0]}\n2.{User.list1[1]}\n3.{User.list1[2]}")
                city=input("enter a city")
                city=city.title()
                i=0
                while i<2:
                    if not city.isalpha():
                        print("enter a string")
                        city=input("enter a city")
                        city=city.title()
                    if city not in User.list1:
                        print("enter a available city")
                        city=input("enter a city")
                        city=city.title()
                    else:
                        city_name=obj.select_venue(city)   #city_name=(102, 'Chidhambaram stadium', 'Chennai')
                        venue_id=city_name[0]
                        print("Your available match lists in ",city_name[2])
                        for i in User.match_list:
                            if venue_id==i[0]: 
                                print(f"{i[1]},{i[2]},{i[3]},{i[4]}")
                        date=input("enter a date in format dd-mm-yyyy")
                        i=0
                        while i<2:
                            def check(date):
                                for i in User.match_list:
                                    if date in i:
                                        return date
                                else:
                                    return None
                            check1=check(date)
                            if check1:
                                match_selection=obj.select_match(venue_id,date)
                                i=3
                            else:
                                print("invalid date")
                                date=input("enter a date in format dd-mm-yyyy")
                            
                        match_id=match_selection[1]     #match_selection=(101,111,"Ind vs Pak","25-05-2023","7.00pm")
                        nothing= obj.check_tickets(match_id)  #nothing=[111,100,0]
                        i=2
                        return nothing
            elif any=="no":
                print("Thank you")
                i=3
                
            else:
                any=input("Do you see the venue and matches available (yes/no)")
        
    def booking_ticket(self):
        print("Register user only can be book the tickets")
       
    def cancel_ticket(self):
        print("Register user only can be cancel the tickets")

        
class Registered_user(User):
    history={}
    booked=[]
    
    def login_user(self):
        print("welcome to login page")
        email_id=input("enter email id")
        while not email_id.endswith("@gmail.com"):
            if not email_id.endswith("@gmail.com"):
                print("enter proper email id")
                email_id=input("enter email id")
        password=input("enter a password")
        def match(email_id,password):
            for i,j in User.contacts.items():
                if j["email"]==email_id and j["password"]==password:
                    return i
            return None
        matched=match(email_id,password)
        if matched:
            print("login successfull")
        else:
            print("Invalid email and password")
            obj.login_user()
        
        
#'priya': {'phone': '9632587410', 'email': 'p@gmail.com', 'password': '789'},'surya:':{'phone':7896541230,'email':'s@gmail.com','password':'098'}
    def booking_ticket(self):
        obj.login_user()
        Registered_user.booked=obj.view()  #booked=[111,100,0]
        #print(Registered_user.booked)
        booking=input("Do you want to book a ticket(yes/no)")
        if booking=="yes":
            if Registered_user.booked[1]!=0:
                #print("No of tickets available",Registered_user.booked[1])
                no_of_seats=int(input("enter a no.of tickets"))
                card=input("Please enter the card details")
                while not card.isdigit() or len(card)!=8:
                    if not card.isdigit():
                        print("enter numbers only")
                        card=input("Please enter the card details")
                    if len(card)!=8:
                        print("enter 8 digit card number")
                        card=input("Please enter the card details")

                count=0
                while count<1:
                    if no_of_seats<=Registered_user.booked[1]:
                        Registered_user.booked[2]=Registered_user.booked[2]+no_of_seats                    
                        print("you booked",Registered_user.booked[2])
                        Registered_user.booked[1]=Registered_user.booked[1]-no_of_seats
                        #print("Available seats",Registered_user.booked[1])
                        count=count+1
                        #print("ss",Registered_user.match_tickets)
                        #print("kk",Registered_user.values)
                        #obj.booking_history()
                        #obj.cancel_ticket()
                        modify=input("do you want modify your booking(yes/no)")
                        if modify=="yes":
                            choice=input("1.press 1 for cancel\n2.press 2 for view booking history\n3.press 3 for exit")
                            if choice=="1":
                                obj.cancel_ticket()
                                return
                                
                            if choice=="2":
                                obj.booking_history()
                                return
                    else:
        
                        print("Tickets are not available")
                        no_of_seats=int(input("enter a no.of tickets"))
            
    def booking_history(self):
        print("your booking history is")
        Registered_user.history=dict(match_name=Registered_user.values[2],match_date=Registered_user.values[3],match_time=Registered_user.values[4],match_venue=Registered_user.values1[1],match_place=Registered_user.values1[2],book_tickets=Registered_user.booked[2])
        #print(Registered_user.history)
        print(Registered_user.values[0],Registered_user.values[2],Registered_user.values[3],Registered_user.values[4],Registered_user.values1[1],Registered_user.values1[2],Registered_user.booked[2],"seats booked")
        #headers=["match_name","match_date","match_time","match_venue","match_place","booked_ticket"]
        #print(tabulate(Registered_user.history.values(),headers=headers))
        #Registered_user.history=dict({Registered_user.booked[0]:his})
        #print(Registered_user.history)
        #dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})

    def cancel_ticket(self):
        match_id=int(input("enter a match id"))
        no_of_cancel=int(input("enter a cancel tickets"))
        for i in Registered_user.match_tickets:
            #print(i[0])
            if i[0]==match_id:
                if i[2]>=no_of_cancel:
                    i[2]=i[2]-no_of_cancel
                    i[1]=i[1]+no_of_cancel
                    Registered_user.history=dict(match_name=Registered_user.values[2],match_date=Registered_user.values[3],match_time=Registered_user.values[4],match_venue=Registered_user.values1[1],match_place=Registered_user.values1[2],book_tickets=Registered_user.booked[2])
                    dic=dict(cancel_tic=no_of_cancel)
                    Registered_user.history.update(dic)
                    print(Registered_user.history)
                    print("you cancelled",no_of_cancel)
                    
                else:
                    print("enter less than booked tickets")  #Registered_user.booked=[111,100,0]            
            
            
        
class Guest_user(User):
    detail={}
    def details(self,name,email):
        self.name=name
        self.email=email
        con=self.name,self.email
        Guest_user.detail["Guest_user"]=con
        print(Guest_user.detail)
        obj1.view()
        obj1.booking_ticket()
    
        
    
        
        
        
print("Welcome to cricket booking service")

obj=Registered_user()
obj1=Guest_user()
i=0
while i<4:
    choose=input("1.Register\n2.Login\n3.Guest user\n4.Exit")
    if choose=="1":
        user_name=input("enter name")
        while not user_name.isalpha():
            if not user_name.isalpha():
                print("Enter a name properly")
                user_name=input("enter name")
        phone_number=input("enter number")
        while not phone_number.isdigit() or len(phone_number)!=10:
            if not phone_number.isdigit():
                print("enter only numbers")
            if len(phone_number)!=10:
                print("enter only 10 digit")
                phone_number=input("enter number")
        email_id=input("enter email id")
        while not email_id.endswith("@gmail.com"):
            if not email_id.endswith("@gmail.com"):
                print("enter proper email id")
                email_id=input("enter email id")
        password=input("enter a password")
        obj.reg(user_name,phone_number,email_id,password)
        choose=0
    if choose=="2":
        obj.booking_ticket()
    if choose=="3":
        print("Welcome to you are a Guest user")
        name=input("enter name")
        while not name.isalpha():
            if not name.isalpha():
                print("Enter a name properly")
                name=input("enter name")
        email=input("enter your email")
        while not email.endswith("@gmail.com"):
            if not email.endswith("@gmail.com"):
                print("enter proper email id")
                email=input("enter email id")
        obj1.details(name,email)
        
        

    if choose=="4":
        i=5
        
#list1=[(101,Chinnaswamy stadium,Bangalore),(102,Chidhambaram stadium,Chennai),(103,Eden Garden,Kolkata)]



