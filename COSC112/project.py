def main():
    total_tickets = total_tickets_sold()
    food_and_bev_tickets = food_and_bev()
    total_ticket, total_food_and_bev, total_income = total_income_generated(total_tickets, food_and_bev_tickets)
    display_total(total_ticket, total_food_and_bev, total_income)
    user_rating = int(input("How would you rate the concert on a scale of (1-5)? "))
    stars = rating(user_rating, '')
    print(stars, determine_rating(user_rating))


def rating(number, string):
    if number == 0:
        return string
    else:
        string+="* "
        return rating(number-1, string)

def display_total(tickets_sold, tickets_food_and_bev, total_income):
    print(f"The total number of tickets sold: is {tickets_sold}")
    print(f"The total number of tickets sold with food and beverages: {tickets_food_and_bev}")
    print(f"The total amount of income generated from the concert: $ {total_income}")

def total_income_generated(total_tickets, with_food_and_bev):
    class_A_without_food = total_tickets[1]- with_food_and_bev[0]
    class_B_without_food = total_tickets[2]- with_food_and_bev[1]
    class_C_without_food = total_tickets[3]- with_food_and_bev[2]
    total_income = (total_tickets[0]*100) +((class_A_without_food * 75) + (with_food_and_bev[0]* ((75*1.15)))) + ((class_B_without_food * 50) + (with_food_and_bev[1]* ((50*1.15)))) + ((class_C_without_food * 25) + (with_food_and_bev[2]* ((25*1.15))))
    
    return sum(total_tickets), sum(with_food_and_bev), total_income


def food_and_bev():
    class_A = int(input(('Enter the number Class A tickets sold with food and beverages: ')))
    class_B = int(input(('Enter the number Class B tickets sold with food and beverages: ')))
    class_C = int(input(('Enter the number Class C tickets sold with food and beverages: ')))
    return [class_A, class_B, class_C]


def total_tickets_sold():
    vip = int(input(('Enter the number of VIP tickets sold: ')))
    class_A = int(input(('Enter the number of Class A tickets sold: ')))
    class_B = int(input(('Enter the number of Class B tickets sold: ')))
    class_C = int(input(('Enter the number of Class C tickets sold: ')))
    return [vip, class_A, class_B, class_C]

def determine_rating(number):
    if number == 5:
        return "five-star rating , the concert was an absolute success"
    elif number == 4:
        return "4 out of 5 star rating, the concert was pretty good"
    elif number == 3:
        return "3 out of 5 star rating, the concert was typical average"
    elif number == 2:
        return "2 out of 5 star rating, he outcome of concert was not as expected but we can make improvements."
    elif number == 1:
        print("1 out of 5 star rating, he concert was a complete disaster!!!")

main()