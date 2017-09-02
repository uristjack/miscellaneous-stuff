import random

def companyname():
    """Creates a random name for a company made up of four generic words."""
    
    companyfirst = ["New",                "Top",
                    "Great",              "Blue",
                    "Best",               "Gold",
                    "Grand",              "United",
                    "First",              "Ocean",
                    "Rich",               "Sino",
                    "Fortune",            "Green",
                    "East",               "Good",
                    "Well",               "Bright",
                    "Sky",                "Power",
                    "Super",              "Lucky",
                    "Prime",              "High",
                    "Red",                "Asian",
                    "Full",               "Win",
                    "Profit",             "South",
                    "Dragon"]

    companysecond = ["Business",          "Financial",
                     "Equities",          "Marketing",
                     "Property",          "Ventures",
                     "Resources",         "Industries",
                     "Asset",             "Real",
                     "Estates",           "Developments",
                     "Enterprise",        "Shipping",
                     "Engineering",       "Energy",
                     "Tech",              "Link",
                     "Success",           "Offshore",
                     "Media",             "View",
                     "Way",               "Land",
                     "Team",              "Marine"]      

    companythird = ["Consultant",         "Industry",
                    "Advisors",           "Venture",
                    "Logistics",          "Import",
                    "Far",                "Chemical",
                    "Machinery",          "Corporate",
                    "Gas",                "Private",
                    "Construction",       "Design",
                    "Family",             "Tower",
                    "Equipment",          "Equity",
                    "Mining",             "Investors",
                    "Oil",                "Sociedad",
                    "System",             "Club",
                    "Petroleum",          "Electronic"]

    companyfourth = ["Ltd.",              "S.A.",
                     "Inc.",              "Corp.",
                     "Foundation",        "Trust",
                     "GMBH",              "Company",
                     "Associates",        "Group",
                     "Fund",              "Partners"]
    
    word_a = (random.choice(companyfirst))  # Takes a random word from the 1st list
    word_b = (random.choice(companysecond)) # Takes a random word from the 2nd list
    word_c = (random.choice(companythird))  # Takes a random word from the 3rd list
    word_d = (random.choice(companyfourth)) # Takes a random word from the 4th list       
    return("%s %s %s %s" % (word_a, word_b, word_c, word_d))
