# Ask the user about the current weather conditions and provide clothing recommendations based on

weather = input("what's the weather like today? (sunny/rainy/cold): ")

if (weather == "sunny"):
    print("Wear a t-shirt and sunglasses.")
elif (weather == "rainy"):
    print("Don't forget your umbrella and a raincoat.")
else:
    print("Make sure to wear a warm coat and a scarf.")