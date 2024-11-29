import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brainwave Blitz")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHEEL_COLOR = (50, 50, 50)
BUTTON_COLOR = (0, 150, 0)
BUTTON_HOVER_COLOR = (0, 200, 0)
TRACK_COLOR = (150, 150, 150)  # Gray for track
FINISH_LINE_COLOR = (255, 215, 0)  # Yellow for finish line
BORDER_COLOR = (100, 100, 100)  # Gray for border

# Fonts
font = pygame.font.SysFont("Impact", 24)
title_font = pygame.font.SysFont("Impact", 48)

# Difficulty settings
difficulty_settings = {
    "Easy": 50,
    "Medium": 25,
    "Hard": 10,
}

# Car Class
class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 30
        self.color = RED  # Default color
        self.speed = 5000000000

    def move(self, speed):
        self.x += speed

    def draw(self, screen):
        # Draw the car body
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        # Draw wheels (simple circles)
        wheel_radius = 7
        wheel_offset = 10  # Offset for wheels from the car's sides

        # Draw two wheels
        pygame.draw.circle(screen, WHEEL_COLOR, (self.x + wheel_offset, self.y + self.height), wheel_radius)
        pygame.draw.circle(screen, WHEEL_COLOR, (self.x + self.width - wheel_offset, self.y + self.height), wheel_radius)

# Flashcards for various subjects
flashcards = {
    "Math": [
        ("15 + 27 + 35", "77"),
        ("45 - 12 + 23", "56"),
        ("12 * 3 - 15", "21"),
        ("36 / 6 + 9", "15"),
        ("5 * 8 + 12", "52"),
        ("81 - 45 + 18", "54"),
        ("9 + 16 * 3", "57"),
        ("14 * 2 - 9", "19"),
        ("100 - 25 / 5", "95"),
        ("33 + 44 - 22", "55"),
        ("10 * 7 + 8", "78"),
        ("96 / 12 + 15", "23"),
        ("5 + 10 * 3", "35"),
        ("60 / 5 + 40", "52"),
        ("20 * 2 - 15", "25"),
        ("100 - 45 + 30", "85"),
        ("11 * 4 - 13", "31"),
        ("25 + 50 - 30", "45"),
        ("18 + 12 * 3", "54"),
        ("144 / 12 + 25", "37")
    ],
    "Geography": [
        ("What is the longest river in the world?", "Nile"),
        ("Which continent has the most countries?", "Africa"),
        ("What is the capital of Australia?", "Canberra"),
        ("Which desert is the largest in the world?", "Sahara"),
        ("What is the smallest country in the world?", "Vatican City"),
        ("Which U.S. state has the most coastline?", "Alaska"),
        ("Which mountain range is the longest in the world?", "Andes"),
        ("What is the capital of South Korea?", "Seoul"),
        ("Which ocean is the largest by area?", "Pacific"),
        ("What is the largest country in South America?", "Brazil"),
        ("Which European country is known as the 'Land of a Thousand Lakes'?", "Finland"),
        ("What is the capital of Argentina?", "Buenos Aires"),
        ("Which country has the most islands?", "Sweden"),
        ("What is the tallest mountain in Europe?", "Mount Elbrus"),
        ("Which country is home to the Great Barrier Reef?", "Australia"),
        ("What is the capital of Canada?", "Ottawa"),
        ("Which African country is completely surrounded by South Africa?", "Lesotho"),
        ("Which is the only country with a flag that is not rectangular?", "Nepal"),
        ("What is the largest desert in Asia?", "Gobi"),
        ("What is the capital of Portugal?", "Lisbon")
    ],
    "Science": [
        ("What is the chemical symbol for gold?", "Au"),
        ("Which planet is the hottest in our solar system?", "Venus"),
        ("What part of the cell produces energy?", "Mitochondria"),
        ("What is the most abundant gas in Earth's atmosphere?", "Nitrogen"),
        ("Who proposed the theory of relativity?", "Albert Einstein"),
        ("What element does the chemical symbol 'K' represent?", "Potassium"),
        ("What is the process by which plants make their own food?", "Photosynthesis"),
        ("Which organ in the human body is responsible for detoxification?", "Liver"),
        ("What is the hardest natural substance on Earth?", "Diamond"),
        ("What is the chemical formula for water?", "H2O"),
        ("Which blood cells help fight infections?", "White blood cells"),
        ("What is the nearest star to Earth?", "Sun"),
        ("What is the smallest unit of life?", "Cell"),
        ("What is the SI unit of force?", "Newton"),
        ("Which planet has the largest number of moons?", "Saturn"),
        ("What is the boiling point of water in Celsius?", "100"),
        ("What type of energy is stored in a stretched rubber band?", "Elastic potential energy"),
        ("What is the study of fungi called?", "Mycology"),
        ("Which layer of Earth's atmosphere contains the ozone layer?", "Stratosphere"),
        ("What is the chemical symbol for sodium?", "Na")
    ]
}

# Start Screen: Main menu with "Play" button
def start_screen():
    running = True
    while running:
        screen.fill(WHITE)
        # Display title
        title_text = title_font.render("Brainwave Blitz", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(title_text, title_rect)
        # Draw Play button
        play_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
        pygame.draw.rect(screen, BUTTON_COLOR, play_button)
        # Button text
        play_text = font.render("Play", True, WHITE)
        play_text_rect = play_text.get_rect(center=play_button.center)
        screen.blit(play_text, play_text_rect)
        # Handle mouse hover
        mouse_pos = pygame.mouse.get_pos()
        if play_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, play_button)
            screen.blit(play_text, play_text_rect)
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return True  # Return True when Play button is clicked
        pygame.display.update()  # Update screen

# Difficulty Selection Screen
def difficulty_screen():
    running = True
    while running:
        screen.fill(WHITE)
        # Display title
        title_text = title_font.render("Select Difficulty", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(title_text, title_rect)
        # Draw Easy, Medium, Hard buttons
        easy_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
        medium_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 60, 200, 50)
        hard_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 120, 200, 50)
        pygame.draw.rect(screen, BUTTON_COLOR, easy_button)
        pygame.draw.rect(screen, BUTTON_COLOR, medium_button)
        pygame.draw.rect(screen, BUTTON_COLOR, hard_button)
        # Button texts
        easy_text = font.render("Easy", True, WHITE)
        medium_text = font.render("Medium", True, WHITE)
        hard_text = font.render("Hard", True, WHITE)
        easy_text_rect = easy_text.get_rect(center=easy_button.center)
        medium_text_rect = medium_text.get_rect(center=medium_button.center)
        hard_text_rect = hard_text.get_rect(center=hard_button.center)
        screen.blit(easy_text, easy_text_rect)
        screen.blit(medium_text, medium_text_rect)
        screen.blit(hard_text, hard_text_rect)
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    return "Easy"
                elif medium_button.collidepoint(event.pos):
                    return "Medium"
                elif hard_button.collidepoint(event.pos):
                    return "Hard"
        pygame.display.update()  # Update screen

# Question Type Selection Screen
def question_type_screen():
    running = True
    while running:
        screen.fill(WHITE)
        # Display title
        title_text = title_font.render("Select Question Type", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(title_text, title_rect)
        # Draw Math, Geography, Science buttons
        math_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
        geography_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 60, 200, 50)
        science_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 120, 200, 50)
        pygame.draw.rect(screen, BUTTON_COLOR, math_button)
        pygame.draw.rect(screen, BUTTON_COLOR, geography_button)
        pygame.draw.rect(screen, BUTTON_COLOR, science_button)
        # Button texts
        math_text = font.render("Math", True, WHITE)
        geography_text = font.render("Geography", True, WHITE)
        science_text = font.render("Science", True, WHITE)
        math_text_rect = math_text.get_rect(center=math_button.center)
        geography_text_rect = geography_text.get_rect(center=geography_button.center)
        science_text_rect = science_text.get_rect(center=science_button.center)
        screen.blit(math_text, math_text_rect)
        screen.blit(geography_text, geography_text_rect)
        screen.blit(science_text, science_text_rect)
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if math_button.collidepoint(event.pos):
                    return "Math"
                elif geography_button.collidepoint(event.pos):
                    return "Geography"
                elif science_button.collidepoint(event.pos):
                    return "Science"
        pygame.display.update()  # Update screen

# Color Selection Screen (Embedded)
def color_selection_screen():
    running = True
    while running:
        screen.fill(WHITE)
        # Display title
        title_text = title_font.render("Choose Your Car Color", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(title_text, title_rect)

        # Draw color selection buttons
        red_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 50, 50)
        green_button = pygame.Rect(WIDTH // 2 - 25, HEIGHT // 2, 50, 50)
        blue_button = pygame.Rect(WIDTH // 2 + 50, HEIGHT // 2, 50, 50)
        pygame.draw.rect(screen, RED, red_button)
        pygame.draw.rect(screen, GREEN, green_button)
        pygame.draw.rect(screen, (0, 0, 255), blue_button)  # Blue color

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if red_button.collidepoint(event.pos):
                    return RED  # Return Red
                elif green_button.collidepoint(event.pos):
                    return GREEN  # Return Green
                elif blue_button.collidepoint(event.pos):
                    return (0, 0, 255)  # Return Blue

        pygame.display.update()

# End Screen: After win/loss, restart or quit
def end_screen(result):
    running = True
    while running:
        screen.fill(WHITE)
        # Display result
        result_text = title_font.render(result, True, BLACK)
        result_rect = result_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(result_text, result_rect)
        # Draw Restart and Quit buttons
        restart_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
        quit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 120, 200, 50)
        pygame.draw.rect(screen, BUTTON_COLOR, restart_button)
        pygame.draw.rect(screen, BUTTON_COLOR, quit_button)
        # Button texts
        restart_text = font.render("Restart", True, WHITE)
        quit_text = font.render("Quit", True, WHITE)
        restart_text_rect = restart_text.get_rect(center=restart_button.center)
        quit_text_rect = quit_text.get_rect(center=quit_button.center)
        screen.blit(restart_text, restart_text_rect)
        screen.blit(quit_text, quit_text_rect)
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    return "restart"
                elif quit_button.collidepoint(event.pos):
                    return "quit"
        pygame.display.update()  # Update screen

# Main Game Loop
def game(difficulty, question_type, car_color):
    # Set opponent car speed based on difficulty
    if difficulty == "Easy":
        opponent_car_speed = 0.20
    elif difficulty == "Medium":
        opponent_car_speed = 0.50
    elif difficulty == "Hard":
        opponent_car_speed = 1.5
    car = Car(50, HEIGHT // 2)
    car.color = car_color  # Set user car color
    opponent_car = Car(50, HEIGHT // 2 + 100)
    opponent_car.speed = opponent_car_speed  # Set opponent car speed
    # Select random question based on the question type
    question, answer = random.choice(flashcards[question_type])
    input_answer = ""
    clock = pygame.time.Clock()
    running = True
    correct_answers = 0
    while running:
        screen.fill(WHITE)
        # Draw race track
        track_width = 100
        user_track = pygame.Rect(0, HEIGHT // 2 - track_width // 2, WIDTH, track_width)
        opponent_track = pygame.Rect(0, HEIGHT // 2 + track_width // 2, WIDTH, track_width)
        pygame.draw.rect(screen, TRACK_COLOR, user_track)
        pygame.draw.rect(screen, TRACK_COLOR, opponent_track)

        # Draw border around the tracks
        pygame.draw.rect(screen, BORDER_COLOR, user_track, 3)  # 3 pixels thick border
        pygame.draw.rect(screen, BORDER_COLOR, opponent_track, 3)  # 3 pixels thick border

        # Draw white lines in the tracks
        line_width = 5
        line_spacing = 30
        for i in range(0, WIDTH, line_spacing * 2):
            pygame.draw.rect(screen, WHITE, (i, HEIGHT // 2 - track_width // 2 + track_width // 4, line_width, track_width // 2))  # User track line
            pygame.draw.rect(screen, WHITE, (i, HEIGHT // 2 + track_width // 2 + track_width // 4, line_width, track_width // 2))  # Opponent track line

        # Draw finish line
        finish_line_width = 10
        pygame.draw.rect(screen, FINISH_LINE_COLOR, (WIDTH - finish_line_width, HEIGHT // 2 - track_width // 2, finish_line_width, track_width))
        pygame.draw.rect(screen, FINISH_LINE_COLOR, (WIDTH - finish_line_width, HEIGHT // 2 + track_width // 2, finish_line_width, track_width))
        # Draw cars
        car.draw(screen)
        opponent_car.draw(screen)
        # Display the question
        question_text = font.render(f"Question: {question}", True, BLACK)
        screen.blit(question_text, (WIDTH // 2 - question_text.get_width() // 2, 50))
        # Display input answer
        input_text = font.render(f"Your Answer: {input_answer}", True, BLACK)
        screen.blit(input_text, (WIDTH // 2 - input_text.get_width() // 2, 100))
        # Display instructions
        instructions = font.render("Press Enter to submit your answer", True, BLACK)
        screen.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, 150))
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_answer.strip() == answer:
                        car.move(difficulty_settings[difficulty])  # Move car forward
                        correct_answers += 1
                    input_answer = ""  # Reset answer input
                    question, answer = random.choice(flashcards[question_type])  # Get new question
                elif event.key == pygame.K_BACKSPACE:
                    input_answer = input_answer[:-1]  # Remove last character
                else:
                    input_answer += event.unicode  # Add character to input
        # Move the opponent car
        opponent_car.move(opponent_car.speed)
        # Check if the computer car has won
        if opponent_car.x >= WIDTH - opponent_car.width:
            result = f"You Lost! Correct Answers: {correct_answers}"
            return end_screen(result)
        # Check if the player has won
        if car.x >= WIDTH - car.width:
            result = f"You Win! Correct Answers: {correct_answers}"
            return end_screen(result)
        pygame.display.update()  # Update screen
        clock.tick(30)  # Control frame rate

# Start the game from the start screen
if start_screen():
    difficulty = difficulty_screen()  # Get difficulty
    question_type = question_type_screen()  # Get question type
    # Embed the color selection screen into the code
    running = True
    while running:
        screen.fill(WHITE)
        # Display title
        title_text = title_font.render("Choose Your Car Color", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(title_text, title_rect)

        # Draw color selection buttons
        red_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 50, 50)
        green_button = pygame.Rect(WIDTH // 2 - 25, HEIGHT // 2, 50, 50)
        blue_button = pygame.Rect(WIDTH // 2 + 50, HEIGHT // 2, 50, 50)
        pygame.draw.rect(screen, RED, red_button)
        pygame.draw.rect(screen, GREEN, green_button)
        pygame.draw.rect(screen, (0, 0, 255), blue_button)  # Blue color

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if red_button.collidepoint(event.pos):
                    car_color = RED  # Return Red
                    running = False
                elif green_button.collidepoint(event.pos):
                    car_color = GREEN  # Return Green
                    running = False
                elif blue_button.collidepoint(event.pos):
                    car_color = (0, 0, 255)  # Return Blue
                    running = False

        pygame.display.update()
    while True:
        result = game(difficulty, question_type, car_color)  # Start the game
        if result == "restart":
            continue  # Restart the game if player chooses to restart
        else:
            break  # Exit the game if player chooses to quit
pygame.quit()