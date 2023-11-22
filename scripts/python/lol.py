string = """
@keyframes colorLoop {
    0% {
        border-color: rgb(255, 0, 0);
    }
    2% {
        border-color: rgb(255, 25, 0);
    }
    3% {
        border-color: rgb(255, 50, 0);
    }
    5% {
        border-color: rgb(255, 75, 0);
    }
    7% {
        border-color: rgb(255, 100, 0);
    }
    8% {
        border-color: rgb(255, 125, 0);
    }
    10% {
        border-color: rgb(255, 150, 0);
    }
    12% {
        border-color: rgb(255, 175, 0);
    }
    13% {
        border-color: rgb(255, 200, 0);
    }
    15% {
        border-color: rgb(255, 225, 0);
    }
    17% {
        border-color: rgb(255, 255, 0);
    }
    18% {
        border-color: rgb(225, 255, 0);
    }
    20% {
        border-color: rgb(200, 255, 0);
    }
    22% {
        border-color: rgb(175, 255, 0);
    }
    23% {
        border-color: rgb(150, 255, 0);
    }
    25% {
        border-color: rgb(125, 255, 0);
    }
    27% {
        border-color: rgb(100, 255, 0);
    }
    28% {
        border-color: rgb(75, 255, 0);
    }
    30% {
        border-color: rgb(50, 255, 0);
    }
    32% {
        border-color: rgb(25, 255, 0);
    }
    33% {
        border-color: rgb(0, 255, 0);
    }
    35% {
        border-color: rgb(0, 255, 25);
    }
    37% {
        border-color: rgb(0, 255, 50);
    }
    38% {
        border-color: rgb(0, 255, 75);
    }
    40% {
        border-color: rgb(0, 255, 100);
    }
    42% {
        border-color: rgb(0, 255, 125);
    }
    43% {
        border-color: rgb(0, 255, 150);
    }
    45% {
        border-color: rgb(0, 255, 175);
    }
    47% {
        border-color: rgb(0, 255, 200);
    }
    36.25% {
        border-color: rgb(0, 255, 225);
    }
    37.5% {
        border-color: rgb(0, 255, 255);
    }
    38.75% {
        border-color: rgb(0, 225, 255);
    }
    40% {
        border-color: rgb(0, 200, 255);
    }
    41.25% {
        border-color: rgb(0, 175, 255);
    }
    42.5% {
        border-color: rgb(0, 150, 255);
    }
    43.75% {
        border-color: rgb(0, 125, 255);
    }
    45% {
        border-color: rgb(0, 100, 255);
    }
    46.25% {
        border-color: rgb(0, 75, 255);
    }
    47.5% {
        border-color: rgb(0, 50, 255);
    }
    48.75% {
        border-color: rgb(0, 25, 255);
    }
    50% {
        border-color: rgb(0, 0, 255);
    }
    51.25% {
        border-color: rgb(25, 0, 255);
    }
    52.5% {
        border-color: rgb(50, 0, 255);
    }
    53.75% {
        border-color: rgb(75, 0, 255);
    }
    55% {
        border-color: rgb(100, 0, 255);
    }
    56.25% {
        border-color: rgb(125, 0, 255);
    }
    57.5% {
        border-color: rgb(150, 0, 255);
    }
    58.75% {
        border-color: rgb(175, 0, 255);
    }
    60% {
        border-color: rgb(200, 0, 255);
    }
    61.25% {
        border-color: rgb(225, 0, 255);
    }
    62.5% {
        border-color: rgb(255, 0, 255);
    }
    63.75% {
        border-color: rgb(255, 0, 225);
    }
    90% {
        border-color: rgb(255, 0, 200);
    }
    91.25% {
        border-color: rgb(255, 0, 175);
    }
    92.5% {
        border-color: rgb(255, 0, 150);
    }
    93.75% {
        border-color: rgb(255, 0, 125);
    }
    95% {
        border-color: rgb(255, 0, 100);
    }
    96.25% {
        border-color: rgb(255, 0, 75);
    }
    97.5% {
        border-color: rgb(255, 0, 50);
    }
    98.75% {
        border-color: rgb(255, 0, 25);
    }
    100% {
        border-color: rgb(255, 0, 0);
    }
}
"""

count = 0
for x in string:
    if x == "{":
        print(f"{count}. {x}")
        count += 1

perc = 0
lol = []
while perc < 100:
    print(f"|||{round(perc)}")
    perc += 1.6
    lol.append("x")

print(len(lol))
