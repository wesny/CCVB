import pymongo
from datetime import datetime
myTime = datetime.now()

#connection = pymongo.MongoClient ("ds029658.mongolab.com", 29658)
#db = connection ["heroku_app25983966"]
#db.authenticate("softdev", "softdev")
client = pymongo.MongoClient()
db = client.SSSD

Twitter = db.Twitter
Instagram = db.Instagram

def addUserTwitter (username,data,data3,data4):
    Twitter.insert({"username": username, "data":data, "part1":data3, "part2":data4, "date":myTime})

def getUserTwitter (username):
    myUser= Twitter.find_one({"username": username})
    print myUser
    dateSaved = myUser["date"]
    dif =  myTime - dateSaved
    difDays = dif.days
    if difDays > 7:
        Twitter.remove({"username":username})
        return -1
    else:
        data = myUser["data"]
        data3 = myUser["part1"]
        data4 = myUser["part2"]
        data2 = data3 + data4
        data ["tweet_text"] = data2
        return data

def addUserInstagram (username,data):
    Instagram.insert({"username": username, "data":data,"date":myTime})

def getUserInstagram (username):
    myUser= Instagram.find_one({"username": username})
    dateSaved = myUser["date"]
    dif =  myTime - dateSaved
    difDays = dif.days
    if difDays > 7:
        Instagram.remove({"username":username})
        return -1
    else:
        return myUser["data"]

if __name__ == '__main__':
    
    data = {
    "description":"19. Activist. Forthcoming book: The End of Creativity: How Schools Fail Children. 2013 Forbes 30 Under 30. Subscribe: http://t.co/Cl5RiOn7xH.",
        "eng_count":2,
        "eng_vals":[
            0,
            2,
            10,
            3,
            1,
            50,
            0,
            5,
            0,
            0,
            0,
            0,
            3,
            2,
            3,
            4,
            1,
            0,
            1,
            0,
            2,
            8,
            0,
            0,
            0,
            7,
            4,
            1,
            1,
            4,
            1,
            0,
            0,
            0,
            0,
            2,
            0,
            1,
            9,
            9,
            0,
            1,
            0,
            0,
            0,
            0,
            0,
            4,
            4,
            0,
            0,
            0,
            0,
            0,
            2,
            3,
            1,
            16,
            2,
            0,
            0,
            2,
            1,
            2,
            0,
            3,
            1,
            1,
            0,
            2,
            0,
            1,
            1,
            3,
            0,
            2,
            12,
            2,
            4,
            0,
            7,
            2,
            4,
            2,
            2,
            2,
            0,
            0,
            0,
            4,
            0,
            0,
            5,
            11,
            4,
            0,
            20,
            1,
            2,
            4,
            8,
            0,
            0,
            4,
            2,
            1,
            0,
            1,
            1,
            0,
            1,
            13,
            0,
            1,
            23,
            0,
            4,
            1,
            7,
            1,
            0,
            1,
            0,
            3,
            0,
            2,
            1,
            0,
            1,
            0,
            3,
            4,
            0,
            0,
            1,
            0,
            9,
            6,
            0,
            1,
            5,
            3,
            2,
            5,
            0,
            7,
            0,
            0,
            0,
            9,
            0,
            6,
            0,
            0,
            0,
            1,
            0,
            1,
            0,
            1,
            22
        ],
    "favorite_count":1,
        "favorite_vals":[
            0,
            2,
            5,
            0,
            1,
            18,
            0,
            3,
            0,
            0,
            0,
            0,
            1,
            0,
            2,
            3,
            1,
            0,
            0,
            0,
            1,
            6,
            0,
            0,
            0,
            6,
            1,
            0,
            0,
            2,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            0,
            2,
            0,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            2,
            0,
            0,
            0,
            0,
            0,
            2,
            3,
            1,
            5,
            2,
            0,
            0,
            0,
            1,
            2,
            0,
            2,
            1,
            0,
            0,
            1,
            0,
            1,
            1,
            1,
            0,
            1,
            8,
            0,
            2,
            0,
            1,
            0,
            4,
            2,
            2,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            4,
            2,
            3,
            0,
            12,
            1,
            1,
            3,
            4,
            0,
            0,
            3,
            0,
            1,
            0,
            1,
            1,
            0,
            1,
            6,
            0,
            1,
            10,
            0,
            0,
            1,
            2,
            1,
            0,
            1,
            0,
            3,
            0,
            2,
            1,
            0,
            1,
            0,
            1,
            2,
            0,
            0,
            0,
            0,
            3,
            6,
            0,
            1,
            5,
            1,
            0,
            2,
            0,
            3,
            0,
            0,
            0,
            7,
            0,
            2,
            0,
            0,
            0,
            1,
            0,
            1,
            0,
            1,
            19
        ],
    "followers_count":11905,
        "friends_count":2892,
        "listed_count":314,
        "location":"New York",
        "name":"Nikhil Goyal",
        "popularTweets":[
            "\"Cantor became the first majority leader to lose a primary in 115 years.\" http://t.co/Gk6OL6lR6r via @motherjones",
            "Trapped in our unjust system of mass incarceration are millions of brilliant people the world won't have the privilege to entertain.",
            "Charter schools are even more oppressive and restrictive than public schools, which seems almost impossible. http://t.co/eu3D2W1o9H",
            "When people say schools teach children \"discipline,\" they really mean conformity and obedience to authority.",
            "\"The true measure of a society's freedom is how it treats its dissidents and other marginalized groups, not how it treats good loyalists.\"",
            "Thomas Friedman, Maureen Dowd, and David Brooks should all get high together and then self destruct.",
            "\"Children do not need to be 'taught' in order to learn; they will learn a great deal, and probably learn best, without being taught.\"\n\u2014Holt",
            "I think it's fitting that my birthday falls on International Children's Day. Here's to another year of activism for children's rights.",
            "Officially reached the ripe old age of 19."
        ],
    "profilePicture":"http://pbs.twimg.com/profile_images/476560180226686976/BIxocu0m_normal.jpeg",
        "retweet_count":1,
        "retweet_vals":[
            0,
            0,
            5,
            3,
            0,
            32,
            0,
            2,
            0,
            0,
            0,
            0,
            2,
            2,
            1,
            1,
            0,
            0,
            1,
            0,
            1,
            2,
            0,
            0,
            0,
            1,
            3,
            1,
            1,
            2,
            0,
            0,
            0,
            0,
            0,
            2,
            0,
            0,
            9,
            7,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            4,
            2,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            11,
            0,
            0,
            0,
            2,
            0,
            0,
            0,
            1,
            0,
            1,
            0,
            1,
            0,
            0,
            0,
            2,
            0,
            1,
            4,
            2,
            2,
            0,
            6,
            2,
            0,
            0,
            0,
            2,
            0,
            0,
            0,
            4,
            0,
            0,
            1,
            9,
            1,
            0,
            8,
            0,
            1,
            1,
            4,
            0,
            0,
            1,
            2,
            0,
            0,
            0,
            0,
            0,
            0,
            7,
            0,
            0,
            13,
            0,
            4,
            0,
            5,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            2,
            2,
            0,
            0,
            1,
            0,
            6,
            0,
            0,
            0,
            0,
            2,
            2,
            3,
            0,
            4,
            0,
            0,
            0,
            2,
            0,
            4,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            3
        ],
    "statuses_count":29367,
        "text":"",
        "tweet_text":""
    }

    data2 = [
    "@WajahatAli also check out anand gopal's No Good Men Among the Living",
    ".@NaomiAKlein's Twitter bio is perfect: \"they say I'm polarizing.\"",
    "If the only thing teachers do is tell their students what and how to learn, how are they going to learn how to make their own decisions?",
    "Cory Doctorow novel pulled from school reading for 'questioning authority' http://t.co/TverICCGYO via @guardian",
    "Oh no. Just got a lot of #UniteBlue and Obama apologist followers.",
    "\"Cantor became the first majority leader to lose a primary in 115 years.\" http://t.co/Gk6OL6lR6r via @motherjones",
    "@shereenTshafi http://t.co/0MCCKNOXvd",
    "Edward Snowden's NSA leaks 'an important service', says Al Gore http://t.co/NE4r2mPRgK",
    "@michaelarria hahahaha",
    "@trevorjoyce ahh ok.",
    "@trevorjoyce why",
    "@trevorjoyce y",
    "R.I.P. immigration reform.",
    "From Jay Griffiths' incredible book Kith http://t.co/kAs40pxuZb",
    "Off-grid living: it's time to take back the power from the energy companies http://t.co/uHxmCSYgS7 via @guardian",
    "How Jurgen Klinsmann Plans to Make U.S. Soccer Better (and Less American) http://t.co/p3yNkOFd6z",
    "@gersandelf there is much investigative journalism, but there is also plenty of writing masqueraded as journalism.",
    "@gersandelf it's called writing a profile. learn what that means before making such statements.",
    "@gersandelf no, this is how journalism works. if your work is public, then you are subject to scrutiny with or without your approval.",
    "Revealed: Asian slave labour producing prawns for supermarkets in US, UK http://t.co/68asbZLPRQ via @guardian",
    "Yes, Nixon Scuttled the Vietnam Peace Talks http://t.co/FF1cwGtwOp",
    "Sometimes you just need a break from the world.",
    "Whitley and Tanaka and pray for rain.",
    "@aronsolomon how did your blue jays get so good?",
    "@WajahatAli I wonder if Modi will make chai for Obama.",
    "With @HillaryClinton at CGIU. http://t.co/9FuzEWZp4k",
    "Another alternative to college: 30 Weeks: An Experimental New Design School, Backed By Google http://t.co/SvljPcAwem",
    "@drewphilp Wow, this is incredible. The @newyorker also had a great piece on the junta a few years ago: http://t.co/w3tQCWGDmv",
    "Excellent piece by @chmader in @ajam: \"The Democrats, especially when in power, have a hard time saying no to war.\" http://t.co/155BvCFfgz",
    "\"Democrats are not actually center-left but center-right, with Republicans a hard-right nationalist alternative.\" http://t.co/155BvCFfgz",
    "Please don't wear a \"short suit.\"",
    "@MilesHalpine Obama took single-payer \"off the table\" very quickly. Never had the courage to fight for it. http://t.co/5zVVmWP4Ux",
    "@MilesHalpine Continues austerity measures in the budget. Slashed billions from food stamps. He also originally wanted to impose chained CPI",
    "@MilesHalpine Climate change: Virtually nothing, except some EPA rules and upping fuel standards. Continues to duck on Keystone XL.",
    "@MilesHalpine ACA helps, but does little to reduce costs and fails to include a single-payer option.",
    "H.I.V.\u2019s Grip on the American South http://t.co/AxogNDjG8C via @NewYorker",
    "@MilesHalpine LOL not even close.",
    "It's nice to remind myself that Joba Chamberlain is no longer on the Yankees.",
    "Trapped in our unjust system of mass incarceration are millions of brilliant people the world won't have the privilege to entertain.",
    "Being able to follow your dreams is a privilege.",
    "@brianpeddle the red sox suck even more though",
    "@JakeAsman So angry.",
    "@micahuetricht I am. They're just playing terribly.",
    "The Yankees suck.",
    "Another stellar @newyorker piece by Rachel Aviv: The Heartland's Pain-Pills Problem http://t.co/OFyUu1a8td #longreads",
    "@orbuch i'll be in town on wednesday. let's grab lunch or dinner.",
    "Lost in Time in England\u2019s Northeast http://t.co/boNzbxWHcm",
    "How Gates pulled off the swift Common Core revolution http://t.co/MOtQnfX172 via @washingtonpost",
    "Bombing, invading, and occupying Afghanistan and murdering and impoverishing its people does not lead to peace. https://t.co/UyltyHTDHR \u2026",
    "With Libya's return to war, democratic dream is all but ruined http://t.co/OVJ84cxqDs via @guardian",
    "Israel's soldiers speak out about brutality of Palestinian occupation http://t.co/xnWape8XFl via @guardian",
    "@j_lanier oh boy",
    "New York sports teams, people.",
    "Hell.",
    "I should watch hockey more often.",
    "This game is insane. #StanleyCup",
    "@shawngude yes, on my list! Thanks.",
    "Charter schools are even more oppressive and restrictive than public schools, which seems almost impossible. http://t.co/eu3D2W1o9H",
    "Yankees pitching. Ugh.",
    "The Yankees have come alive in the 6th. Tie ballgame.",
    "@JessFeelsDressy ah yes. hope you're well!",
    "\u201cLessons From a Year of Solo Travel\u201d by @keeg https://t.co/Jsd5IQodUA",
    "@JessFeelsDressy welcome back!",
    "Barack Obama: This May Not Be The Ideal Moment Politically, But It\u2019s Time To Talk Reparations http://t.co/RIC7cToEBk via @TheOnion",
    "Top Obama Aide Says History Won't Applaud Obama\u2019s Climate Policy http://t.co/fx9TPFOFHh via @Harpers",
    "A Survey of Grown Unschoolers http://t.co/DuHPKiotmv",
    "Save soccer. Abolish FIFA.: \"People don\u2019t have to be displaced and workers don\u2019t need to die for soccer.\" http://t.co/jTShF8wadn",
    "Yankees' top pick could be in majors soon http://t.co/fKgywpldaZ",
    "Can we please make #NotAllEggs a thing?",
    "Three of the five Taliban prisoners released from Guantanamo had joined or tried to join the Afghan government http://t.co/7wA94EpTeJ",
    "Great piece of narrative reporting in the @newyorker: The eight days of the financial crisis http://t.co/rVWHSlfd0A #longreads",
    "Frequent Flyer miles are extremely addictive.",
    "Was just at Penn Station two hours ago.",
    "Announcing the 2014 Class of Thiel Fellows: http://t.co/0tA3DBWxfb",
    "From the 10th floor of the NYU Skirball Center. http://t.co/d2nWf4gopP",
    "For $2,500, you can get an \"anti-drone burqa\" to avoid detection. http://t.co/xX91nzKmGf",
    "When people say schools teach children \"discipline,\" they really mean conformity and obedience to authority.",
    "Snowden: I didn't do anything special. I did a civic duty. #PDF14",
    "Snowden: Security is not the only value Americans treasure. #PDF14",
    "@mgyerman you at PDF? would love to meet!",
    "Snowden: Are we protecting the nation or are we protecting the state? #PDF14",
    "Livestream of whistleblower Edward Snowden speaking at #PDF14 will start shortly. http://t.co/DP5IdtXhiy",
    "With Ta-Nehisi Coates (@tanehisicoates) http://t.co/ejYQPKOPdt",
    ".@GQmagazine's @MikePaterniti reports: The world's most adventurous restaurant: Mugaritz http://t.co/MYdybQWzoy #longreads",
    "Nice piece in @nymag by @jfagone on the breakup of one of the most successful partnerships in typography. http://t.co/lmIGXBQKv0",
    "Three-run home run by Ellsbury. Yankees lead 4-0. Big hit.",
    "@ESPNNYYankees finally they got rid of aceves. what a wreck.",
    "\"Iraq has become a one-stop-shopping jihadist laboratory for car bombs, IEDs, and kidnapping scenarios.\" http://t.co/QE5GWOkIxX",
    "The Dogs of War http://t.co/CV51eyYXz6 via @NatGeoMag #longreads",
    "Nearly a dozen women say a popular Brooklyn teacher abused them decades ago. http://t.co/cqQM3tDEhz",
    "Ramadan road trip: Moving melting pot finds peace, love and animosity http://t.co/86l5yCADMN #longreads",
    "@shereenTshafi hahahaha",
    "Just finished No Place to Hide by @ggreenwald. Go read it. It's an incredible, moving book.",
    "\"The true measure of a society's freedom is how it treats its dissidents and other marginalized groups, not how it treats good loyalists.\"",
    "\"Mass surveillance kills dissent...in the mind, where the individual trains to think only in line with what is expected.\"\n\u2014@ggreenwald",
    "@CharlotteSMBC damn",
    "Thomas Friedman, Maureen Dowd, and David Brooks should all get high together and then self destruct.",
    "Mark Teixeira hits one out! 2-1 Yankees.",
    "\"It is the nature of authority to equate dissent with wrongdoing, or at least with a threat.\" http://t.co/OWUNgCJlNG",
    "The need to constantly prove oneself was also suddenly lifted off their shoulders.",
    "When I talk to students at Sudbury and democratic schools, they are often relieved that they are no longer watched over at all times.",
    "Currently reading the new books by Glenn Greenwald and Alice Goffman. http://t.co/Ri8KxPtRni",
    "@numbalum89 hahaha",
    "Stop asking me this question: \"Will you get to ride an elephant at your wedding?\u201d http://t.co/7B0XqkAmD7",
    "Can anyone explain to me the difference between the warrantless wiretapping program under Bush and mass surveillance under Obama?",
    "Over a million children have mental health problems because they grew up too quickly, claims report http://t.co/KUBU4kpUyq",
    "@CKummer Hi Corby! I sent you an email a few weeks ago. Just wanted to make sure you got it. ngoyal2013@gmail.com. Thanks!",
    "What Excuse Remains for Obama\u2019s Failure to Close GITMO? http://t.co/Qk476gPfml",
    "@brianpeddle hahaha",
    "Anybody going to #PDF14 later this week?",
    "@numbalum89 haha, good quote to save for later!",
    "\"Look at me! Grade me! Evaluate and rank me! I'm good, good, good and oh so smart!\"\n\u2014Lisa Simpson",
    "NSA chief Michael Rogers: Edward Snowden 'probably not' a foreign spy. No shit. http://t.co/Xd62jymFBg via @guardian",
    "@bipolaroids Yes!",
    "\"Children do not need to be 'taught' in order to learn; they will learn a great deal, and probably learn best, without being taught.\"\n\u2014Holt",
    "@almazmom another victim of schooling.",
    "High school student, 17, 'caught cheating on exam jumps to her death in river' http://t.co/EYzrBB5iLs",
    "@HisbeeFrisbee Yes, it's been sitting on my reading list for awhile.",
    "\"Austerity was not an emergency response to testing economic times, but a permanent disassembling of the state.\" http://t.co/l8Fcxf8cIa",
    "@staceyemmert too many pitcher injuries; not enough offense.",
    "@bigdyman happy birthday!!",
    "What is going on with the Yankees? This is embarrassing.",
    "@nicoleradziwill ah, thank you for the mention! great piece.",
    "Last Week Tonight with John Oliver is the best show. http://t.co/5HHOgYIO12",
    "@trevorjoyce @swamp_dad put that on your resume: tweet featured in salon.",
    "@swamp_dad lol danny you're famous http://t.co/RIO3G6z3eQ @trevorjoyce",
    "@nprnews The True American by @AnandWrites!",
    ".@Sulliview calls for Kristof to explain to readers his favorable writing on Somaly Mam's work. http://t.co/s5mUGJlqCr",
    "\"Defining sharia as a threat, therefore, is the same thing as saying that all observant Muslims are a threat.\" http://t.co/4BsuRCKTFk",
    "Now Palestinians must go to the Int\u2019l Criminal Court, and US Should Back Them http://t.co/CmLv6NvvEe",
    "\"[Zapatistas] understood that corporate capitalism had launched a war against us. They showed us how to fight back.\" http://t.co/I550SPJ33D",
    "Who's in control \u2013 nation states or global corporations? http://t.co/QDWGbJrPGc via @guardian",
    "@id3asman thank you! haha.",
    "Alice Goffman\u2019s \u2018On the Run\u2019 Studies Policing in a Poor Urban Neighborhood http://t.co/oxHeT41FMA",
    "\"Prison is considered part of community not isolated institution. Life inside prison needs to resemble life outside.\" http://t.co/IOkwpBd082",
    "Via @nprnews: In Ohio, Inmate Mothers Care For Babies In Prison http://t.co/VuBr3KMOpy",
    "Prison Program Turns Inmates Into Intellectuals http://t.co/KbtSVmXvm6",
    "Had a wonderful birthday! Thanks for all the wishes.",
    "@luknorris hahaha",
    "@luknorris quality tweet.",
    "Please pronounce \"Iraq\" and \"Iran\" correctly.",
    "One effect of over-policing: \"I once saw a 6-year-old pull another child\u2019s pants down to attempt a cavity search.\" http://t.co/pIMZM7PL3b",
    "Anand Gopal on how America is bankrolling corrupt, murderous warlords in Afghanistan. http://t.co/8o3sH56b4i",
    "Great piece in the @nytimes on how children had more freedom to roam and play in the 19th century. http://t.co/oro2hvjdTc",
    "@shereenTshafi it makes it much easier to determine who to block.",
    "Great piece by @nitashatiku in today's @nytimes on teaching girls to code (nice @geekgirlweb shout-out!). http://t.co/UvOY8J51Bl",
    "Dellin Betances is one of the most talented pitchers I've had the great privilege to watch.",
    "@kennycooks thank you! happy birthday to him as well!",
    "@LineDalile thank you!",
    "I think it's fitting that my birthday falls on International Children's Day. Here's to another year of activism for children's rights.",
    "\"Bosnian Serb forces committed genocide. They targeted for extinction 40,000 Bosnian Muslims living in Srebrenica...\" http://t.co/pnyxRyAopz",
    "Incredible story in @nytmag on the Srebrenica massacre in Bosnia two decades later http://t.co/IgZccDwTrz",
    "@michaelarria hahahahahha",
    "@Tara_SuperSub thank you!",
    "@MicahSingleton thank you!",
    "@badsushichef ha, no. thank you.",
    "\u201cMen explaining things to me had been happening my whole life\u201d: The author behind \u201cmansplaining\u201d  http://t.co/A6UZZoMFVC",
    "@veganforareason thank you! likewise.",
    "@adorasv thank you!!",
    "@JonathanCohn yes, thank you!",
    "Officially reached the ripe old age of 19." ]
    
    dataLen = len (data2)
   # print dataLen
# x = int(round(dataLen/2))
   # print isinstance (dataLen,tuple)
   # print isinstance (x,tuple)
   # print data2[3]
    data3 = data2[0:30]
   # data4 = data2[80:dataLen]
    data4 = [] 
    addUserTwitter ('cahnda',data,data3,data4)
    print getUserTwitter('cahnda')

