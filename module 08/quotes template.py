quotes =[
    {
"anime": "MAGI: The Labyrinth Of Magic",
"character": "Aladdin",
"quote": "I've learned that from a war ignited by revenge, nothing can be born, but sorrow."
},
{
"anime": "Mondaiji-tachi Ga Isekai Kara Kuru Sou Desu Yo?",
"character": "Izayoi Sakamaki",
"quote": "Not taking the initiative to secure your future but just waiting for luck to come your way, wasn't that just the definition of being lazy?"
},
{
"anime": "Super Dangan Ronpa 2",
"character": "Chiaki Nanami",
"quote": "Believe in yourself... If you don’t have that... it doesn’t matter how many talents you have, you still won’t be able to hold your head up high..."
},
{
"anime": "Fruits Basket",
"character": "Honda Tohru",
"quote": "[in her head] My happiness comes from the kindness of those around me."
},
{
"anime": "ReLIFE",
"character": "Kaizaki Arata",
"quote": "There is no right answer for getting along. Different people require different answers."
},
{
"anime": "Avatar: The Last Airbender",
"character": "Roku",
"quote": "In the avatar state... You're at your most powerful, but you're also...at your most vulnerable. If you're killed in the avatar state, the reincarnation cycle will be broken and the avatar will cease to exist."
},
{
"anime": "Death Note",
"character": "L Lawliet",
"quote": "Let's value our lives."
},
{
"anime": "Fullmetal Alchemist",
"character": "Maes Hughes",
"quote": "Yeah, it's still a nameless sniper. It's become quite a topic among us. She's still a cadet from the military academy, but at any rate she's got a good arm. It seems she's been brought all the way out here. Hah... to think they have to pull out even a little chick like that... this must be the end."
},
{
"anime": "Fruits Basket",
"character": "Sohma Kyo",
"quote": "If you love someone, they could make you sad. They could even make you feel lonely sometimes. But, that someone can also make you happier than you'll ever be."
},
{
"anime": "Naruto",
"character": "Hatake Kakashi",
"quote": "Leaf Village Secret-Finger Justu...1,000 Years of Death!!! *sticks his fingers up Naruto's ass*"
}
]
# print(type(quotes[0]))

for quote in quotes:
    character = quote.get('character')
    q = quote.get('quote')
    template = f'{character} says, "{q}"'
    print(template)
    print('*'* 10)