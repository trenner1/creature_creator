import random
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Retrieve OpenAI API key from environment variables
client = OpenAI(api_key=api_key)

def generate_creature_name(creature1, creature2):
    """Generates a hybrid name from two creatures."""
    part1 = creature1[:len(creature1) // 2]
    part2 = creature2[len(creature2) // 2:]
    return f"{part1}{part2}" if random.random() < 0.5 else f"{creature2[:len(creature2) // 2]}{creature1[len(creature1) // 2:]}"

def generate_creature_stats():
    """Generates random statistics for the hybrid creature."""
    weight = random.randint(10, 1000)  # Weight in pounds
    diet = random.choice(["herbivore", "carnivore", "omnivore, pizzavore"])
    return weight, diet

def create_dalle_image(description):
    """Creates an image of the creature using OpenAI DALL-E."""
    response = client.images.generate(
        model="dall-e-3",
        prompt=description, 
        n=1, 
        size="1024x1024")
    image_url = response.data[0].url
    
    return image_url

def main():
    # Prompting the user for input
    creature1 = input("Enter the first creature: ")
    creature2 = input("Enter the second creature: ")

    # Generating hybrid creature details
    hybrid_name = generate_creature_name(creature1, creature2)
    weight, diet = generate_creature_stats()

    # Outputting the creature's information
    print(f"\nYour new hybrid creature: {hybrid_name}")
    print(f"Weight: {weight} lbs")
    print(f"Diet: {diet}")

    # Describing the hybrid creature
    description = f"A hybrid creature between {creature1} and {creature2}, named {hybrid_name}, weighing {weight} lbs and eating a {diet} diet."
    
    # Creating and displaying the creature image using DALL-E
    image_url = create_dalle_image(description)
    print(f"See your new hybrid creature here: {image_url}")

if __name__ == "__main__":
    main()
