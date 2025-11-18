import pygame
import math
from datetime import datetime

# -----------------------------
# CONFIG (OLD VINTAGE STYLE)
# -----------------------------
WIDTH, HEIGHT = 600, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
CLOCK_RADIUS = 250

# Vintage colors
BG_COLOR = (45, 30, 20)            # dark brown background
CLOCK_FACE_COLOR = (235, 220, 190) # parchment
BORDER_COLOR = (90, 60, 35)        # wooden border
INNER_RING_COLOR = (160, 120, 80)
TICK_COLOR = (80, 50, 30)

HOUR_HAND_COLOR = (60, 40, 25)
MINUTE_HAND_COLOR = (70, 45, 25)
SECOND_HAND_COLOR = (140, 40, 30)

CENTER_DOT_OUTER = (70, 40, 30)
CENTER_DOT_INNER = (230, 220, 200)

FPS = 60


# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def polar_to_cartesian(center, radius, angle_deg):
    """
    Convert polar coordinates (radius, angle) to cartesian (x, y),
    where angle_deg is in degrees and 0° is at 3 o'clock,
    but we rotate so 0° is at 12 o'clock (top).
    """
    angle_rad = math.radians(angle_deg)
    x = center[0] + radius * math.cos(angle_rad)
    y = center[1] + radius * math.sin(angle_rad)
    return int(x), int(y)


def draw_clock_face(screen, font):
    """Draw the old-style clock face with Roman numerals."""
    # Outer wooden-ish ring
    pygame.draw.circle(screen, BORDER_COLOR, CENTER, CLOCK_RADIUS + 15)

    # Main parchment circle
    pygame.draw.circle(screen, CLOCK_FACE_COLOR, CENTER, CLOCK_RADIUS)

    # Inner ring to give depth
    pygame.draw.circle(screen, INNER_RING_COLOR, CENTER, CLOCK_RADIUS - 20, 3)

    # Minute & hour tick marks
    for i in range(60):
        angle = i * 6 - 90  # each minute step is 6°, starting from top
        if i % 5 == 0:
            # Hour tick (thicker, longer)
            inner = CLOCK_RADIUS - 35
            outer = CLOCK_RADIUS - 10
            thickness = 4
        else:
            # Minute tick (thin)
            inner = CLOCK_RADIUS - 25
            outer = CLOCK_RADIUS - 10
            thickness = 2

        start_pos = polar_to_cartesian(CENTER, inner, angle)
        end_pos = polar_to_cartesian(CENTER, outer, angle)
        pygame.draw.line(screen, TICK_COLOR, start_pos, end_pos, thickness)

    # Roman numerals for hours
    roman = {
        1: "I",   2: "II",  3: "III",
        4: "IV",  5: "V",   6: "VI",
        7: "VII", 8: "VIII",9: "IX",
        10: "X",  11: "XI", 12: "XII"
    }

    for hour in range(1, 13):
        angle = hour * 30 - 90  # 30° per hour
        text_radius = CLOCK_RADIUS - 65
        text_pos = polar_to_cartesian(CENTER, text_radius, angle)

        label = font.render(roman[hour], True, (50, 30, 20))
        label_rect = label.get_rect(center=text_pos)
        screen.blit(label, label_rect)


def draw_hands(screen, now):
    """Draw hour, minute, and second hands in an old-style look."""
    hour = now.hour % 12
    minute = now.minute
    second = now.second
    microsecond = now.microsecond

    sec_fraction = second + microsecond / 1_000_000.0

    # Angles
    second_angle = sec_fraction * 6 - 90
    minute_angle = (minute + sec_fraction / 60) * 6 - 90
    hour_angle = (hour + minute / 60 + sec_fraction / 3600) * 30 - 90

    # Hour hand (shorter, thick)
    hour_length = CLOCK_RADIUS - 120
    hour_end = polar_to_cartesian(CENTER, hour_length, hour_angle)
    pygame.draw.line(screen, HOUR_HAND_COLOR, CENTER, hour_end, 10)

    # Minute hand (longer)
    minute_length = CLOCK_RADIUS - 80
    minute_end = polar_to_cartesian(CENTER, minute_length, minute_angle)
    pygame.draw.line(screen, MINUTE_HAND_COLOR, CENTER, minute_end, 8)

    # Second hand (thin, red-ish)
    second_length = CLOCK_RADIUS - 60
    second_end = polar_to_cartesian(CENTER, second_length, second_angle)
    pygame.draw.line(screen, SECOND_HAND_COLOR, CENTER, second_end, 3)

    # Small back counterweight for second hand
    back_length = 35
    back_end = polar_to_cartesian(CENTER, back_length, second_angle + 180)
    pygame.draw.line(screen, SECOND_HAND_COLOR, CENTER, back_end, 3)

    # Center cap
    pygame.draw.circle(screen, CENTER_DOT_OUTER, CENTER, 12)
    pygame.draw.circle(screen, CENTER_DOT_INNER, CENTER, 7)


def draw_date(screen, font_small, now):
    """
    Date & time just below the clock hands (below the center point),
    both centered horizontally.
    """
    date_str = now.strftime("%d %B %Y")
    time_str = now.strftime("%I:%M:%S %p")

    # Render text
    date_label = font_small.render(date_str, True, (110, 75, 45))
    time_label = font_small.render(time_str, True, (110, 75, 45))

    # Position: a bit below the center, but well inside the dial
    date_y = CENTER[1] + 35
    time_y = CENTER[1] + 60

    date_rect = date_label.get_rect(center=(CENTER[0], date_y))
    time_rect = time_label.get_rect(center=(CENTER[0], time_y))

    screen.blit(date_label, date_rect)
    screen.blit(time_label, time_rect)


# -----------------------------
# MAIN
# -----------------------------
def main():
    pygame.init()
    pygame.display.set_caption("Vintage Analog Clock")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Fonts: old-style serif
    number_font = pygame.font.SysFont("timesnewroman", 44, bold=True)
    small_font = pygame.font.SysFont("timesnewroman", 20, bold=False)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        now = datetime.now()

        # Background (plain dark brown)
        screen.fill(BG_COLOR)

        # Draw components
        draw_clock_face(screen, number_font)
        draw_hands(screen, now)
        draw_date(screen, small_font, now)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
