
import time
import car4 as c4
import car3 as c3
import car2 as c2
import car1 as c1
import bike1 as b1
import bike2 as b2
import bike3 as b3
import bike4 as b4
import intra_v50 as t1
import cycle1 as bc1
import cycle2 as bc2
import cycle3 as bc3
import cycle4 as bc4


def menu():
    while 1:
        print('Press 1 : For information about Cars')
        print('Press 2 : For information about Bike')
        print('Press 3 : For information about commercial vehicle')
        print('Press 4 : For information about Bicycle')
        print('Press 5 : For Exit')
        b=input(a+': ')
        match b:
            case '1':
                print('Wall-E: Welcome To The Car Section')
                print('Press 1 : I20')
                print('Press 2 : Swift Dzire')
                print('Press 3 : Creta')
                print('Press 4 : Venue')
                print('Press 5 : Menu')
                print('Please select the Car you are looking for')
                c=input('You: ')
                match c:
                    case '1':
                        print('I20 selected')
                        print('Hi! I\'m Wall-E I\'m here to help you')
                        print("!!!!You Can Press 1 to exit Anytime!!! Ask your Question")
                        while 1:
                            f1 = open("car1.txt", "a")
                            car1=input('You: ')
                            
                            if(car1=='1'):
                             f1.write("\n")
                             f1.close()
                             print('Have a Great Day! Its Great interacting with you! ')
                             exit()
                            
                            else: 
                             print('Wall-E : '+c1.user_res(car1))
                             f1.write("You: "+ car1)
                             f1.write("\n")
                             f1.write("Bot: " + c1.user_res(car1))
                             f1.write("\n")    
                        break
                    case '2':
                        print('Swift Dzire Selected')
                        print('Hi! I\'m Wall-E I\'m here to help you')
                        print("!!!!You Can Press 1 to exit Anytime!!! Ask your Question")

                        while 1:
                         f2 = open("car2.txt", "a")
                         car2=input('You: ')
    
                         if(car2=='1'):
                           f2.write("\n")
                           f2.close()
                           print('Have a Great Day! Its Great interacting with you! ')
                           exit()
     
                         else: 
                          print('Wall-E : '+c2.user_res(car2))
                          f2.write("You: "+ car2)
                          f2.write("\n")
                          f2.write("Bot: " + c2.user_res(car2))
                          f2.write("\n")   
                        break
                    case '3':
                        print('Creta Selected')  
                        print('Hi! I\'m Wall-E I\'m here to help you')
                        print("!!!!You Can Press 1 to exit Anytime!!! Ask your Question")

                        while 1:
                         f3 = open("car3.txt", "a")
                         car3=input('You: ')
    
                         if(car3=='1'):
                            f3.write("\n")
                            f3.close()
                            print('Have a Great Day! Its Great interacting with you! ')
                            exit()
                            
                         else: 
                            print('Wall-E : '+c3.user_res(car3))
                            f3.write("You: "+ car3)
                            f3.write("\n")
                            f3.write("Bot: " + c3.user_res(car3))
                            f3.write("\n")
                                                
                        break 
                    case '4':
                        print('Venue Selected')
                        print('Hi! I\'m Wall-E I\'m here to help you')
                        print("!!!!You Can Press 1 to exit Anytime!!! ask your Question")
                        while 1:
                            f4 = open("car4.txt", "a")
                            car4=input('You: ')
    
                            if(car4=='1'):
                             f4.write("\n")
                             f4.close()
                             print('Have a Great Day! Its Great interacting with you! ')
                             exit()
                            
                            else: 
                             print('Wall-E : '+c4.user_res(car4))
                             f4.write("You: "+ car4)
                             f4.write("\n")
                             f4.write("Bot: " + c4.user_res(car4))
                             f4.write("\n")
                        break 
                    case '5':
                        menu()
                        break
                    case _:
                        print('Invalid Choice')
                        menu()  
                break
            case '2':
                print('Wall-E: Welcome To The Bike Section')
                print('Press 1 : Royal Enfield')
                print('Press 2 : Bajaj Pulsar-220')
                print('Press 3 : KTM')
                print('Press 4 : TVS Apache')
                print('Press 5 : Menu')
                print('Please select the Bike you are looking for')
                d=input(a+': ')
                match d:
                    case '1':
                        print('Royal Enfield Selected')   
                        print('Hi! I\'m Wall-E I\'m here to help you')
                        print("!!!!You Can Press 1 to exit Anytime!!! ===>>> Ask your Question about Royal Enfield <<<===")
                        while 1:
                            fb1= open("bike1.txt", "a")
                            bike1=input('You: ')
                            
                            if(bike1=='1'):
                             fb1.close()
                             print('Have a Great Day! Its Great interacting with you! ')
                             exit()
                            
                            else: 
                             print('Wall-E : '+b1.user_res(bike1))
                             fb1.write("You: "+ bike1)
                             fb1.write("\n")
                             fb1.write("Bot: " + b1.user_res(bike1))
                             fb1.write("\n")
                        break
                    case '2':
                        print('Bajaj Pulsar-220 Selected')  
                        print('Hi! I\'m Wall-E I\'m here to help you')
                        print("!!!!You Can Press 1 to exit Anytime!!! ===>>> Ask your Question about Bajaj Pulsar-220 <<<===")
                        while 1:
                            fb2 = open("bike2.txt", "a")
                            bike2=input('You: ')
                            
                            if(bike2=='1'):
                             fb2.close()
                             print('Have a Great Day! Its Great interacting with you! ')
                             exit()
                            
                            else: 
                             print('Wall-E : '+b2.user_res(bike2))
                             fb2.write("You: "+ bike2)
                             fb2.write("\n")
                             fb2.write("Bot: " +b2.user_res(bike2))
                             fb2.write("\n")
                        break
                    case '3':
                        print('KTM Selected')
                        print('Hi! I\'m Wall-E I\'m here to help you')
                        print("!!!!You Can Press 1 to exit Anytime!!! Ask your Question about KTM <<<===")
                        while 1:
                            fb3 = open("bike3.txt", "a")
                            bike3=input('You: ')
                            
                            if(bike3=='1'):
                             fb3.close()
                             print('Have a Great Day! Its Great interacting with you! ')
                             exit()
                            
                            else: 
                             print('Wall-E : '+b3.user_res(bike3))
                             fb3.write("You: "+ bike3)
                             fb3.write("\n")
                             fb3.write("Bot: " + b3.user_res(bike3))
                             fb3.write("\n")   
                        break 
                    case '4':
                        print('TVS Apache Selected')   
                        print('Hi! I\'m Wall-E I\'m here to help you')
                        print("!!!!You Can Press 1 to exit Anytime!!! ===>>> Ask your Question about TVS Apache <<<===")
                        while 1:
                            fb4 = open("bike4.txt", "a")
                            bike4=input('You: ')
                            
                            if(bike4=='1'):
                             fb4.close()
                             print('Have a Great Day! Its Great interacting with you! ')
                             exit()
                            
                            else: 
                             print('Wall-E : '+b4.user_res(bike4))
                             fb4.write("You: "+ bike4)
                             fb4.write("\n")
                             fb4.write("Bot: " + b4.user_res(bike4))
                             fb4.write("\n")
                        break 
                    case '5':
                        menu()
                        break
                    case _:
                        print('Invalid Choice')
                        menu()
                break
            case '3':
                print('Wall-E: Welcome To The Commercial Vehicle Section')
                print('Hi! I\'m Wall-E I\'m here to help you')
                print("!!!!You Can Press 1 to exit Anytime!!! Ask your Question")
                ft1 = open("truck.txt", "a")
                while 1:
                        truck1=input('You: ')
                        
                        if(truck1=='1'):
                         ft1.write("\n")   
                         ft1.close()
                         print('Have a Great Day! Its Great interacting with you! ')    
                         exit()
                        else: 
                         print('Wall-E : '+t1.user_res(truck1))
                         ft1.write("You: "+ truck1)
                         ft1.write("\n")
                         ft1.write("Bot: " + t1.user_res(truck1))
                         ft1.write("\n")    
                break
            case '4':
                print('Wall-E: Welcome To The Bicycle Section')
                print('Press 1 : Hero Ranger')
                print('Press 2 : Hero DTB')
                print('Press 3 : Hero Sprint')
                print('Press 4 : Hero E-cycles')
                print('Press 5 : Menu')
                print('Please select the Bicycle you are looking for!')
                f=input(a+': ')
                match f:
                    case '1':
                        print('Hero Ranger Selected')   
                        print('Welcome To The Bicycle Section! I\'m Wall-E I\'m here to help you')
                        print("!!!!You Can Press 1 to exit Anytime!!!")
                        while 1:
                            fbc1 = open("bicycle1.txt", "a")
                            cy1=input('You: ')
                            if(cy1=='1'):
                             fbc1.write("\n")   
                             fbc1.close()
                             print('Have a Great Day! Its Great interacting with you! ')
                             exit()
                            
                            else: 
                             print('Wall-E : '+bc1.user_res(cy1))
                             fbc1.write("You: "+ cy1)
                             fbc1.write("\n")
                             fbc1.write("Bot: " + bc1.user_res(cy1))
                             fbc1.write("\n")
                        break
                    case '2':
                        print('Hero DTB Selected')
                        print('Welcome To The Bicycle Section! I\'m Wall-E I\'m here to help you')
                        print("!!!!You Can Press 1 to exit Anytime!!!")
                        while 1:
                            fbc2 = open("bicycle2.txt", "a")
                            cy2=input('You: ')
                            if(cy2=='1'):
                             fbc2.write("\n")
                             fbc2.close()
                             print('Have a Great Day! Its Great interacting with you! ')
                             exit()
                            
                            else: 
                             print('Wall-E : '+bc2.user_res(cy2))
                             fbc2.write("You: "+ cy2)
                             fbc2.write("\n")
                             fbc2.write("Bot: " + bc2.user_res(cy2))
                             fbc2.write("\n")
                        break
                    case '3':
                        print('Hero Sprint Selected')  
                        print('Welcome To The Bicycle Section! I\'m Wall-E I\'m here to help you')
                        print("!!!!You Can Press 1 to exit Anytime!!!")
                        while 1:
                                fbc3 = open("bicycle3.txt", "a")
                                cy3=input('You: ')
                                if(cy3=='1'):
                                 fbc3.write("\n")   
                                 fbc3.close()
                                 print('Have a Great Day! Its Great interacting with you! ')
                                 exit()
                                
                                else: 
                                 print('Wall-E : '+bc3.user_res(cy3))
                                 fbc3.write("You: "+ cy3)
                                 fbc3.write("\n")
                                 fbc3.write("Bot: " + bc3.user_res(cy3))
                                 fbc3.write("\n")
                        break 
                    case '4':
                        print('Hero E-Cycle Selected') 
                        print('Welcome To The Bicycle Section! I\'m Wall-E I\'m here to help you')
                        print("!!!!You Can Press 1 to exit Anytime!!!")
                        while 1:
                            fbc4 = open("bicycle4.txt", "a")
                            cy4=input('You: ')
                            if(cy4=='1'):
                             fbc4.write("\n")
                             fbc4.close()
                             print('Have a Great Day! Its Great interacting with you! ')
                             exit()
                            
                            else: 
                             print('Wall-E : '+bc4.user_res(cy4))
                             fbc4.write("You: "+ cy4)
                             fbc4.write("\n")
                             fbc4.write("Bot: " + bc4.user_res(cy4))
                             fbc4.write("\n")
                        break 
                    case '5':
                        menu()
                        
                        break
                    case _:
                        print('Invalid Choice')
                        menu()
                break

            case '5':
                print('Have a Great Day! Its Great interacting with you! ')
                exit()
                break     
            case _:
                print('invaild choice')
                time.sleep(1)



print('Hi! I\'m Wall-E I\'m here to help you')
time.sleep(.5)
print('Wall-E: May I Know your Name ?')
a=input('You: ')
print('Wall-E: Hello! '+a)
time.sleep(1)
print('Wall-E: How may I help you?')
menu()
