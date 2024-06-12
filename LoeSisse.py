import csv
import turtle
import time

def convert_time_to_seconds(time_str):
    # Split the time string into its components
    minutes, seconds = time_str.split(':')
    # Convert minutes to seconds and add to the seconds part
    total_seconds = int(minutes) * 60 + float(seconds)
    # Round the total seconds to three decimal places
    total_seconds_rounded = round(total_seconds, 3)
    return total_seconds_rounded


def LoeSisse( driver_id, race_id):
    laptimes = []
    with open('lap_times.csv', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if row['driverId'] == str(driver_id) and row['raceId'] == str(race_id):
                # Convert the time format to seconds
                total_seconds = convert_time_to_seconds(row['time'])
                laptimes.append(total_seconds)
    return laptimes

def Soitjad( race_id): #Leiab kõik ühes sõidus võistelnud sõitjate id´d
    driver_ids = set()
    with open('lap_times.csv', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if row['raceId'] == str(race_id):
                driver_ids.add(row['driverId'])
    return list(driver_ids)


driver_id = 1  # Replace with the actual driverId
race_id = 955    # Replace with the actual raceId
pikkus = len(LoeSisse(driver_id, race_id))

racers = Soitjad(race_id)
KoikAjad = []
for i in range(len(racers)):
    id = racers[i]
    ajad = LoeSisse(id, race_id)
    KoikAjad.append(ajad)

print(KoikAjad)


number_of_drivers = len(KoikAjad)
number_of_laps = len(KoikAjad[0])

speed_factor = 10

screen = turtle.Screen()
screen.title('Race Simulation')

# Function to create a Turtle for each driver
def create_driver(color):
    driver = turtle.Turtle(shape='circle')
    driver.color(color)
    driver.penup()
    driver.speed(0)  # This is the animation speed, 0 means "fastest"
    return driver

# Initialize drivers and position them at the starting line
colors = ["red", "blue", "green", "orange", "purple", "pink", "yellow", "cyan", "magenta", "brown","plum",
    "salmon","sienna","teal","violet", "yellow","azure","coral","darkorange","lightblue","lime"]
drivers = [create_driver(colors[i % len(colors)]) for i in range(number_of_drivers)]

# Function to draw the race track
import turtle


def draw_track():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)

    track = turtle.Turtle()
    track.speed(0)  # Fastest drawing speed
    track.penup()

    # Starting point
    track.goto(-350, -250)

    # La Source Hairpin
    track.pendown()
    track.left(90)
    track.circle(50, 180)

    # Straight to Eau Rouge and Raidillon
    track.right(45)
    track.forward(100)

    # Eau Rouge and uphill Raidillon
    track.right(20)
    track.circle(-120, 45)

    # Kemmel Straight
    track.left(5)
    track.forward(250)

    # Les Combes
    track.right(50)
    track.forward(50)
    track.circle(25, 180)
    track.forward(50)

    # Malmedy to Rivage
    track.left(30)
    track.forward(70)
    track.circle(50, 90)

    # To Pouhon
    track.left(90)
    track.forward(100)

    # Pouhon
    track.circle(-100, 70)

    # To Fagnes
    track.forward(60)
    track.right(60)
    track.forward(40)

    # Campus to Stavelot
    track.right(20)
    track.forward(60)
    track.circle(45, 90)

    # Straight to Blanchimont
    track.left(70)
    track.forward(180)

    # Blanchimont
    track.left(20)
    track.forward(100)

    # Chicane and Finish Line
    track.right(10)
    track.circle(45, 90)
    track.forward(40)
    track.circle(45, 90)
    track.forward(50)

    track.penup()

    # End drawing
    turtle.done()


draw_track()

#