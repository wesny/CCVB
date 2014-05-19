window.onload = function () {
    document.getElementById("dialog").innerHTML = "";
}

// var favorite_vals = "{{ favorite_vals | tojson | safe}}";
//console.log( favorite_vals)
// Graphs your posts to tell you how popular they have been using d3.js

var height=400, width=400;
var yPadding=10;
var xPadding=40;

var svg = d3.select("body").append('svg')
    .attr('width',width)
    .attr('height',height)
    .attr('id','svg')
    .style('border','1px solid')

d1 = []

// Nikhil Goyal's favorite values for recent posts
favorite_vals = [0, 0, 0, 0, 0, 0, 1, 2, 17, 3, 0, 2, 1, 2, 1, 2, 2, 3, 1, 0, 0, 0, 0, 2, 0, 3, 2, 1, 2, 0, 0, 1, 3, 4, 34, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 2, 0, 1, 1, 3, 2, 2, 2, 0, 0, 2, 0, 2, 1, 0, 7, 0, 2, 4, 4, 10, 4, 4, 5, 1, 1, 2, 0, 2, 0, 3, 5, 3, 5, 0, 3, 6, 1, 12, 18, 0, 3, 6, 1, 0, 5, 3, 1, 12, 1, 1, 2, 0, 0, 1, 0, 2, 0, 0, 1, 0, 0, 2, 1, 1, 0, 3, 6, 0, 2, 0, 0, 1, 0, 0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 2, 0, 3, 5, 2];

text_vals = [
        "Arrived in London! (at @HeathrowAirport) \u2014 https://t.co/5dqNWCYOQN",
        ".@louisck and others are missing the major problem with Common Core: that nobody besides the learner should decide what to learn.",
        "Headed to London. In Europe: London, Budapest, and Amsterdam\u2026 (at John F. Kennedy International Airport (JFK)) \u2014 https://t.co/VROylag1vd",
        "Vote for my friend and school board member @JoshuaLafazan in the Bammy Awards! http://t.co/uIVE5loF4J",
        "\"A racism that invites the bipartisan condemnation of Barack Obama and Mitch McConnell must necessarily be minor.\" http://t.co/MvksnZi308",
        "\"Elegant racism is invisible, supple, and enduring. It disguises itself in the national vocabulary.\" http://t.co/MvksnZi308",
        "Anyone know if the London Tube strike is over?",
        "On Friday and Saturday nights, people should just hang out in bookstores instead of bars.",
        "NYT journo's book on gay rights \"is riddled with the telltale signs of a reporter becoming too close to her sources.\" http://t.co/SYYfQioUFH",
        "@BhasChat Or Malcolm X for me.",
        "Via @nprnews: Experimental School Gets Rid of Classes, Teachers http://t.co/vwq1USUTFt",
        "@srchiose hey! sent an email a few weeks ago. wanted to make sure you got it.",
        "Time to Ban Corporal Punishment for Good http://t.co/gJHmpVKdWG",
        "@jesslahey great piece!",
        "@JacobBayes lol",
        "What do you think of this book title: Every Child Is An Artist: How Schools Rob Our Children of Their Education, Freedom, and Dreams?",
        "Hedges: Under Obama, the deterioration of civil liberties has been much worse than under Bush. http://t.co/UySJowp7xL",
        "\"Reducing children to a test score is the worst form of identity theft we could commit in schools.\"\n\u2014Steven Covey",
        "I wish it rained every day.",
        "Three bell hooks' lectures at the New School in NYC next week: http://t.co/iyQKNxWybt",
        "\"No one can cite even a single terrorist attack that has been stopped, or could have been stopped, with torture.\" http://t.co/oG4nZeEG9o",
        "@samknight1 Amazing book.",
        "Great @newyorker piece: \"A journey through the mangrove forest of Bengal.\" http://t.co/aQtVxacfod #longreads",
        "Can Jonathan Chait get any more awful?: \"What\u2019s Behind That Insanely Hostile NYT Story on Charter Schools?\" http://t.co/Pppf9gZo0r",
        "How much action does a baseball game have? Almost 18 minutes http://t.co/7H8IKU8vyB",
        "The Island Where People Forget to Die http://t.co/GeWedlZgDe #longreads",
        "\"Leaving school is an acknowledgment of a dynamic that isn't working and a movement toward change.\" http://t.co/JzUei5pIqD",
        "@numbalum89 Shhhh",
        "Yankees fans are chanting to Cano: You sold out.",
        "@keyindabox He'd make more money outside of baseball if he were still in NY.",
        "And Cano strikes out. That's what he gets for leaving the Yankees.",
        "\"From 1995 to 2006, nearly 200,000 farmers killed themselves in different parts of India.\"\n\u2014Deb in The Beautiful and the Damned",
        "Activist: Farmer suicides in India linked to debt, globalization http://t.co/Pb9LVfbZSM #cnn",
        "Chris Hayes on Climate Change: Fargo Will Be as Hot as Phoenix http://t.co/4msz9xwc5q",
        "Finished reading Siddhartha Deb's excellent book: The Beautiful and the Damned, which humanizes the immense changes in Indian society.",
        "@JD1871 lolololo",
        "CNN \"seems to have a thing for exploiting Asian fatalities for fun and profit.\" http://t.co/dRxY2ARrNA via @Salon",
        "@scottroth76 @Ali_Gharib that's offensive to children.",
        "Looking forward to Robinson Cano's return to the Bronx.",
        "@audreywatters lolololo",
        "@audreywatters and vox will then explain the question.",
        "Politico: How will Donald Sterling's lifetime ban affect Hillary Clinton's potential presidential run in 2016?",
        "Adam Silver for U.S. Attorney General.",
        "Donald Sterling was dealt a larger punishment than any Wall Street banker received in the wake of the financial crisis.",
        "@JD1871 George Steinbrenner was once banned from baseball.",
        "Woah. Sterling banned for life from NBA and Clippers and fined $2.5 million.",
        "@goodglobalcitiz ah yes, just looked it up.",
        "@goodglobalcitiz haha well i'm staying with a friend about half an hour outside of london.",
        "@goodglobalcitiz but could be continued until monday.",
        "Did some research on the London Tube strike. Most articles are on how to survive it, not about the austerity measures directed at workers.",
        "A few days before I'm in London, there's a Tube strike. http://t.co/ZL98pAyN8f",
        "Climate change is the fight of our lives \u2013 yet we can hardly bear to look at it. http://t.co/MvDrH1hOBO via @guardian",
        "@jfagone congrats!!",
        "Goal of the David Project: \"to stifle and censor discussion of Israel\" https://t.co/YYAS4w6PRA",
        "Important Guardian piece by @antloewenstein: Australians were killed by a US drone strike, and we deserve to know why http://t.co/KDtO9rGOKg",
        "Jimmy Fallon tricks Yankees fans into booing Robinson Cano to his face http://t.co/NLwMWSycl2 via @Cut4",
        "@rupertbe @VolkanTopalli No. Palestinians are under Israeli occupation.",
        "@rupertbe @VolkanTopalli See link: http://t.co/kc7McxpnMd",
        "@rupertbe @VolkanTopalli \"Arab citizens of Israel who marry Palestinians will have to emigrate in order to live with their spouses.\"",
        "@rupertbe @VolkanTopalli Yes, there are more than 50 laws that discriminate against Palestinian citizens of Israel.",
        "Well if it isn't John Kerry pandering to the Israel lobby?",
        "@alan_uplc @JonahHill ha, I didn't know it was a TV series before.",
        "\"Each month, there are more suicide terrorists trying to kill Americans and their allies than in all the years before 2001 combined.\"",
        "\"More than 95 percent of all suicide attacks are in response to foreign occupation.\" http://t.co/KxJ9yJC9qz",
        "@DrLeeAnneG unfortunately not; will be traveling.",
        "@robdelaney @louisck I wrote a piece for MSNBC on this: American students deserve better than Arne Duncan http://t.co/XwQ3fDA46R",
        "\"The greatest weapon of mass destruction turned out to be the invasion itself.\" http://t.co/3jg58SATQn",
        "Don't call yourself a humane individual if you defend the havoc wreaked on the Iraqi people in the U.S. invasion of Iraq.",
        ".@jts @MITDelian But that \"collateral damage\" has inspired extremism, suicide bombings, and people to take up arms against the U.S.",
        ".@jts @MITDelian \"601,000 more people died in Iraq as a result of violence than would have died had the invasion not happened.\"",
        ".@jts @MITDelian Hope you know that the war was about oil and ramming through free-market policies, not help the Iraqis.",
        ".@jts @MITDelian \"Democratic\" elections? More like a farce. Genocide? U.S. tortured, killed, wounded hundreds of thousands.",
        "@jts @MITDelian How exactly is the Middle East better off?",
        ".@jts @MITDelian You really think the Middle East is better off after the murder of hundreds of thousands of innocent civilians?",
        "@jts @MITDelian Did Blair and Bush not circumvent the United Nations and launch an invasion of Iraq? http://t.co/FsN3AhFsv4",
        ".@MITDelian Tony Blair = war criminal.",
        "John Oliver interviews General Keith Alexander, the former NSA chief. Hilarious. http://t.co/dz6EnZfAOB",
        "Will Dylan Byers please shut up and sit down?",
        "I really hate writing application essays.",
        "Nice piece in @theatlantic by @reyjunco on the boons of playing Minecraft. http://t.co/vNjIAjclbh",
        "Awesome piece by @RyanHoliday on whether you should drop out of college or not. http://t.co/6HXxy57Aes",
        "\"The NGO-ization of politics threatens to turn resistance into a well-mannered, reasonable, salaried, 9-to-5 job.\" http://t.co/5z9zeu6ks5",
        "If people were educated of the nefarious intent of the school system's architects, many would feel repulsed to have anything to do with it.",
        "In school, you never learn the history of the very institution children are confined in for thirteen years of their lives.",
        "It frustrates me how few people know the origins of the American compulsory schooling system.",
        "Abolish compulsory schooling. http://t.co/vnDvyxeqaN",
        "\"It has been found that the best way to insure implicit obedience is to commence tyranny in the nursery.\"\n\u2014Benjamin Disraeli",
        "The female 'confidence gap' is a sham http://t.co/RNiJY6IbF3 via @guardian",
        "TEIXEIRA. HOME RUN.",
        "Desmond Tutu: \"Israel will never get true security and safety through oppressing another people.\" http://t.co/eTw8fUmnXB via @guardian",
        "@adamhudson5 awesome piece!!",
        "@BhasChat and they will never leave.",
        "Would You Notice Your Mother Dressed as a Homeless Person?http://t.co/hIfNZRzeHb via @truthdig",
        "MT @mat_johnson In America you don't say racist things, you just quietly perpetuate and endorse underlying racist ideologies.",
        "Sterling may be punished, but blacks will continue to be victims of white supremacy, war on drugs, police brutality, and the justice system.",
        "Dear person who has looked at my LinkedIn at least twice a week: I haven't updated it in months.",
        "Please stop taking selfies and just ask someone to take the picture for you.",
        "I've transcribed over ten hours of interviews in the past few days. About to pass out.",
        "@BhasChat \"Most American high schools are almost sadistically unhealthy places to send adolescents.\" http://t.co/gfOBhqfLOP",
        "Fascinating story in the @newyorker of an Arizona nursing home that cares for people with dementia http://t.co/xZhoXM0cuj #longreads",
        "The Media Has a Woman Problem http://t.co/5TwmnGUFZf",
        "Isn't it odd that the opponents of affirmative action aren't as fervently opposed to legacy preferences in admissions?",
        "Criticize racist remarks, but not a word about institutionalized racism or white supremacy.",
        "Good @nytimes piece by @motokorich on the Walton Foundation's deep pockets in the charter school movement. http://t.co/Qonqnao4bq",
        "Oh boy. Now he's asking for examples of \"gender bias\" in society.",
        "A privileged white male just posted on FB that gender discrimination is a \"non-issue.\" Oh my.",
        "YANKEES WIN.",
        "Ellsbury. Boom.",
        "Choosing a university? Look into campus rape rankings before you start packing. http://t.co/IaIoTjZ6Kq via @guardian",
        "revolution. diplo.",
        "\"U.S. was presented with a possibility that might have saved countless lives: the surrender of top Taliban leaders.\" http://t.co/Y540MXDGzO",
        "so many good books to read. so little time.",
        "@mattaikins added to my list!",
        "Leave it to Fareed Zakaria to whitewash Narendra Modi's legacy. http://t.co/OhAaaSkfqm via @TIME",
        "Why a \u2018Student Privacy Bill of Rights\u2019 is desperately needed http://t.co/5I7lKJDjB8",
        "@rcarzo I'm too scared to switch over.",
        "@aronsolomon And true.",
        ".@Laura_E_Adkins If there's one thing you should learn from yr irresponsible and odious actions, it's that you shouldn't go into journalism.",
        "@id3asman Macbook Pro!",
        "Nice @newyorker profile of Paul Watson, the founder of the Sea Shepherd Conservation Society. http://t.co/SQmhPk0kta #longreads",
        "\"Lockheed Martin\u2019s interest in getting inside your private life via surveillance has remained undiminished.\" http://t.co/8G9JIJy86F",
        "Kuroda is getting slammed tonight.",
        "@SirKenRobinson Congrats, Ken!",
        ".@TIME calls writer and activist Arundhati Roy \"the conscience of India.\" http://t.co/JmaqgSAG9G",
        "Duke Porn Star Belle Knox Tells All http://t.co/vq26n1qHHD via @rollingstone #longreads",
        "Next week, I'm headed to Europe for three weeks. If you're in London, let me know if you're around.",
        "\"Write in crowds, in alleys, in the back seats of crumb-filled cars.\" http://t.co/21EG0H4seM",
        "End College Legacy Preferences http://t.co/iGq2jV3CyR",
        "James Rhodes: Find what you love and let it kill you. http://t.co/LNgusROjqx",
        "\"Black has always been beautiful, way before neoliberalism enabled whiteness to say so.\" http://t.co/actVyNApGo via @guardian",
        "College Campuses Are Treating Rape Like A Crime Without Criminals http://t.co/PWUpyoiuwT",
        "@JakeAsman This team looks so much better than last year.",
        "Incredible performance by the Yankees against the Red Sox tonight. 12-2.",
        "\u2018The Price of Silence\u2019 Replays a Wrenching Campus Episode http://t.co/Y1A42M8bMh",
        "YANGERVIS.",
        "Pine Tar Should Be Fully Legal, And Baseball Is Still Fucking Insane http://t.co/ls0ATAK9wI",
        "The U.S. should \"use its influence to pressure Israel to abandon its commitment to ethnoreligious segregation.\" http://t.co/GHILPGl8Y4",
        "In @gqmagazine: Welcome to Camp Idontwantobama! http://t.co/39463zzBvM #longreads",
        "If you haven't personally read the damn book, you have no right to criticize it. #Piketty",
        "Alfie Kohn: Why \u2018grit\u2019 is overrated http://t.co/JA1NBv8cxK via @washingtonpost"
    ];


for (i=0; i<favorite_vals.length; i++) {
    d1.push ({
	'label':i,
	'x':i,
	'y':favorite_vals[i],
	'text':text_vals[i]
    })
}

var yScale = d3.scale.linear()
	.domain([-2, d3.max(d1,function(d){return d.y;}) ])
	.range([height,0]);

var xScale = d3.scale.linear()
    .domain([d3.max(d1,function(d){return d.x;})+20,-9 ])
    .range([width,0]);

var c = svg.selectAll("circle")
    .data(d1)
    .enter()
    .append("circle")
    .attr('r',5)
    .attr('cx',function(d) {return xScale (d.x);})
    .attr('cy',function(d) {return yScale (d.y);})
    .attr('fill','steelblue')

$("#svg").on("mouseover", "circle", function(event){
    document.getElementById("dialog").innerHTML = "";
    myVar = this;
    xCor = event.screenX;
    txt = text_vals[xCor];
    var txtNd=document.createTextNode(txt);
    document.getElementById("dialog").appendChild(txtNd);
    $( "#dialog" ).dialog(); 
});

$("#svg").on("mouseout", "circle", function(event){
    $("#dialog").dialog('close');
});


var yAxis = d3.svg.axis()
	.scale(yScale)
	.ticks(10)
	.orient('left')

var xAxis = d3.svg.axis()
	.scale(xScale)
	.ticks(10)
	.orient('')

svg.append("g")
    .attr('class','axis')
    .attr('transform','translate (25,-20)')
    .call(yAxis);

svg.append("g")
    .attr('class','axis')
    .attr('transform','translate (0,375)')
    .call(xAxis);
