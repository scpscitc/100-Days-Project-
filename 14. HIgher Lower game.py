import random
logo = """     __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/ """
vs = """ _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)"""
accounts = {
    "Cristiano Ronaldo, a Footballer, from Portugal." : 692,
    "Lionel Messi, a Footballer, from Argentina." : 504,
    "Selena Gomez, a Musician & Actress, from United States." : 428,
    "Kylie Jenner, a Businesswoman & Media Personality, from United States." : 397,
    "Dwayne Johnson, an Actor & Former Wrestler, from United States." : 398,
    "Kim Kardashian, a Media Personality & Businesswoman, from United States." : 364,
    "Beyoncé, a Musician, from United States." : 324,
    "Justin Bieber, a Musician, from Canada." : 290,
    "Zendaya, an Actress & Singer, from United States." : 198,
    "Emma Chamberlain, a YouTuber & Influencer, from United States." : 17,
    "Khaby Lame, a Content Creator, from Italy." : 80,
    "PewDiePie, a YouTuber & Gamer, from Sweden." : 21,
    "Charli D’Amelio, a Dancer & TikTok Star, from United States." : 49,
    "MrBeast, a YouTuber & Philanthropist, from United States." : 51,
    "Taylor Swift, a Musician, from United States." : 283,
    "Billie Eilish, a Musician, from United States." : 113,
    "Ariana Grande, a Musician & Actress, from United States." : 380,
    "Neymar Jr., a Footballer, from Brazil." : 221,
    "Bad Bunny, a Musician, from Puerto Rico." : 52,
    "BTS, a Music Band, from South Korea." : 75,
    "Chris Brown, a Musician, from United States.": 145,
    "Shakira, a Musician, from Colombia.": 90,
    "Jennifer Lopez, a Musician & Actress, from United States.": 252,
    "Drake, a Musician, from Canada.": 146,
    "Kendall Jenner, a Model & Media Personality, from United States.": 294,
    "Miley Cyrus, a Musician & Actress, from United States.": 216,
    "Nicki Minaj, a Musician, from United States.": 230,
    "Rihanna, a Musician & Businesswoman, from Barbados.": 152,
    "Shawn Mendes, a Musician, from Canada.": 73,
    "Gigi Hadid, a Model, from United States.": 80,
    "Will Smith, an Actor & Rapper, from United States.": 64,
    "LeBron James, a Basketball Player, from United States.": 158,
    "Virat Kohli, a Cricketer, from India.": 267,
    "Zayn Malik, a Musician, from United Kingdom.": 53,
    "Anushka Sharma, an Actress, from India.": 69,
}
print(logo)
point = 0
lost = False
A = random.choice(list(accounts))
while lost != True:
    B = random.choice(list(accounts))
    while B == A:
        B = random.choice(list(accounts))
    print(f"Compare A: {A}")
    print(vs)
    print(f"Compare B: {B}")
    choice = input("Who has more followers on Instagram? Type 'A' or 'B': ").lower()
    if choice == "a" and accounts[A] > accounts[B]:
        point = point+1
        print(f"Right answer! Your current point is {point}")
    elif choice == "b" and  accounts[A] < accounts[B]:
        point = point+1
        print(f"Right answer! Your current point is {point}")
    else:
        print(f"Game over.Your point is {point}")
        lost = True
    A = B



