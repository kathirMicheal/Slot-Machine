import random

def spin_row():
    Symbols = ['🍒', '🥭', '🌟', '🤑', '🚨']
    
    return [random.choice(Symbols) for _ in range(3)]
    

def style_show(row):
    print("************")
    print(" | ".join(row))
    print("************")    

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 2
        if row[0] == '🥭':
            return bet * 3
        if row[0] == '🌟':
            return bet * 4
        if row[0] == '🤑':
            return bet * 5
        if row[0] == '🚨':
            return bet * 10
    return 0

def main():
    balance = 100
    
    print("******************************")
    print("Welcome to My Slot Machine Game")
    print("Symbols: 🍒 🥭 🌟 🤑 🚨")
    print("******************************")
    
    while balance > 0:
        print(f"current balance is {balance}")
        
        user_bet = input("Enter the bet amount:")
        
        if not user_bet.isdigit():
            print("Please Enter the valid Amount 💸 💸 💸")
            continue
        
        bet = int(user_bet)
        
        
        if bet > balance:
            print("Insufficient Balance")
            continue
        
        if bet <= 0:
            print("Amount must be greater than 0")
            continue
        
        balance -= bet
        
        row = spin_row()
        style_show(row)
        
        pay = get_payout(row, bet)
        
        if pay > 0:
            print(f"You win ${pay}")
        else:
            print("You lose the Round")
        
        balance += pay
        
        play_again = input("Do You want Spin Again (Y or N):").upper()
        
        if play_again != 'Y':
            break
        
    print("*****************************")        
    print(f"Game Over! Your balance is {balance}")
    print("*****************************")  
    
if __name__ == '__main__':
    main()
