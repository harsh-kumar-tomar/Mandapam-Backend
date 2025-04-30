import sqlite3

conn = sqlite3.connect('hotels.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table_name in tables:
    table = table_name[0]
    print(f"\n=== {table} ===")
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
        print()

conn.close()

# import sqlite3

# # Example descriptions list (one per hotel)
# desc_list = [
#     "Experience ultimate relaxation with our oceanfront resort offering private balconies, panoramic sea views, and world-class dining. Enjoy morning beach yoga, sunset cruises, and rejuvenating spa treatments. Our attentive concierge will help arrange island tours, water sports, and cultural experiences. Perfect for couples, families, and solo travelers seeking a coastal paradise getaway.",
#     "Nestled in lush green hills, this serene retreat offers luxurious cabins with fireplaces, hiking trails, and nature-inspired wellness therapies. Guests can enjoy guided birdwatching, mountain biking, and farm-to-table dining from locally sourced ingredients. Evening bonfires and stargazing sessions create unforgettable memories. Ideal for nature lovers and outdoor enthusiasts alike.",
#     "Located in the heart of a vibrant city, this hotel boasts modern suites with skyline views, a rooftop infinity pool, and gourmet restaurants. Guests can access cultural landmarks, bustling markets, and entertainment hubs within minutes. The spa, fitness center, and rooftop bar provide perfect relaxation after a busy day exploring.",
#     "Step back in time at this historic mansion featuring antique furnishings, opulent chandeliers, and elegant courtyards. Enjoy afternoon teas, classical music evenings, and curated heritage tours. The on-site fine dining restaurant offers exquisite regional delicacies. Perfect for travelers seeking timeless charm, sophisticated ambiance, and a touch of aristocratic grandeur.",
#     "This beachfront haven offers direct access to white sand beaches, overwater villas, and vibrant coral reefs for snorkeling. Indulge in fresh seafood grills, relax in ocean-view spas, and embark on sailing or kayaking adventures. Sunset dinners and live music create a perfect romantic escape for couples and honeymooners.",
#     "Our alpine resort offers panoramic mountain views, ski-in ski-out access, and cozy lodges with fireplaces. Guests can enjoy spa therapies, gourmet alpine cuisine, and après-ski cocktails. Summer visitors can explore hiking trails, mountain biking, and paragliding. A year-round destination for adventure seekers and relaxation lovers in equal measure.",
#     "Surrounded by tranquil lakes and blooming gardens, this countryside inn offers charming rooms with vintage decor. Wake to birdsong and enjoy hearty home-cooked breakfasts. Canoe along serene waters, explore nearby vineyards, or relax with a book on garden patios. Evenings end with bonfires and locally sourced farm-to-table dinners.",
#     "Escape to this tropical paradise featuring spacious villas with private plunge pools, open-air showers, and lush garden views. Guests can indulge in holistic spa treatments, beachfront yoga, and gourmet dining under the stars. Kayaking, paddleboarding, and guided reef dives offer adventure, while serene hammocks invite peaceful afternoon naps.",
#     "This sophisticated urban hotel features stylish suites, rooftop lounges, and a vibrant art gallery. Enjoy artisan coffee at the café, international cuisine at the restaurant, and panoramic city views from the terrace. Perfectly located near museums, theaters, and shopping districts, it’s ideal for both business and leisure travelers.",
#     "An island resort offering secluded beachfront cottages, private boat tours, and crystal-clear lagoons for snorkeling and diving. Enjoy candlelit seafood dinners, sunrise yoga, and spa therapies with ocean breezes. Island hopping excursions, dolphin watching, and beach volleyball ensure every day is filled with both relaxation and adventure.",
#     "Our luxurious spa resort offers mineral-rich hot springs, aromatherapy massages, and serene meditation gardens. Guests can join wellness workshops, healthy cooking classes, and guided forest walks. The vegetarian fine-dining restaurant serves organic, farm-fresh meals. Ideal for rejuvenation retreats, solo travelers, and couples seeking tranquility and self-care experiences.",
#     "A vibrant boutique hotel featuring colorful murals, eclectic furnishings, and live music evenings. Guests can enjoy rooftop tapas bars, fusion cuisine restaurants, and guided street art tours. Located near artisan markets and historic landmarks, it offers an energetic base for culture seekers and creative travelers exploring the city.",
#     "Our family-friendly resort features spacious villas, a water park with slides, and kids’ adventure clubs. Parents can relax at the beachfront spa, play golf, or enjoy gourmet restaurants. Evening entertainment includes cultural shows, movie nights, and live music. Perfect for multigenerational families seeking fun and relaxation together.",
#     "This elegant riverside retreat offers colonial-era architecture, lush gardens, and tranquil courtyards. Guests can take boat cruises, explore nearby temples, and dine at the riverside restaurant offering regional specialties. The luxurious spa and peaceful library create an ideal escape for those seeking culture, history, and quiet reflection.",
#     "Stay in stylish suites with floor-to-ceiling windows, enjoy rooftop infinity pools, and dine on gourmet international cuisine. The state-of-the-art fitness center, business lounges, and spa make it ideal for modern travelers. Located steps from shopping malls, theaters, and nightlife, it blends convenience, comfort, and cosmopolitan elegance.",
#     "Immerse yourself in rustic charm at our forest cabins featuring wood-burning stoves, cozy nooks, and panoramic woodland views. Guests can hike scenic trails, try fishing, or join nature photography workshops. Evenings bring campfire storytelling and stargazing. A perfect retreat for unplugging and reconnecting with nature’s beauty and calm.",
#     "This luxury desert resort offers opulent tents with plush interiors, camel safaris at sunrise, and traditional cultural performances under the stars. Guests can savor regional delicacies, enjoy spa treatments using indigenous herbs, and explore ancient forts nearby. A unique blend of adventure, history, and royal hospitality awaits.",
#     "Our chic beachside property features sun-drenched terraces, beachfront bars, and watersport centers. Guests can windsurf, jet ski, or relax with seaside massages. Evenings offer live DJ sessions and seafood feasts by the waves. Ideal for young travelers and couples seeking a lively, stylish coastal escape.",
#     "An exclusive mountaintop resort offering private chalets, gourmet alpine dining, and guided glacier tours. Guests can relax in thermal pools, ski pristine slopes, and enjoy fireside wine tastings. Summer brings hiking, rock climbing, and paragliding. A luxurious year-round destination for thrill-seekers and mountain lovers alike.",
#     "Our elegant coastal retreat offers cliffside dining, panoramic ocean terraces, and whale-watching excursions. Explore scenic bike paths, relax in ocean-view spas, and savor fine wines from nearby vineyards. Perfect for romantic getaways and gourmet travelers seeking breathtaking vistas and unforgettable culinary experiences by the sea.",
#     "Located beside a tranquil lake, this serene lodge offers paddleboarding, fishing trips, and lakeside picnics. Guests can enjoy outdoor yoga, artisan workshops, and gourmet lakeside dinners. Cozy cabins with lake views and crackling fireplaces create a warm, intimate atmosphere ideal for reflection and rejuvenation.",
#     "A grand hotel with opulent marble lobbies, crystal chandeliers, and luxurious suites. Guests can indulge in fine dining, private butler service, and afternoon teas. The spa offers rejuvenating treatments, and the ballroom hosts elegant soirées. A destination for travelers seeking classic sophistication and timeless luxury.",
#     "This rainforest eco-resort offers treehouse accommodations, guided jungle treks, and canopy zip-line tours. Guests can visit nearby waterfalls, join wildlife safaris, and participate in conservation workshops. Organic dining and spa treatments using local botanicals enhance the experience. Perfect for eco-conscious travelers and adventure seekers alike.",
#     "Our contemporary art hotel showcases rotating exhibitions, artist residencies, and interactive workshops. Enjoy modern suites, rooftop cocktail bars, and fusion cuisine restaurants. Located in the creative heart of the city, it’s ideal for art lovers, digital nomads, and travelers seeking cultural immersion and inspiration.",
#     "Experience vineyard luxury with vineyard tours, wine tastings, and gourmet farm-to-table dining. Guests can stay in elegant vineyard-view suites, relax in the spa, and participate in cooking classes. Perfect for romantic weekends, foodies, and wine enthusiasts seeking indulgence amid rolling countryside landscapes.",
#     "This luxury yacht hotel offers floating suites, private sunset cruises, and deep-sea fishing excursions. Enjoy gourmet seafood dining on deck, stargazing from your balcony, and water sports at secluded coves. An exclusive escape for ocean lovers seeking privacy, elegance, and unparalleled maritime experiences.",
#     "Our heritage fort hotel features sandstone courtyards, intricately carved balconies, and historical suites. Guests can explore ancient ramparts, attend folk music evenings, and dine on royal Rajasthani cuisine. Ideal for history buffs, cultural enthusiasts, and travelers seeking a regal experience within centuries-old walls.",
#     "A secluded rainforest retreat offering waterfall-fed pools, bamboo massage huts, and jungle trekking paths. Guests can participate in yoga sessions, organic cooking classes, and nighttime firefly tours. Designed for deep relaxation, wellness, and eco-adventures, it’s perfect for those reconnecting with nature and themselves.",
#     "This alpine lodge features hand-crafted log cabins, hot cocoa lounges, and scenic gondola rides. Guests can ski, snowboard, and relax in mountain-view hot tubs. Summer brings wildflower hikes, mountain biking, and alpine festivals. A cozy, year-round haven for outdoor enthusiasts and mountain lovers.",
#     "Stay at a lakeside château offering boating, horseback riding, and evening jazz concerts. Guests can savor fine wines, gourmet regional cuisine, and relax in luxurious spa suites. The sprawling gardens, grand library, and elegant ballroom evoke timeless European elegance perfect for romantic getaways.",
#     "This island wellness resort features beachfront yoga decks, ayurvedic spas, and organic cafés. Guests can snorkel coral reefs, join meditation retreats, and take sunset paddleboarding excursions. Designed for deep relaxation and self-care, it blends tropical beauty with holistic healing and gourmet healthy cuisine.",
#     "A desert oasis offering palm-shaded pools, camel treks, and stargazing nights. Guests can experience Bedouin-style tents, traditional feasts, and hammam spa rituals. The boutique shops, art galleries, and sunset dunes provide adventure and tranquility for travelers seeking cultural immersion and natural wonder.",
#     "Our elegant ski resort offers chalet-style suites, gourmet fondue dinners, and world-class ski slopes. After skiing, guests can relax in mountain-view saunas, sip mulled wine by fireplaces, and enjoy live alpine music. A charming winter wonderland perfect for both thrill-seekers and cozy relaxation lovers.",
#     "This exclusive island retreat offers beachfront villas, private yacht tours, and sunset beach picnics. Guests can snorkel pristine reefs, dine on gourmet cuisine, and relax in oceanfront spas. Secluded and luxurious, it’s perfect for honeymoons, anniversaries, and those seeking ultimate privacy and elegance."
# ]


# # Open connection
# conn = sqlite3.connect('hotels.db')
# cursor = conn.cursor()

# # Fetch all hotel IDs in order
# cursor.execute("SELECT id FROM hotels")
# hotel_ids = [row[0] for row in cursor.fetchall()]

# # Safety check: make sure desc_list has enough descriptions
# if len(desc_list) < len(hotel_ids):
#     raise ValueError("Not enough descriptions for all hotels")

# # Now update description per hotel
# for idx, hotel_id in enumerate(hotel_ids):
#     new_description = desc_list[idx]
#     cursor.execute(
#         "UPDATE hotels SET description = ? WHERE id = ?",
#         (new_description, hotel_id)
#     )
#     print(f"Updated hotel ID {hotel_id} → description: {new_description}")

# # Commit + close
# conn.commit()
# conn.close()
