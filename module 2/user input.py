# multi_line_str = """
# Anonta the great make a movie
# with Barsha Apu, name Din the day
# """
#
# print(multi_line_str)

"""
The Mobile is released on 26th September.
It's model is Xiaomi Note 96
Camera: 200M
Price in Bangladesh: 500 BDT
"""
release_date = input('Enter mobile release date: ')
model = input("Enter Mobile Model: ")
camera = input("Enter Camera Megapixel: ")
price = input("Price in Bangladesh: ")

# print(release_date,model,camera, price)
template = f"""
The Mobile is released on {release_date}.
It's model is {model}
Camera: {camera}M
Price in Bangladesh: {price} BDT
"""
print(template)

