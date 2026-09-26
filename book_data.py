#!/usr/bin/env python3
"""
Centralized book metadata, polished story text, original text, and illustration paths
for "The Giant Adventure" by Mishka Pant.
"""

BOOK_TITLE = "The Giant Adventure"
BOOK_SUBTITLE = "Written & Illustrated by Mishka Pant (Age 8)"
BOOK_AUTHOR = "Mishka Pant"

FRONT_COVER_ILLUSTRATION = "illustrations/cover_illustration.png"
FRONT_COVER_ORIGINAL = "photos/WhatsApp Image 2026-07-17 at 4.32.18 PM.jpeg"

BACK_COVER_ILLUSTRATION = "illustrations/back_cover_illustration.png"
BACK_COVER_ORIGINAL = "photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (8).jpeg"

ABOUT_THE_BOOK = (
    "What starts as a holiday flight to Singapore turns into the adventure of a lifetime! "
    "Join eight-year-old Mishka and her best friends, Mira and Billy, as they journey across "
    "magical islands and beyond. From outsmarting bears on Greenland Island and riding camels "
    "past volcanoes, to tumbling through a space portal, visiting a candy house, sneaking past "
    "dragons at the Centre of the Earth, and befriending a lonely multi-colored unicorn on "
    "Planet Earth 2—this imaginative tale celebrates friendship, curiosity, and the boundless "
    "magic of childhood."
)

STORY_PAGES = [
    {
        "page_number": 1,
        "title": "Page 1: Flight to Singapore",
        "polished_text": (
            "My friends Mira, Billy, and I always go somewhere for the holidays. "
            "This time, we were flying to Singapore, but our plane crashed into the water! "
            "Everyone else made it to shore except for us. We were stuck, so we swam to a "
            "nearby island. I gathered some coconuts, and Mira found some berries."
        ),
        "original_text": (
            "Me and My Friends Mira and billy always go somewhere in the holidays so this time "
            "we went to Singapore but the plane crashed in water everyone went on land excepte us "
            "we were stuck so we swam to an island I got some coconuts and Mira got some berries."
        ),
        "illustration_file": "illustrations/page1_plane_crash.png",
        "original_photos": [
            "photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (1).jpeg",
            "photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (2).jpeg"
        ]
    },
    {
        "page_number": 2,
        "title": "Page 2: Greenland Island",
        "polished_text": (
            "Next, we went to Greenland Island. Over there, we spotted a bear! "
            "We knew that bears do not eat dead people, so we all lay down on the grass "
            "and pretended to be dead."
        ),
        "original_text": (
            "Next we went to greenland ilssand over there we saw a bear we knew that do not "
            "eat dead people so we act to be dead."
        ),
        "illustration_file": "illustrations/page2_greenland_bear.png",
        "original_photos": [
            "photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (3).jpeg"
        ]
    },
    {
        "page_number": 3,
        "title": "Page 3: Desert Island",
        "interactive_note": "✨ Interactive Lift-the-Flap Scene ✨",
        "polished_text": (
            "After that, we traveled to Desert Island. On the island, we found a friendly camel "
            "and rode on its back. Along the way, we even saw an erupting volcano!"
        ),
        "original_text": (
            "Next we went to desert island in the island we saw a camel so we rode on it "
            "we even saw a volcano."
        ),
        "illustration_file": "illustrations/page3_desert_island.png",
        "original_photos": [
            "photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (4).jpeg",
            "photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (5).jpeg"
        ]
    },
    {
        "page_number": 4,
        "title": "Page 4: The Space Hole",
        "polished_text": (
            "Then we discovered a mysterious hole. When we jumped inside, we found ourselves "
            "floating in outer space! We explored wonderful new planets and then headed back to Earth."
        ),
        "original_text": (
            "Then we found a hole so we went in it and we were in space! "
            "We explored new things then went back to earth."
        ),
        "illustration_file": "illustrations/page4_space_hole.png",
        "original_photos": [
            "photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (6).jpeg"
        ]
    },
    {
        "page_number": 5,
        "title": "Page 5: Flower Island",
        "interactive_note": "✨ Interactive Pull-Tab Scene ✨",
        "polished_text": (
            "Soon, we found ourselves on Flower Island, where beautiful flowers bloomed everywhere. "
            "We slept there peacefully for one night."
        ),
        "original_text": (
            "And we found ourselves on flower island we slept there for one night."
        ),
        "illustration_file": "illustrations/page5_flower_island.png",
        "original_photos": [
            "photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (7).jpeg",
            "photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (8).jpeg"
        ]
    },
    {
        "page_number": 6,
        "title": "Page 6: Chocolate Island",
        "polished_text": (
            "Next, we swam to Chocolate Island and saw a house made of candy! "
            "Inside lived a Chocolate Man and a Caramel Woman. They gave us delicious sweets "
            "and told us all about Treasure Island."
        ),
        "original_text": (
            "Then we swam to chocolate island over there we saw a candy house in the candy house "
            "we saw a chocolate man and a caramel women they gave us candy and they told us about "
            "treasure island."
        ),
        "illustration_file": "illustrations/page6_chocolate_island.png",
        "original_photos": [
            "photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (9).jpeg"
        ]
    },
    {
        "page_number": 7,
        "title": "Page 7: Treasure Island & The Map",
        "interactive_note": "✨ Interactive Envelope & Map Scene ✨",
        "polished_text": (
            "In the morning, we set off for Treasure Island. There, we discovered a chest of "
            "gold coins and a secret map! We followed the trail on the map, and..."
        ),
        "original_text": (
            "In the morning we went to treasure island over there we found some gold coins and "
            "a map we followed were the map told us to go and......."
        ),
        "illustration_file": "illustrations/page7_treasure_island.png",
        "original_photos": [
            "photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (10).jpeg",
            "photos/WhatsApp Image 2026-07-17 at 4.32.19 PM.jpeg"
        ]
    },
    {
        "page_number": 8,
        "title": "Page 8: Centre of the Earth",
        "polished_text": (
            "...we reached the Centre of the Earth! Over there, we saw cave people, Vikings, "
            "pirates, dinosaurs, and even fire-breathing dragons! We quickly hid behind some "
            "bushes and tiptoed away."
        ),
        "original_text": (
            "We reached to the centre of the earth over there we saw cave people, vikings, "
            "pirates, dinosauses and even dragons so we quikly hid behind some bushes and "
            "then walked away."
        ),
        "illustration_file": "illustrations/page8_centre_earth.png",
        "original_photos": [
            "photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (1).jpeg"
        ]
    },
    {
        "page_number": 9,
        "title": "Page 9: The Cloud Castle",
        "polished_text": (
            "And then... we found a magical Cloud Castle! After doing all kinds of fun things "
            "inside, we discovered a special rose that showed us the way to the Magical World."
        ),
        "original_text": (
            "And then...... we found a cloud castle in there we did all kinds off things and "
            "then we found a rose and on that rose it showed how to go to magical world."
        ),
        "illustration_file": "illustrations/page9_cloud_castle.png",
        "original_photos": [
            "photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (2).jpeg"
        ]
    },
    {
        "page_number": 10,
        "title": "Page 10: The Magical World",
        "polished_text": (
            "We followed the directions on the rose until we reached the Magical World. "
            "There, we played with gnomes, hunted for emeralds with dwarfs, chitchatted with "
            "elves, practiced magic with fairies, and even cackled with witches!"
        ),
        "original_text": (
            "We followed the way how to go there and we reached over there we played with gnomes, "
            "found emeralds with dwarfs, chit chated with elves, did magic with faries and even "
            "cackeled with witches"
        ),
        "illustration_file": "illustrations/page10_magical_world.png",
        "original_photos": [
            "photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (3).jpeg"
        ]
    },
    {
        "page_number": 11,
        "title": "Page 11: Flight Home to Bangalore",
        "polished_text": (
            "And guess what? After all that excitement, we had a peaceful nap on the IndiGo plane "
            "and arrived safely back in Bangalore."
        ),
        "original_text": (
            "And guss what after that we had a peaceful nap on the plane and then we reached banglore."
        ),
        "illustration_file": "illustrations/page11_indigo_plane.png",
        "original_photos": [
            "photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (4).jpeg"
        ]
    },
    {
        "page_number": 12,
        "title": "Page 12: Planet Earth 2 & The Mysterious Unicorn",
        "polished_text": (
            "The next day, we went to school—but instead of studying, we traveled to Planet Earth 2! "
            "Everything there was unique and different: the schools, shops, clothes, homes, language, "
            "and traditions. The most extraordinary sight of all was the Mysterious Unicorn, brilliantly "
            "colored in blue, green, and yellow! The saddest thing, however, was that it had no friends. "
            "When we said, 'You can be our friend!', we suddenly understood its language! From then on, "
            "we often visited its home, and sometimes it even came to visit ours."
        ),
        "original_text": (
            "The next day we had to go to school and we didn't study in school we went to planet earth 2 "
            "over there was a meige and diffent school, shops, clothes, studys, homes, culture, language "
            "and tradition but the most meige and diffent thing of all was the mysteriouse unicorn it had "
            "a totaly new style, clothes, home, culture, tradition, language and colour! it was blue, green "
            "and yellow together! but the most sad thing of all was it had No friends so when we sad that "
            "you could be our friend we understud its language so we used to come to its home and sometimes "
            "it even came to ours."
        ),
        "illustration_file": "illustrations/page12_mysterious_unicorn.png",
        "original_photos": [
            "photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (5).jpeg",
            "photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (6).jpeg"
        ]
    },
    {
        "page_number": 13,
        "title": "Page 13: Where to Next?",
        "polished_text": (
            "That night, back in our own homes, each of us held onto our favorite souvenirs—the "
            "Treasure Island map, the Chocolate Island candy, and the Cloud Castle rose—and wondered: "
            "Where will we go next? Canada or the USA?"
        ),
        "original_text": (
            "That night when we came home all of us wondered in there own house were will we go "
            "next canada or USA."
        ),
        "illustration_file": "illustrations/page13_souvenirs_next.png",
        "original_photos": [
            "photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (7).jpeg"
        ]
    }
]
