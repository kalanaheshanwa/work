#!/usr/bin/env python3
"""
Kalana Square — Work Catalogue generator.
Edit PROJECTS below and run:  python3 build.py
Outputs index.html + projects/*.html (static, GitHub Pages ready).
"""
import os, html

CDN = "https://images.squarespace-cdn.com/content"

SQSP_LOGO = "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/36d8bf55-de6a-475f-9d1e-229d8441190c/squarespace-logo-png-transparent.png"
PORTRAIT = "https://images.squarespace-cdn.com/content/v1/69cdfa4b7e96fb29aceec739/6d195aac-e2b3-4a6f-b54e-0fbe33978339/portrait.png"
UPWORK = "https://www.upwork.com/freelancers/kalanaheshan"
LINKEDIN = "https://www.linkedin.com/in/kalanaheshan/"

LINKEDIN_ICON = """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.5 8.25H3.25V18.5H6.5V8.25ZM4.88 3.5a1.88 1.88 0 1 0 0 3.75 1.88 1.88 0 0 0 0-3.75ZM18.75 12.63c0-3.08-1.64-4.51-3.83-4.51a3.3 3.3 0 0 0-3 1.65V8.25H8.67V18.5h3.25v-5.08c0-1.34.25-2.64 1.91-2.64 1.64 0 1.66 1.53 1.66 2.73v4.99h3.26v-5.87Z"/></svg>"""

LOGOS = [
    ("Psych Science Hub", "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/91415749-5043-4a6f-875f-fd3900e2e1a7/Psych+Science+Hub+.png?format=400w"),
    ("Wellnergy", "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/c1e18a15-41de-4431-ad96-9bc101cdbacb/wellnergy-logo-brandmark-rgb-yellow.png?format=400w"),
    ("The Curly Pineapples", "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/b6b7f76d-410e-4fc6-98cf-c927a0b512a8/The+Curly+Pineapples_.png?format=400w"),
    ("NanoPing", "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/0f3b3c73-5452-4927-82b8-686abd497688/Steinwurf+is+Evolving+into+_NanoPing.png?format=400w"),
    ("Snap & Boom", "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/3264c34f-51dc-45ba-8366-935c4260937d/Snap+%26+Boom__.png?format=400w"),
    ("Pink Steak", "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/412e2021-5a95-4473-b14a-23e161da7673/Pink+Steak.png?format=400w"),
    ("Fletcher Films", "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/209b5ce9-d551-48fc-9508-677c76379e51/Fletcher+Filmsnation+Wedding+Videographer.png?format=400w"),
    ("Direct Booking Summit", "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/9ace5322-f841-492d-bd32-e7da04aafc54/Direct+Booking+Summit.png?format=400w"),
    ("Coastline Therapy Group", "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/b16d4bb7-e3ed-4b0a-8fa8-80879afbb085/Coastline+Therapy+Group_.png?format=400w"),
    ("Author Magazine", "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/14b3dddf-a705-4c2a-908a-1645a8af7618/AUTHOR+MAGAZINE.png?format=400w"),
    ("Ambiance Atlanta", "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/8405f770-a57c-499f-b9d0-ecef03895fb8/Ambiance+Atlanta.png?format=400w"),
]

BADGES = [
    ("Upwork Top Rated", "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/54b79e05-27ba-4816-a16d-d31c0102f694/upwork-top-rated-dark.png?format=300w", ""),
    ("Fiverr Top Rated", "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/5eb2f7a6-69fa-440e-b9a1-c13fb12a9cc7/fiver-top-rated-dark.png?format=300w", ""),
    ("Squarespace Marketplace Expert", "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/2ec0a90b-a285-4a58-a719-26c51ffcfbed/squarespace-expert+%281%29.png?format=300w", "https://www.squarespace.com/designer/profile/4920324"),
    ("Squarespace Circle Platinum Partner", "https://images.squarespace-cdn.com/content/69cdfa4b7e96fb29aceec739/6b46491c-b4bd-4980-9271-8291aabc0ca5/squarespace-circle-partner.png?format=300w", "https://forum.squarespace.com/profile/363220-heyshan/"),
]

TESTIMONIALS = [
    ("Ed Breed", "Jun 2026", "$700", "Squarespace Website for Brand Your Journey", "I needed someone with strong expertise in Squarespace to convert some illustrated concepts into a functional website. Kalana hit the mark. He had great solutions to the issues raised, provided regular updates, and gave me options throughout the build. When he needed me to evaluate the options, we jumped on a video call. Kalana was very detail-oriented and delivered every milestone on time. He is an excellent resource, and I highly recommend him."),
    ("Melissa Pinson", "Jun 2026", "$400", "Website redesign", "Fantastic to work with \u2014 very responsive, efficient, and highly receptive to feedback throughout the process. Collaboration was seamless, and he consistently delivered high-quality work in a timely manner. I will definitely be hiring him again for future projects."),
    ("David Carlson", "Jun 2026", "$675", "Squarespace Website Designer for In-Home Medical Practice", "Kalana did an outstanding job building our InHomeMD.com website on Squarespace. From start to finish he was proactive, highly knowledgeable, responsive, and incredibly patient. He consistently anticipated issues before they became problems and showed a deep understanding of Squarespace and design best practices. What impressed us most was his professionalism and commitment to getting every detail right. He delivered a website that exceeded our expectations. If you want someone technically skilled, reliable, and genuinely invested in your project, I highly recommend Kalana."),
    ("Oluwaseyi Ayodeji", "May 2026", "$760", "SquareSpace Personal Website Development", "I had the best experience using Kalana for my website. He was immensely patient and knowledgeable. I always had a 1001 questions and he met me with 1002 answers for each of my questions. I unequivocally recommend him if you need someone to be patient through ideation while also delivering top notch work. Thank you Kalana."),
    ("Justin Traucht", "May 2026", "$840", "Website Development Using Squarespace (HTML Mockup)", "Kalana was excellent to work with. He completed every task to perfection. He was able to bring the vision of a perfect website on desktop and mobile together on Squarespace. There were lots of things that were asked of him and he was able to complete them all right away. I will definitely be using him and recommending him for future projects."),
    ("Tom Serby", "May 2026", "$150", "Squarespace Layout Implementation for Business", "Great experience with Kalana, was able to replicate my ideas into reality and happy with the work he produced, will be using again for sure."),
    ("Debra Jackson", "May 2026", "$300", "Professional Squarespace Website for Medical Billing", "I had to kiss a lot of frogs before I met Kalana. He was very different from the start. Kalana was extremely patient with this very picky person. From the start, he suggested we get on a call because he wanted to make sure his understanding of my vision was aligned with mine. That level of communication made a major difference. As a result, I now have a beautiful, professional website that truly reflects my company and brand. Thank you for your patience, kindness, expertise, and strong attention to detail throughout this project."),
    ("Alexander Stellar", "Apr 2026", "$500", "Website update for recreation company", "Great Web Designer! We hired him to work on our Squarespace and it went flawlessly. 100% recommend him to anyone on Upwork looking for a great website design or Squarespace optimization."),
    ("Duy Bui", "Apr 2026", "$630", "Custom Jewellery Website On Squarespace", "Kalana has been nothing but amazing on helping me with my website. So helpful on helping me set up everything I needed to do. Would definitely work with again."),
    ("Lucy Faulconbridge", "Apr 2026", "$200", "Squarespace Website Design and Optimization", "We were very happy working with Kalana. He turned the project around quickly and was receptive to feedback and easy to work with."),
    ("Christopher Jakobsen", "Apr 2026", "$20", "30 minute consultation", "Excellent first experience working with Kalana! I'm immediately booking him for the next job."),
    ("Teyonna Bowman", "Mar 2026", "$800", "Squarespace website For Cancer Survivors", "Kalana was great to work with! He was very responsive to all of my questions and provided accessible tools to complete our website work. Kalana is very knowledgeable about Squarespace and collaborative when making suggestions. He consistently went above and beyond by being available for calls, making changes in real time and taught me how to make updates myself. I will definitely work with Kalana again and highly recommend him."),
    ("Nick Ghionis", "Mar 2026", "$650", "Squarespace Photography and Video Website", "Kalana was not only professional and knew his stuff, but was also patient. Creating a website is daunting enough, so when it came to holding my hand all the way, he was brilliant. I highly recommend him."),
    ("Karen Aroney", "Mar 2026", "$1,000", "Premium Website Formatting & Optimization", "Working with Kalana was an exceptional experience. He is highly skilled, professional, and truly excellent in his speciality. He took the time to understand my vision and matched it perfectly. His work is clean, precise, and delivered with a clear, thoughtful process. What I appreciated most was his communication \u2014 he keeps you informed at every stage so you always know what's happening. It made the entire experience seamless and stress-free. I would confidently recommend Kalana to anyone looking for quality work."),
    ("David Rabkin", "Mar 2026", "$330", "Squarespace (Paloma Template) Literary Website", "Working with Kalana was efficient, effective, and fun! Kalana is extremely responsive, very available, and highly committed. He did such a nice job ensuring he understood each component along the way, even if it meant asking a series of clarifying questions. He was also responsive with changes and edits, and contributed his own helpful ideas. I would certainly work with him again!"),
    ("Shauna Moran", "Mar 2026", "$420", "Website Changes", "Wonderful to work with Kalana on my Squarespace website. He's technical with the right eye for design and communicates exceptionally well. A pleasure and I'll be using him going forward."),
    ("Max First", "Mar 2026", "$209", "Website Update and Maintenance for Squarespace", "Kalana was fantastic to work with. From the beginning, he was extremely professional, responsive, and detail-oriented. He quickly understood the vision I had and translated that into a clean, modern, and functional design. What I appreciated most was how easy he made the entire process. He was proactive, organized, and always willing to go the extra mile. The final result exceeded my expectations and the site feels much more polished and user-friendly. I would absolutely recommend Kalana."),
    ("Andrey Zverev", "Feb 2026", "$1,500", "Develop a Squarespace website based on Figma", "I worked with Kalana on developing a completely new website for my nail salon business in Midtown Manhattan. I provided a custom design created in Figma, and the task was to build the site from scratch. The project was not simple \u2014 it involved custom coding and integration of external resources to achieve the desired functionality. Kalana handled everything professionally and efficiently, consistently proposing effective solutions. I always felt confident that he knew exactly what he was doing. The website is now live and performing well. I would definitely work with Kalana again."),
    ("Jonas Helmy", "Feb 2026", "$185", "Review and Improvement of Existing Website", "Working with Kalana was a fantastic experience from start to finish. The final website looks polished, modern, and performs flawlessly across devices. Kalana was proactive with suggestions and quick to resolve any feedback or changes. I'd absolutely recommend him to anyone looking for a reliable and talented web developer."),
    ("Jamie Torr", "Feb 2026", "$400", "Squarespace website build", "Outstanding service. Kalana goes above and beyond."),
    ("Camille Goldstein", "Feb 2026", "$120", "Squarespace expert to improve mobile friendly", "Kalana was a pleasure to work with. He is thoughtful, thorough, and very clear in his communication. He took the time to answer all of my questions and even jumped on a call to make sure I fully understood the work he was doing. He delivered everything in a timely manner and was easy to collaborate with. I would absolutely work with him again and highly recommend him."),
    ("Kevin Reynolds", "Jan 2026", "$105", "Create Professional Squarespace Store", "Kalana worked so quickly and everything was very well done! Will be using him again for future updates."),
    ("Heather Bolen", "Jan 2026", "$40", "Add hyperlink to Squarespace form", "Kalana helped me with some custom code for a product launch on my website. I had a very tight turnaround of a few hours, and he was able to get it done on very short notice, along with a high level of communication. Highly recommend!"),
    ("Hsing Tseng", "Jan 2026", "$600", "Squarespace designer for a wedding industry website", "Very fast turnaround and good design work, understood the editorial vision I was going for. Implemented changes quickly via Squarespace."),
    ("Melody Pabon", "Jan 2026", "$300", "Building a custom wedding website on Squarespace", "We had a fantastic experience working with Kalana on our wedding website. He was incredibly responsive and trustworthy, and did an excellent job getting a strong MVP up and running quickly. He was very open to feedback and truly collaborative throughout the process. Even when we were overwhelmed or slow to respond, Kalana stayed in the driver's seat and owned the project with professionalism and calm. We would absolutely recommend him!"),
    ("Danielle Taliaferro", "Jan 2026", "$600", "Squarespace Website Builder for Travel Agency", "Kalana was an incredible asset to our new business as we prepared for the official launch! He built a beautiful website for us that truly reflected our vision \u2014 with patience, kindness, and expertise! We will definitely be hiring Kalana again for future projects!"),
    ("Amanda Brkich", "Dec 2025", "$150", "Squarespace Custom Coder", "Kalana was great to work with! He tackled our Squarespace custom code task quickly and efficiently. As soon as we began he suggested we hop on a call where we clarified our needs so he could get started immediately. He shared updates and asked questions as needed. Would 100% recommend Kalana for your custom coding needs."),
    ("Shannon Sauer-Zavala", "Dec 2025", "$2,300", "Squarespace website Redesign and development", "Kalana was extremely responsive to our team's needs. He helped us create a website with the functionality we needed and asked for feedback along the way. He also made us Loom videos so we can make minor edits ourselves. We absolutely plan to work with Kalana in the future as we update our site with more content."),
    ("Christopher Stear", "Dec 2025", "$150", "Fast, Precise Sales Page Build (Wireframe Provided)", "Kalana was very professional, easy to work with, exhibited outstanding attention to detail, excellent understanding and implementation of the brief, and delivered high quality milestones ahead of an already tight schedule. I'm happy to recommend him unreservedly and will be using him with complete confidence when an opportunity arises."),
    ("Raj Samuel", "Dec 2025", "$330", "Squarespace website UI/UX Fix and Redesign", "Kalana has brilliant UX & Design skills. My site definitely needed some UX & Design improvement and he was able to deliver. When something wasn't working quite right, we discussed and he was able to solve it. I highly recommend using him for UX & Design."),
    ("David Cull", "Dec 2025", "$300", "Squarespace website development", "Kalana was fantastic. He ensured that we were totally happy with the final product before sign-off. I would highly recommend Kalana."),
    ("Rachel Preddey", "Dec 2025", "$200", "Resource page layout and website design", "Excellent communication, quick to deliver and completed job as required. Thank you. Will definitely hire again."),
    ("Joshua Clark", "Nov 2025", "$500", "Squarespace Website & Logo for Surfboard Company", "Kalana was attentive to my needs and easy to collaborate with. He took direction well and had a lot of positive input. He made the process easy and I am happy with the results. I will use him for future projects."),
    ("Zion Pineda", "Oct 2025", "$870", "Squarespace redesign", "Working with Kalana has been a great experience. He's professional, talented, and very responsive throughout the entire project. He handled the design of a full website with multiple pages, incorporated feedback quickly, and made updates the same day when needed. I appreciate his patience, attention to detail, and commitment to delivering quality work. I'd gladly work with him again and highly recommend him."),
    ("Tobi Atte", "Oct 2025", "$400", "Conference / course web pages", "Kalana is hands down one of the best experiences I have had on any freelance site. He cares about the project and takes initiative to ensure success. He is detail oriented and will ensure that everything gets checked off. Absolutely amazing!"),
    ("Jennifer Kim", "Oct 2025", "$525", "Squarespace Website Consolidation & Redesign", "I am very pleased to share my experience working with Kalana on my Squarespace website. From start to finish, he demonstrated exceptional skills in website design as well as consolidating my other businesses into one branding. The project was delivered on time, communication was professional, and attention to detail was exceptional. I highly recommend Kalana for anyone looking for a reliable and talented web designer and SEO optimization."),
    ("Sarah Talbot", "Oct 2025", "$400", "Squarespace website for Flair Recruitment LLC", "Kalana built my website from the ground up, including helping me shape my brand and logo. At first, I wasn't sure what I wanted, but he was patient and worked at my pace. He really listened when I asked for changes, answered all my questions, and even offered to remain available for support now that I'm managing my own site. I highly recommend Kalana for his dedication and work ethic \u2014 he's incredibly responsive and often available seven days a week. Thank you, Kalana!"),
    ("Lucy Hargrave", "Sep 2025", "$393", "Squarespace Design and Build", "Kalana built a complete Squarespace website based on our existing style guide and Figma template. He completed the project quickly and implemented changes with ease. Would highly recommend."),
    ("Tyler Van Den Handel", "Sep 2025", "$350", "Logo & Branding", "Kalana was a pleasure to work with and exceeded my expectations creating branding and a website for my business. I would certainly recommend his services to anyone, and plan to utilize him again in the future."),
    ("Ana Valdez Curiel", "Sep 2025", "$2,000", "Website Design for Tourism Van Transport Service", "Kalana was extremely attentive, helpful and did the design exactly to my liking. I would work with him over and over again due to his professionalism, quick response time, and knowledge. He's the first person I've used on Upwork and I was very satisfied with my results."),
    ("Gordon Allott", "Sep 2025", "$630", "Squarespace Website Development for Mobile App", "Super Professional. Very fast turn around. Kalana is a Squarespace guru. Pulled together the requested website in no time. Filled in grey areas very well. Was able to really come through with minimal guidance. Would absolutely use again and again."),
    ("Julie Bertonazzi", "Sep 2025", "$147", "Make current website user friendly", "Once again it was a great experience."),
    ("Gavin Versi", "Aug 2025", "$500", "Healing Washington Squarespace website build", "I had a wonderful experience with Kalana. He is super-responsive, has an eye for detail, and quickly understood my preferred way of working. He is generous with his time, patient, and thorough. He possesses all the requisite skills I associate with a web designer. I would not hesitate to re-hire him."),
    ("Sarah Magliolo", "Aug 2025", "$275", "Create Membership Site within Squarespace", "I've worked with Kalana on multiple Squarespace projects and he is my go-to for any web work! He's built new pages in my website and built out my membership space most recently. I look forward to continuing to work with him and recommend him highly!"),
    ("David Boh", "Jul 2025", "$150", "Fix and Customize Mobile Header CTA Button", "Kalana has been highly responsive and professional. Even when there were certain issues that were not mentioned at the start of the contract, he was accommodating to help solve it. Highly recommended for anyone looking to hire someone for Squarespace projects."),
    ("Obaid Ur Rehman", "Jul 2025", "$400", "Complete Squarespace Website Redesign", "Great work on my Squarespace redesign. Clean, modern, and exactly what I needed. Easy to work with and delivered on time. Highly recommend!"),
    ("Sandy Shamon", "Jun 2025", "$225", "Website Migration from WordPress to Squarespace", "Kalana did a great job redesigning and transferring our business website into Squarespace. His work is very accurate, efficient, and aesthetically appealing. He ensured all issues were problem solved along the way until the website was live. I highly recommend working with him!"),
    ("Amalia Camateros", "Jun 2025", "$40", "30 minute consultation", "Kalana has a broad scope of knowledge and expertise in what I need with web development and how to use Squarespace. He is kind, patient, skillful and confident in approaching work, listens carefully and produces exactly what I need. He also has extra applications that offer a broad range of options to enhance the projects at hand."),
    ("Kelly Rust", "Jun 2025", "$525", "Further website development \u2014 properties page", "Kalana is wonderful! We will use him for all edits and expansion of our website going forward. He was very helpful and clear with explaining the limits and capabilities of Squarespace. He used Loom to explain options to me which was incredibly helpful given my schedule. So happy with the outcome and will continue to use Kalana for our website updates and projects!"),
]

def img(path, fmt):
    # path is the part after /content/ ; add format sizing, strip any junk
    base = path.split("?")[0]
    return f"{CDN}/{base}?format={fmt}"

# Category labels used by the filter bar (slug -> label)
CATS = [
    ("all", "All work"),
    ("realestate", "Real Estate"),
    ("health", "Health & Wellness"),
    ("ecom", "eCommerce"),
    ("photo", "Photography & Video"),
    ("hospitality", "Travel & Hospitality"),
    ("business", "Professional Services"),
    ("beauty", "Beauty"),
    ("tech", "Tech & Apps"),
    ("entertainment", "Entertainment"),
    ("nonprofit", "Nonprofit"),
    ("convert", "HTML \u2192 Squarespace"),
]

# Each project. screenshot/hero are the path AFTER /content/  (no domain).
PROJECTS = [
    {
        "slug": "chemoclub",
        "title": "ChemoClub Squarespace Website",
        "client": "ChemoClub",
        "cat_slugs": ["health", "ecom"],
        "cat_label": "Health",
        "duration": "2 Days",
        "industry": "Health",
        "tech": ["Squarespace", "SEO", "Email"],
        "sub": "A fast-turnaround commerce and content build that gave ChemoClub one connected platform for products, stories and audience growth.",
        "overview": "ChemoClub needed more than a visual refresh. Its shop, podcast content and educational articles had to work together while the brand prepared for a time-sensitive launch. The challenge was delivering that broader customer journey without slowing the project down.",
        "solution_p": "Within 48 hours, I reorganised the Squarespace site around three clear destinations: the online store, podcast library and blog. I also completed the core SEO settings, introduced a promotional sign-up prompt and prepared an email campaign so the new experience could start attracting and retaining customers immediately.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/d54d89ef-a980-42fa-840a-f26125235afe/The+Chemo+Club+.jpg",
        "shot": "69cdfa4b7e96fb29aceec739/e010da53-f907-4add-a00a-172f2d5b01dc/screencapture-chemoclub-2025-04-27-12_05_47.png",
        "shot_url": "chemoclub",
    },
    {
        "slug": "complete-health-collective",
        "title": "Wellness Brand Redesign & WordPress Migration",
        "client": "Complete Health Collective",
        "cat_slugs": ["health"],
        "cat_label": "Wellness",
        "duration": "3 Weeks",
        "industry": "Wellness",
        "tech": ["Squarespace", "Migration"],
        "sub": "A cleaner wellness website and a carefully managed move from WordPress to an easier Squarespace setup.",
        "overview": "Complete Health Collective had outgrown a WordPress site whose structure and presentation no longer supported the brand. The migration needed to retain the useful material while making the experience simpler for visitors and easier for the team to maintain.",
        "solution_p": "I rebuilt the site in Squarespace with a fresh visual hierarchy, clearer page organisation and responsive layouts designed around the client\u2019s wellness positioning. Content was moved into a manageable system, navigation was simplified and each page was refined to feel consistent across desktop and mobile.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/c76f24cb-9c87-4c41-8774-353cc6adf4bc/198.png",
        "shot": "69cdfa4b7e96fb29aceec739/4459fcc7-d2f0-4cc6-a9c0-6d0eb49043a0/Artboard+73.png",
        "shot_url": "completehealthcollective",
    },
    {
        "slug": "destination-exploration-travel",
        "title": "Travel Agency Website Design & Development",
        "client": "Destination Exploration Travel",
        "cat_slugs": ["hospitality"],
        "cat_label": "Travel",
        "duration": "2 Weeks",
        "industry": "Travel",
        "tech": ["Squarespace", "Figma"],
        "sub": "A destination-led travel website that turns trip inspiration into qualified consultation enquiries.",
        "overview": "Destination Exploration Travel needed a professional home for its expertise, destinations and planning services. The key requirement was to help potential travellers explore ideas freely, then move naturally toward sharing their plans with the consultancy.",
        "solution_p": "I created a responsive Squarespace experience with reusable destination sections, an integrated travel journal and strategically placed enquiry forms. The content structure supports search visibility while the page flow guides visitors from discovering a destination to beginning the client onboarding process.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/478f77d8-f5a4-42ea-9ab6-2dc28afbe900/destinationexplorationtravel.jpg",
        "shot": "69cdfa4b7e96fb29aceec739/7cce7eca-4715-463e-88b8-ce96f3d8bccd/screencapture-destinationexplorationtravel-2026-04-15-14_13_17+%281%29.png",
        "shot_url": "destinationexplorationtravel",
    },
    {
        "slug": "pausitive-outlook",
        "title": "Squarespace Website for Cancer Survivors",
        "client": "Pausitive Outlook",
        "cat_slugs": ["health"],
        "cat_label": "Medical",
        "duration": "2 Weeks",
        "industry": "Medical",
        "tech": ["Squarespace", "Figma"],
        "sub": "An empathetic information hub that makes sensitive health guidance easier to find, understand and revisit.",
        "overview": "Pausitive Outlook supports cancer survivors dealing with medically induced menopause, but its growing library risked feeling dense at a time when visitors needed reassurance and clarity. The website had to organise important material without losing the warmth of the community behind it.",
        "solution_p": "I shaped the Squarespace build around calm pacing, clear topic groupings and mobile-first reading. A structured resource library helps visitors reach relevant guidance quickly, while newsletter pathways make it easier for the organisation to keep supporting its audience beyond a single visit.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/23673284-17e9-4d4f-9b8b-cf6b62f8bafd/1+hlf3.png",
        "shot": "69cdfa4b7e96fb29aceec739/4e9c403f-988b-4163-b433-a9bf330e4dea/screencapture-pausitiveoutlook-2026-04-12-16_43_14.png",
        "shot_url": "pausitiveoutlook",
    },
    {
        "slug": "flair-recruitment",
        "title": "Flair Recruitment \u2014 Branding, Logo & Website",
        "client": "Flair Recruitment LLC",
        "cat_slugs": ["business"],
        "cat_label": "Branding",
        "duration": "1 Week",
        "industry": "Human Resources",
        "tech": ["Squarespace", "Branding"],
        "sub": "A cohesive identity and website that positions a people-first recruitment business with clarity and confidence.",
        "overview": "Flair Recruitment was launching with strong values but without a finished visual identity or digital presence. The brand needed to speak equally well to employers, candidates and coaching clients while still feeling personal rather than corporate and impersonal.",
        "solution_p": "I developed the logo, brand direction and Squarespace website as one connected system. Warm visual choices, straightforward service pathways and responsive page layouts communicate connection, opportunity and trust while giving every audience a clear route to the information they need.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/b42f8681-27e5-437f-8f01-3d875d43b2a7/flairrecruitmentllc.jpg",
        "shot": "69cdfa4b7e96fb29aceec739/d6640628-5538-4bef-81d8-97da55bf741c/screencapture-flairrecruitmentllc-2026-04-12-22_31_40.png",
        "shot_url": "flairrecruitmentllc",
        "extra_shots": [
            "v1/69cdfa4b7e96fb29aceec739/b425bbc9-d58f-432f-86db-ffd33b814f7a/flairrecruitmentllc.jpg",
            "v1/69cdfa4b7e96fb29aceec739/9fd5d948-a5f8-4dac-8bf6-e758ab409243/flairrecruitmentllcflairrecruitflairrecruit.jpg",
        ],
    },
    {
        "slug": "curly-pineapples",
        "title": "Curly Pineapples \u2014 Beauty Homepage Revamp",
        "client": "Curly Pineapples Beauty",
        "cat_slugs": ["ecom", "beauty"],
        "cat_label": "eCommerce",
        "duration": "2 Weeks",
        "industry": "E-commerce",
        "tech": ["Squarespace", "Figma"],
        "sub": "A brighter, easier-to-shop homepage designed around the personality of a natural curly-hair brand.",
        "overview": "The Curly Pineapples had a lively product range, but the existing homepage did not communicate the brand energy or move shoppers smoothly toward its key collections. The redesign needed to improve the purchase journey without flattening the playful visual identity.",
        "solution_p": "I rebuilt the homepage hierarchy around product discovery, brand storytelling and clearer shopping prompts.",
        "solution_list": [
            ("Simpler shopping journey", "Reordered the content so visitors can understand the offer and reach featured products with fewer distractions."),
            ("Stronger brand expression", "Used colour, imagery and movement to better represent the natural, energetic character of the business."),
            ("Polished presentation", "Refined spacing, responsive behaviour and calls to action so the store feels more credible on every screen."),
        ],
        "hero": "v1/69cdfa4b7e96fb29aceec739/17092138-c09b-459c-86e8-d7456f158479/Curly+Pineapples.jpg",
        "shot": "69cdfa4b7e96fb29aceec739/ac291d67-6b6b-4f5b-9919-10b9af9cd521/screencapture-thecurlypineapples-2025-04-27-17_18_36.png",
        "shot_url": "thecurlypineapples",
    },
    {
        "slug": "abstract-insurance",
        "title": "Abstract Insurance \u2014 Luxury Web Presence",
        "client": "Abstract Insurance Brokerage",
        "cat_slugs": ["business"],
        "cat_label": "Insurance",
        "duration": "2 Weeks",
        "industry": "Insurance",
        "tech": ["Squarespace", "Figma"],
        "sub": "A restrained, high-trust digital presence for specialist insurance services and discerning private clients.",
        "overview": "Abstract Insurance Brokerage serves collectors, car enthusiasts and high-net-worth households whose expectations differ from a typical consumer-insurance audience. Its website needed to signal discretion and expertise immediately while explaining specialised coverage without unnecessary complexity.",
        "solution_p": "I designed a focused single-page Squarespace site with an editorial feel, measured typography and a deliberately limited visual palette. Services, coverage areas and the enquiry route are organised in a concise sequence that reinforces credibility and gives prospective clients a confident next step.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/79e9168a-59c2-4035-8667-fb4129a778bb/Abstract+Insurance+Brokerage+LLC.png",
        "shot": "69cdfa4b7e96fb29aceec739/3852248c-7870-466d-b81a-1f103e667731/screencapture-abstractins-2026-04-25-14_06_18+%281%29.png",
        "shot_url": "abstractins",
    },
    {
        "slug": "matter-co",
        "title": "Matter & Co \u2014 Premium Flooring eCommerce",
        "client": "Matter & Co",
        "cat_slugs": ["ecom"],
        "cat_label": "eCommerce",
        "duration": "3 Weeks",
        "industry": "E-Commerce",
        "tech": ["Squarespace", "Figma"],
        "sub": "A design-led materials store serving both trade professionals and homeowners across Canada.",
        "overview": "Matter & Co curates premium flooring, rugs and sustainable surfaces for residential and hospitality projects. The business needed one website that could feel credible to architects and developers while remaining clear and inviting for direct customers browsing products online.",
        "solution_p": "I built an editorial Squarespace Commerce experience with distinct collections for hardwoods, rugs and eco flooring. Project work, partner brands and sustainability information support product discovery, giving professional and consumer audiences the context they need before making an enquiry or purchase decision.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/125bb5dc-5955-4103-83eb-7c3b4d7436bc/Matter+%26+Co.png",
        "shot": "69cdfa4b7e96fb29aceec739/6791c9a2-edbc-43ef-9bd1-f66a319d12a8/screencapture-matterandco-ca-2026-04-25-15_04_14+%281%29.png",
        "shot_url": "matterandco.ca",
    },
    {
        "slug": "coastline-therapy",
        "title": "Coastline Therapy Group \u2014 Practice Website",
        "client": "Coastline Therapy Group",
        "cat_slugs": ["health"],
        "cat_label": "Wellness",
        "duration": "1 Week",
        "industry": "Wellness",
        "tech": ["Squarespace", "Figma"],
        "sub": "A reassuring practice website that helps therapy clients find the right support before making contact.",
        "overview": "Coastline Therapy Group offers trauma-informed care in Santa Barbara and by telehealth across California. The website needed to reduce uncertainty for potential clients while also communicating the practice\u2019s clinical depth, team culture and practical information such as fees and insurance.",
        "solution_p": "I organised the Squarespace site into clear routes for services, therapist profiles, costs, the client portal and careers. Soft visual styling makes the experience approachable, while concise navigation and responsive page templates keep essential information easy to reach during what can be a sensitive decision.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/900d990b-a223-4397-bdd0-74622d3b4819/coastlinetherapygroupsb.png",
        "shot": "69cdfa4b7e96fb29aceec739/a9a36abc-806a-4c77-a773-1064eafcc484/screencapture-coastlinetherapygroupsb-2026-04-25-15_21_34+%281%29.png",
        "shot_url": "coastlinetherapygroup",
    },
    {
        "slug": "gorgeous-gorgona",
        "title": "Gorgeous Gorgona \u2014 Luxury Nail Salon, NYC",
        "client": "Gorgeous Gorgona",
        "cat_slugs": ["beauty"],
        "cat_label": "Beauty",
        "duration": "1 Week",
        "industry": "Beauty, Wellness",
        "tech": ["Squarespace", "Figma"],
        "sub": "A fashion-forward salon website that pairs luxury positioning with a frictionless route to booking.",
        "overview": "Gorgeous Gorgona brings Russian manicure expertise and medical-grade standards to a Midtown Manhattan clientele. Its digital presence had to feel as considered as the in-studio experience while still answering practical questions for first-time guests.",
        "solution_p": "I translated the salon\u2019s bold art direction into a cinematic Squarespace build with artist profiles, trend galleries and detailed treatment pages. Gift cards, FAQs and booking access are woven into the experience so visitors can move from visual inspiration to an appointment without losing the premium atmosphere.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/724998f2-cd1a-4bf7-8f9b-de7587b50285/Gorgeous+Gorgona.webp",
        "shot": "69cdfa4b7e96fb29aceec739/4ae334f7-650b-4dcd-8a4d-0ffd5469a40f/screencapture-russiannails-2026-04-25-15_33_48.webp",
        "shot_url": "gorgeousgorgona",
    },
    {
        "slug": "fletcher-films",
        "title": "Fletcher Films \u2014 Wedding Videography",
        "client": "Fletcher Films",
        "cat_slugs": ["photo", "entertainment"],
        "cat_label": "Photography",
        "duration": "2 Weeks",
        "industry": "Photography, Videography",
        "tech": ["Squarespace"],
        "sub": "A quietly cinematic portfolio that lets wedding films create the emotion before the sales message begins.",
        "overview": "Fletcher Films has spent almost a decade documenting luxury weddings across the UK and Europe. The previous presentation needed to evolve into a refined portfolio capable of communicating both technical craft and the intimate feeling behind each film.",
        "solution_p": "I created a minimal Squarespace experience in which motion and imagery lead the story. Curated film collections, selected weddings, founder background and a focused availability form build confidence gradually, allowing couples to understand the style and enquire without visual noise.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/068c7a18-abda-46f8-802d-26e28edb072c/afletcherfilm.webp",
        "shot": "69cdfa4b7e96fb29aceec739/3b7991b8-e3a6-45c8-af99-47d8c897832b/screencapture-afletcherfilm-2026-04-25-15_46_18.webp",
        "shot_url": "fletcherfilms",
    },
    {
        "slug": "by-lena",
        "title": "By Lena \u2014 Photography Portfolio",
        "client": "By Lena",
        "cat_slugs": ["photo"],
        "cat_label": "Photography",
        "duration": "2 Weeks",
        "industry": "Photography, Videography",
        "tech": ["Squarespace"],
        "sub": "A personal, bilingual photography portfolio for attracting local and international commissions.",
        "overview": "Munich photographer and videographer Lena works across weddings, families, lifestyle, travel and analogue imagery. She needed a portfolio broad enough to show that range, yet personal enough that prospective clients could immediately recognise her warm, natural point of view.",
        "solution_p": "I gave each discipline its own image-led gallery while maintaining one consistent visual rhythm throughout the Squarespace site. German and English introductions, client feedback and a simple contact pathway support both local and international audiences without competing with the photography.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/e4e13495-3d4a-47cf-8bd3-b4f91ce20fe7/By+Lena.webp",
        "shot": "69cdfa4b7e96fb29aceec739/b6d3cf17-5275-4671-a3b2-8460136d8da5/screencapture-by-lena-2026-04-25-15_54_01.webp",
        "shot_url": "bylena",
    },
    {
        "slug": "gb-bible-app",
        "title": "+GB \u2014 AI-Powered Bible App Landing Page",
        "client": "+GB (The Good Book)",
        "cat_slugs": ["tech"],
        "cat_label": "Tech & Apps",
        "duration": "1 Week",
        "industry": "Tech & Apps",
        "tech": ["Squarespace"],
        "sub": "A focused product page that explains an AI Bible companion quickly and drives visitors to the app stores.",
        "overview": "+GB helps readers explore scripture through plain-language explanations, AI-assisted questions, multiple languages and family reading modes. With an established user base, the product needed a website that could communicate those capabilities quickly without burying the download action.",
        "solution_p": "I built a single-scroll Squarespace landing page around product education and conversion. Animated feature moments, a short usage sequence, testimonials and repeated store links take visitors from understanding the app to installing it, while the modern interface reflects the technology behind the experience.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/7a656f48-232a-4875-a8f8-b8d9c5a44f90/thegb.webp",
        "shot": "69cdfa4b7e96fb29aceec739/d4d81264-e924-4c9b-a1e8-80dfe7ea406b/screencapture-thegb-co-2026-04-30-00_01_17.webp",
        "shot_url": "thegb.co",
    },
    {
        "slug": "psych-science-hub",
        "title": "Psych Science Hub \u2014 Nonprofit Website",
        "client": "Psych Science Hub (CAAPS)",
        "cat_slugs": ["health", "nonprofit"],
        "cat_label": "Nonprofit",
        "duration": "1 Week",
        "industry": "Health & Wellness, Nonprofit",
        "tech": ["Squarespace", "Canva"],
        "sub": "An accessible public platform that turns psychological research into useful, trustworthy information.",
        "overview": "CAAPS needed Psych Science Hub to connect academic expertise with journalists and everyday readers seeking evidence-based mental-health guidance. The central challenge was making a large body of scientific material approachable without weakening its authority.",
        "solution_p": "I structured the Squarespace site around topic-led learning, an expert directory and human-centred researcher profiles. Supporting areas for articles, media connections and donations create a credible publishing platform that serves both the public and professionals while keeping the content easy to explore.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/d9d0ec17-61be-4366-95fc-aa4326b9f3b6/Psych+Science+Hub.webp",
        "shot": "69cdfa4b7e96fb29aceec739/0dfcb3bd-ae42-4ea9-9d4a-17befeee70aa/screencapture-psychsciencehub-2026-05-02-17_43_52.webp",
        "shot_url": "psychsciencehub",
    },
    {
        "slug": "pink-steak",
        "title": "Pink Steak \u2014 Luxury Steakhouse, West Palm Beach",
        "client": "Pink Steak",
        "cat_slugs": ["hospitality"],
        "cat_label": "Restaurant",
        "duration": "2 Weeks",
        "industry": "Food & Restaurant",
        "tech": ["Squarespace", "Figma"],
        "sub": "A vivid restaurant website that turns the venue\u2019s nightlife energy into reservations and event enquiries.",
        "overview": "Pink Steak combines premium cuts, raw-bar dishes and a strong cocktail programme in a theatrical West Palm Beach setting. Its website needed to sell the mood as convincingly as the menu while giving guests immediate access to the actions that matter.",
        "solution_p": "I designed a dark, high-impact Squarespace experience using dramatic imagery and confident pacing. Menus, OpenTable booking, private-event information and gift cards sit within the same visual story, helping prospective guests move directly from interest to a reservation or enquiry.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/6a8bc46e-cd3b-467d-9d6a-1d6d7587276c/pinksteak.webp",
        "shot": "69cdfa4b7e96fb29aceec739/7630d5e8-26e3-4005-9f2e-2d5c8ff25112/screencapture-pinksteak-2026-05-02-18_04_36.webp",
        "shot_url": "pinksteak",
    },
    {
        "slug": "xsight",
        "title": "XSiGHT Photography & Video \u2014 Portfolio",
        "client": "XSiGHT Photography & Video",
        "cat_slugs": ["photo"],
        "cat_label": "Photography",
        "duration": "6 Weeks",
        "industry": "Photography & Video",
        "tech": ["Squarespace", "Custom CSS"],
        "sub": "A media-rich portfolio engineered to showcase two decades of wedding photography without sacrificing performance.",
        "overview": "XSiGHT needed to modernise a long-established Melbourne wedding brand while preserving the timeless quality of its work. Large photo collections and cinematic reels had to feel immersive, but the experience also needed to remain stable and usable on smaller screens.",
        "solution_p": "I built a custom Squarespace gallery system that gives high-resolution imagery room to breathe and uses lightweight CSS in place of heavier scripts where possible. Responsive portfolio filters, streamlined navigation and on-page SEO create a faster exhibition-style experience that remains practical for real clients.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/11593737-4256-4e8a-b244-671b302f2a86/2.webp",
        "shot": "69cdfa4b7e96fb29aceec739/9f9333cf-928e-40b9-9b54-9c3f9e73a296/Artboard+1ssss.webp",
        "shot_url": "xsight",
    },
    {
        "slug": "html-to-squarespace",
        "title": "HTML & Mockup \u2192 Squarespace",
        "client": "Conversion projects",
        "cat_slugs": ["convert"],
        "cat_label": "Conversions",
        "duration": "Ongoing",
        "industry": "HTML / Figma \u2192 Squarespace",
        "tech": ["HTML", "Figma", "Squarespace"],
        "sub": "Client-supplied HTML and visual concepts translated into responsive Squarespace websites without losing the original design intent.",
        "is_convert": True,
        "hero": "static1/69cdfa4b7e96fb29aceec739/69d353a27f01e61adb48975e/6a168b045663dc31b00ad026/1780802515185/mockup-to-squarespace-dark-green.webp",
        "convert_items": [
            {
                "pj": "Project 01",
                "name": "Premier Medicare Planning",
                "desc": "Seven coded page concepts became one editable Squarespace website. I preserved the supplied visual system, rebuilt each layout responsively and incorporated the client\u2019s final refinements before launch.",
                "files": ["home.html", "Contact.html", "Medicare-Advantage.html", "Medicare-Supplement-Plans.html", "Part-D-Drug-Plans.html", "Turning-65.html", "Why-Us.html"],
                "mock": "https://kalanaheshanwa.github.io/client-mockups-projects/Premier%20Medicare%20Planning/home.html",
                "live": "https://www.premiermedicareplanning.com/",
            },
            {
                "pj": "Project 02",
                "name": "Muse MSC",
                "desc": "I converted a seven-page biotech HTML package into a manageable Squarespace build, retaining the information architecture, scientific content and key interactive behaviour across screen sizes.",
                "files": ["home.html", "Clinical-Evidence.html", "Contact-Us.html", "Mechanism-of-Action.html", "Publications-Overview.html", "The-Science.html", "Webinar-Registration.html"],
                "mock": "https://kalanaheshanwa.github.io/client-mockups-projects/muse-msc/home.html",
                "live": "https://www.musemsc.com/",
            },
            {
                "pj": "Project 03",
                "name": "Resurface Co.",
                "desc": "Starting from a single homepage image, I reconstructed the design language in Squarespace and extended it across the missing pages so the finished website felt intentionally designed as one system.",
                "files": [],
                "mock_img": "69cdfa4b7e96fb29aceec739/e06f30f3-fedc-451b-9bf3-d351a575e046/6A217C59-1281-4789-A815-4B62E12EE6F5.png",
                "mock": "https://kalanaheshanwa.github.io/client-mockups-projects/resurface/resurface-viewer.html",
                "live": "https://www.resurface.co/",
            },
            {
                "pj": "Project 04",
                "name": "Mouna Health",
                "desc": "A client-provided wellness concept was rebuilt and refined in Squarespace, with its premium visual direction preserved and the consultation journey simplified for real visitors.",
                "files": ["Threshold_Full_Mockup_16.html"],
                "mock": "https://kalanaheshanwa.github.io/client-mockups-projects/Mouna-Health/Threshold_Full_Mockup_16.html",
                "live": "https://www.mounahealth.com/",
            },
        ],
    },
    {
        "slug": "in-home-md",
        "title": "In-Home MD \u2014 Senior Primary Care",
        "client": "In-Home MD",
        "cat_slugs": ["health"],
        "cat_label": "Healthcare",
        "duration": "Multi-page",
        "industry": "Healthcare",
        "tech": ["Squarespace"],
        "sub": "A senior-friendly medical website that supports continuity of care and introduces an independent home-visit practice.",
        "overview": "In-Home MD was created by a trusted Memphis physician moving into independent practice. The website had to reassure existing patients through that transition, explain home-based primary care to new families and make every step understandable for an older audience.",
        "solution_p": "I designed a clear multi-page Squarespace site with separate journeys for current and prospective patients. Service explanations, physician credentials, testimonials and a carefully worded contact route build confidence, while larger type, simple navigation and responsive layouts improve usability for seniors and caregivers.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/f1e8d201-d478-49bd-af17-9725d6c01564/inhomemd-casestudy-1-cover.jpg",
        "shot": "69cdfa4b7e96fb29aceec739/4f09943e-e289-4e8e-93e9-c24973048ef9/screencapture-inhomemd-2026-06-11-21_48_55.webp",
        "shot_url": "inhomemd",
    },
    {
        "slug": "steeple-glenn",
        "title": "Steeple Glenn \u2014 Luxury 55+ Condominium Website",
        "client": "Steeple Glenn",
        "cat_slugs": ["realestate"],
        "cat_label": "Real Estate",
        "duration": "1 Week",
        "industry": "Real Estate",
        "tech": ["Squarespace", "Lovable"],
        "sub": "A sales-focused property site for a limited collection of move-in-ready homes aimed at active-adult buyers.",
        "overview": "Steeple Glenn had only nine luxury condominiums remaining in Newark, Delaware, alongside a time-sensitive upgrade incentive. The marketing website needed to communicate scarcity without feeling aggressive and give 55+ buyers enough detail to feel ready for a private tour.",
        "solution_p": "I built a single-page Squarespace sales experience that combines availability messaging with model details, amenities, finishes, interior photography and neighbourhood context. A valuation tool, FAQs and repeated contact prompts give serious prospects several natural points to request information or schedule a visit.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/56fea495-67ed-4ea3-b6d9-7316f207782a/steepleglennluxurycondos+1.png",
        "shot": "69cdfa4b7e96fb29aceec739/b796b030-5608-4b2e-b711-aa44881da53f/steepleglennluxurycondos+5.webp",
        "shot_url": "steepleglenn.com",
    },
    {
        "slug": "brand-your-journey",
        "title": "Brand Your Journey \u2014 Brand Strategy Consulting Website",
        "client": "Brand Your Journey",
        "cat_slugs": ["business", "convert"],
        "cat_label": "Consulting",
        "duration": "2 Weeks",
        "industry": "Business & Consulting",
        "tech": ["Squarespace", "Claude"],
        "sub": "A strategy-led consulting website that makes an intangible service easier for growing organisations to value.",
        "overview": "Brand Your Journey helps nonprofits, startups and smaller businesses sharpen their positioning, but many prospects do not initially recognise brand strategy as a business priority. The site therefore needed to educate, demonstrate relevance and create enough confidence for a consultation.",
        "solution_p": "I built the Squarespace journey around the problems caused by unclear branding, followed by a simple process and audience-specific explanations. The Strategy Room, client proof and a well-timed consultation invitation turn the website into both an educational resource and a lead-generation tool.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/8fb28972-6f96-4b54-93a7-fdb05e3be4c0/brandyourjourney-casestudy-2.png",
        "shot": "69cdfa4b7e96fb29aceec739/fa72e369-ea64-4760-ae4b-109327da149a/screencapture-brandyourjourney-2026-07-04-18_11_18.webp",
        "shot_url": "brandyourjourney.com",
    },
    {
        "slug": "nadia-sarmova",
        "title": "Nadia Sarmova \u2014 Hollywood Producer Personal Brand",
        "client": "Nadia Sarmova",
        "cat_slugs": ["photo", "entertainment", "convert"],
        "cat_label": "Film & Video",
        "duration": "2 Weeks",
        "industry": "Film & Videography",
        "tech": ["Squarespace", "HTML"],
        "sub": "A cinematic executive portfolio translated from custom HTML into a site the client can edit inside Squarespace.",
        "overview": "Producer, writer and social entrepreneur Nadia Sarmova needed a personal website that could connect her film work, company leadership and social-impact projects under one credible identity. The supplied designs were ambitious and had to be reproduced without leaving the client with a difficult-to-maintain site.",
        "solution_p": "I converted the provided HTML and image references into responsive Squarespace pages while retaining their cinematic character. Biography, credits, production ventures and impact work now form a polished portfolio that supports conversations with studios, collaborators and the press while remaining editable by the client.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/e96e8629-4cb1-4a0b-a328-09185807d102/nadiasarmova-casestudy-2-bento.png",
        "shot": "69cdfa4b7e96fb29aceec739/f48526c4-357e-45b4-b066-8665424d6973/screencapture-nadiasarmova-2026-07-11-06_37_10.webp",
        "shot_url": "nadiasarmova.com",
    },
    {
        "slug": "premier-medicare-planning",
        "title": "Premier Medicare Planning \u2014 Medicare Agency Website",
        "client": "Premier Medicare Planning",
        "cat_slugs": ["health", "convert"],
        "cat_label": "Healthcare",
        "duration": "2 Weeks",
        "industry": "Health & Consulting",
        "tech": ["Squarespace", "Claude"],
        "sub": "A clear Medicare education and lead-generation site reconstructed in Squarespace from the client\u2019s coded concepts.",
        "overview": "Premier Medicare Planning compares plans from more than 15 carriers for seniors in the Dayton area. Because Medicare choices can feel intimidating, the website had to reduce confusion, establish the agency\u2019s local expertise and make a no-cost consultation feel like a safe next step.",
        "solution_p": "I translated the client\u2019s HTML designs into a fully editable Squarespace site with dedicated guidance for Advantage, Supplement, Part D and Turning 65 decisions. A clear enrolment path, testimonials, educational articles and consultation prompts help visitors progress at their own pace before speaking with an adviser.",
        "hero": "69cdfa4b7e96fb29aceec739/ed893fff-dc31-43f0-b5a8-249ba7027fda/screencapture-premiermedicareplanning-2026-07-18-11_34_40.webp",
        "shot": "69cdfa4b7e96fb29aceec739/ed893fff-dc31-43f0-b5a8-249ba7027fda/screencapture-premiermedicareplanning-2026-07-18-11_34_40.webp",
        "shot_url": "premiermedicareplanning.com",
    },
    {
        "slug": "coffee-run-properties",
        "title": "Coffee Run Properties \u2014 Luxury Real Estate Landing Page",
        "client": "Coffee Run Properties",
        "cat_slugs": ["realestate"],
        "cat_label": "Real Estate",
        "duration": "1 Week",
        "industry": "Real Estate",
        "tech": ["Squarespace"],
        "sub": "A pre-sales website that presents a new luxury development as both a property opportunity and a lifestyle.",
        "overview": "Coffee Run was preparing to market 45 maintenance-free residences across a landscaped Hockessin site before sales momentum was established. Prospective buyers needed to understand the design, location and exclusivity of the development from digital material alone.",
        "solution_p": "I created a visual one-page Squarespace presentation combining lifestyle storytelling, amenities, floor plans, interior renderings and location highlights. Team and agent information adds credibility, while a focused enquiry flow converts early interest into qualified requests for private tours and pricing.",
        "hero": "69cdfa4b7e96fb29aceec739/42671792-494d-4f0e-b367-5736a8ef817f/full.webp",
        "shot": "69cdfa4b7e96fb29aceec739/42671792-494d-4f0e-b367-5736a8ef817f/full.webp",
        "shot_url": "coffeerunproperties.com",
    },
    {
        "slug": "lasata-90-broadway",
        "title": "LaSata at 90 Broadway \u2014 Property Marketing Website",
        "client": "N1 Real Estate Development",
        "cat_slugs": ["realestate"],
        "cat_label": "Real Estate",
        "duration": "2 Weeks",
        "industry": "Real Estate",
        "tech": ["Squarespace", "Lovable"],
        "sub": "One of four coordinated property websites created for N1 USA, balancing a distinct development identity with group-wide consistency.",
        "overview": "N1 USA required a digital presence for LaSata at 90 Broadway as part of a wider four-development portfolio. This project needed to stand on its own for prospective buyers while still feeling connected to the parent company and presenting residences, amenities, floor plans and availability without confusion.",
        "solution_p": "I created a mobile-responsive Squarespace marketing site with premium property imagery, well-structured development information and search-friendly copy. The enquiry journey is kept simple, while the underlying visual system allows LaSata to retain its own character and remain recognisably part of the broader N1 USA portfolio.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/e1d5375c-0f0d-4b23-8e72-85fb8cb759e6/LaSata+at+90+Broadway+website+showcase.webp",
        "shot": "69cdfa4b7e96fb29aceec739/49743dae-ad6c-49dc-b090-2e5b6c781e22/screencapture-lasata90broadway-2026-08-28-11_03_26.webp",
        "shot_url": "lasata90broadway.com",
    },
    {
        "slug": "creek-view-linwood",
        "title": "Creek View Linwood \u2014 Luxury Townhome Website",
        "client": "Creek View Linwood",
        "cat_slugs": ["realestate"],
        "cat_label": "Real Estate",
        "duration": "2 Weeks",
        "industry": "Real Estate",
        "tech": ["Squarespace", "Lovable"],
        "sub": "A refined property website for new townhomes with bay views and easy access to the Jersey Shore.",
        "overview": "Creek View Linwood needed to introduce a new residential development to buyers who would compare floor plans, finishes, location and lifestyle online before arranging a visit. The experience had to feel premium while keeping detailed property information easy to scan.",
        "solution_p": "I turned the supplied direction into a responsive Squarespace site led by large-scale photography and clear content sections. Floor-plan details, bay-view positioning, neighbourhood context and direct enquiry prompts work together to help prospects evaluate the development and confidently request pricing or a private tour.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/aa3860ef-ede1-4646-b727-08a6fe12a721/Creek+View+Linwood+%E2%80%93+Luxury+Real+Estate+Squarespace+Website+Development.webp",
        "shot": "69cdfa4b7e96fb29aceec739/3daa4c26-954c-473e-ab2c-7c3fa32188a7/screencapture-creekviewlinwood-2026-08-28-13_36_35.webp",
        "shot_url": "creekviewlinwood.com",
    },
    {
        "slug": "lassiebiome",
        "title": "LassieBiome \u2014 Pet Wellness Website & Booking Flow",
        "client": "LassieBiome",
        "cat_slugs": ["health"],
        "cat_label": "Pet Wellness",
        "duration": "2 Weeks",
        "industry": "Pet Care, Health & Wellness",
        "tech": ["Squarespace", "Calendly"],
        "sub": "A supplied wellness mockup developed into a responsive website with a more direct route to canine gut and skin consultations.",
        "overview": "LassieBiome arrived with a strong design concept but needed a production-ready website that dog owners could use comfortably on any device. Preserving the brand was important, yet the consultation pathway also needed to become clearer and easier to complete.",
        "solution_p": "I reproduced the mockup in Squarespace, refined responsive spacing and navigation, and connected Calendly to the booking journey. Visitors can now understand the gut-and-skin service, join early access or schedule a review through clearly separated actions, while the client retains an editable site for future growth.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/017b9eec-68e4-4853-9ca8-691053be2d97/ChatGPT+Image+Aug+28%2C+2026%2C+02_49_43+PM.webp",
        "shot": "69cdfa4b7e96fb29aceec739/2ec19c8c-747d-43ac-a195-a512a1036c03/screencapture-lassiebiome-2026-08-28-14_48_34.webp",
        "shot_url": "lassiebiome.com",
    },
    {
        "slug": "mouna-health",
        "title": "Mouna Health \u2014 Wellness Website & WhatsApp Consultations",
        "client": "Mouna Health",
        "cat_slugs": ["health", "convert"],
        "cat_label": "Wellness",
        "duration": "2 Weeks",
        "industry": "Health & Wellness",
        "tech": ["Squarespace", "HTML", "WhatsApp"],
        "sub": "A premium HTML concept rebuilt in Squarespace and adapted into a practical booking experience for in-person and online care.",
        "overview": "Mouna Health had a complete coded concept, but the final website needed to be editable, responsive and adjusted around real client feedback. The key risk was losing the calm, premium wellness direction while improving the imagery, page flow and consultation choices.",
        "solution_p": "I reconstructed the HTML design in Squarespace, refined individual sections and optimised the layouts for desktop and mobile. A dedicated booking page separates the two consultation options and routes each choice into WhatsApp, making it easier for visitors to contact the practitioner with the right context.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/a9897139-5976-4945-b0b9-71478d5b365e/ChatGPT+Image+Aug+28%2C+2026%2C+07_06_24+PM.webp",
        "shot": "69cdfa4b7e96fb29aceec739/4d0caf2c-0151-4543-b0ff-b00b433da377/screencapture-mounahealth-2026-08-28-15_15_44.webp",
        "shot_url": "mounahealth.com",
    },
    {
        "slug": "ridr-atx",
        "title": "RIDR ATX \u2014 DJ Backline & Event Support Website",
        "client": "RIDR ATX",
        "cat_slugs": ["entertainment"],
        "cat_label": "Entertainment",
        "duration": "1 Week",
        "industry": "Music & Entertainment",
        "tech": ["Squarespace"],
        "sub": "A bold service website for Austin promoters, touring DJs and production teams that need fast, reliable rider support.",
        "overview": "RIDR ATX offers backline, rider fulfilment and emergency event support within a specialist electronic-music market. The website had to explain several technical service types, coverage details and common questions without losing the underground character of the brand.",
        "solution_p": "I developed a high-contrast Squarespace site with a direct, industry-aware voice and a compact information hierarchy. Promoters and artists can quickly confirm available support, review the Austin service area, understand the process and submit the practical details RIDR ATX needs to respond efficiently.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/c4b51342-721c-44ca-99ba-e8f04c2ffeaa/RIDR+ATX+%E2%80%93+Squarespace+Website+Development+for+DJ+Backline+%26+Rider+Support.webp",
        "shot": "69cdfa4b7e96fb29aceec739/70c34768-af3c-4af3-82a4-40c6b3c7a595/screencapture-ridratx-2026-08-28-21_18_15.webp",
        "shot_url": "ridratx.com",
    },
    {
        "slug": "musemscs",
        "title": "MuseMSCs \u2014 Biotech Research Website",
        "client": "MuseMSCs",
        "cat_slugs": ["health", "tech", "convert"],
        "cat_label": "Biotechnology",
        "duration": "2 Weeks",
        "industry": "Healthcare & Biotechnology",
        "tech": ["Squarespace", "Custom CSS", "HTML"],
        "sub": "A scientific website that makes regenerative-medicine mechanisms, evidence and comparisons easier to navigate.",
        "overview": "MuseMSCs needed to communicate complex regenerative-medicine research to visitors with different levels of scientific knowledge. Clinical evidence, mechanisms of action, treatment comparisons and data visualisations all had to remain credible without turning the experience into an overwhelming research archive.",
        "solution_p": "Using the supplied HTML elements and content as a starting point, I organised the Squarespace build into progressive, readable sections. Responsive timelines, comparison layouts and custom graphs help visitors interpret the science, while consultation and webinar actions provide a logical next step for those ready to engage further.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/9f790c52-daea-4272-8b83-9fe4834f017a/Muse+Cells.webp",
        "shot": "69cdfa4b7e96fb29aceec739/9d7f56ca-2005-4961-9d6f-d5495fd1ef71/MuseMSCs+%E2%80%93+Biotech+Squarespace+Website+Development+with+Scientific+Graphs.webp",
        "shot_url": "musemsc.com",
    },
]

def hero_url(path, fmt):
    if path.startswith("static1/"):
        return f"https://static1.squarespace.com/static/{path[len('static1/'):]}?format={fmt}"
    return img(path, fmt)

E = html.escape

# ---------------- shared chrome ----------------
def topbar():
    return f"""<header class="topbar"><div class="wrap">
  <a class="brand" href="../index.html"><span class="mark"></span><b>Kalana&nbsp;Square</b><span>&nbsp;/ Work</span></a>
  <nav><a href="../index.html">All work</a><a class="nav-linkedin" href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="View Kalana Heshan on LinkedIn">{LINKEDIN_ICON}</a><a class="nav-hire" href="{UPWORK}" target="_blank" rel="noopener">Hire on Upwork&nbsp;\u2197</a></nav>
</div></header>"""

def topbar_index():
    return f"""<header class="topbar"><div class="wrap">
  <a class="brand" href="index.html"><span class="mark"></span><b>Kalana&nbsp;Square</b><span>&nbsp;/ Work</span></a>
  <nav aria-label="Primary navigation"><a href="#portfolio">Work</a><a href="#reviews">Reviews</a><a href="#process">Process</a><a href="#faq">FAQ</a><a href="#about">About</a><a class="nav-linkedin" href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="View Kalana Heshan on LinkedIn">{LINKEDIN_ICON}</a><a class="nav-hire" href="{UPWORK}" target="_blank" rel="noopener">Hire on Upwork&nbsp;\u2197</a><button class="nav-menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open navigation"><span></span><span></span></button></nav>
  <div class="mobile-nav" id="mobile-nav" hidden><a href="#portfolio">Work</a><a href="#reviews">Reviews</a><a href="#process">Process</a><a href="#faq">FAQ</a><a href="#about">About</a></div>
</div></header>"""

def footer(rel=""):
    return f"""<footer><div class="wrap">
  <a class="brand" href="{rel}index.html"><span class="mark"></span><b>Kalana&nbsp;Square</b></a>
  <div class="skills">
    <span class="t">Custom builds</span><span class="t">Redesigns</span><span class="t">eCommerce</span>
    <span class="t">Migrations</span><span class="t">SEO</span><span class="t">Custom code</span><span class="t">HTML&nbsp;\u2192&nbsp;Squarespace</span>
  </div>
  <div class="note">Squarespace Marketplace Expert &middot; Circle Member &middot; 450+ builds &middot; 7+ years</div>
</div></footer>"""

def head(title, desc, css_rel):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="robots" content="noindex">
<link rel="icon" href="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2032%2032'%3E%3Crect%20width='32'%20height='32'%20rx='8'%20fill='%2315151a'/%3E%3Crect%20x='11'%20y='11'%20width='10'%20height='10'%20rx='2.5'%20fill='none'%20stroke='%230ea47e'%20stroke-width='2.6'/%3E%3C/svg%3E">
<meta name="theme-color" content="#15151a">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css_rel}assets/styles.css">
</head>
<body>
<script>document.documentElement.className+=' js';</script>"""

# ---------------- index ----------------
def build_index():
    chips = ""
    for slug, label in CATS:
        pressed = "true" if slug == "all" else "false"
        chips += f'<button class="chip" data-cat="{slug}" aria-pressed="{pressed}">{E(label)}</button>'

    cards = ""
    for i, p in enumerate(PROJECTS, 1):
        cats = "|".join(p["cat_slugs"])
        href = f'projects/{p["slug"]}.html'
        cards += f"""
    <a class="card" href="{href}" data-cats="{cats}">
      <div class="thumb">
        <img loading="lazy" src="{hero_url(p['hero'],'900w')}" alt="{E(p['client'])} \u2014 Squarespace project cover">
        <span class="open"><span>View case</span></span>
      </div>
      <div class="body">
        <div class="meta-top"><span class="client">{E(p['client'])}</span><span class="cat">{E(p['cat_label'])}</span></div>
        <h3>{E(p['title'])}</h3>
      </div>
    </a>"""

    star = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l2.9 6.26 6.88.6-5.2 4.54 1.56 6.74L12 17.1 5.86 20.7l1.56-6.74-5.2-4.54 6.88-.6z"/></svg>'
    fivestars = star * 5
    def rev_card(name, date, price, title, quote):
        n = len(quote)
        if n < 90: size = "a"
        elif n < 170: size = "b"
        elif n < 250: size = "c"
        elif n < 340: size = "d"
        elif n < 430: size = "e"
        elif n < 520: size = "f"
        else: size = "g"
        return (f'<figure class="rev-card rw-{size}">'
                f'<div class="stars">{fivestars}</div>'
                f'<blockquote>{E(quote)}</blockquote>'
                f'<figcaption><div class="rev-name">{E(name)}</div>'
                f'<div class="rev-proj">{E(title)}</div>'
                f'<div class="rev-meta"><span class="rev-up">Upwork</span><span class="rev-dot">\u00b7</span><span>{E(date)}</span></div>'
                f'</figcaption></figure>')
    row1 = "".join(rev_card(*t) for i, t in enumerate(TESTIMONIALS) if i % 2 == 0)
    row2 = "".join(rev_card(*t) for i, t in enumerate(TESTIMONIALS) if i % 2 == 1)

    html_doc = head(
        "Work Catalogue \u2014 Kalana Square \u2014 Squarespace Design & Development",
        "Selected Squarespace website design and development work across health, wellness, eCommerce, photography, hospitality and tech. 450+ builds over 7+ years.",
        "",
    )
    html_doc += topbar_index()
    hv = lambda p: f'<a class="hv-card" href="#portfolio"><img loading="lazy" src="{hero_url(p["hero"],"640w")}" alt=""></a>'
    colA = "".join(hv(p) for p in PROJECTS[0::2])
    colB = "".join(hv(p) for p in PROJECTS[1::2])
    chk = '<svg viewBox="0 0 24 24" fill="none" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>'
    arw = '<svg viewBox="0 0 24 24" fill="none" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
    brand_items = "".join(f'<span class="blogo"><img src="{u}" alt="{E(n)}" loading="lazy"></span>' for n, u in LOGOS)
    badge_items = "".join(
        f'<a class="badge-link" href="{link}" target="_blank" rel="noopener" aria-label="View {E(n)} profile"><img class="badge-img" src="{u}" alt="{E(n)}" loading="lazy"></a>'
        if link else
        f'<span class="badge-link"><img class="badge-img" src="{u}" alt="{E(n)}" loading="lazy"></span>'
        for n, u, link in BADGES
    )
    html_doc += f"""
<section class="hero" id="work">
  <div class="glow"></div>
  <div class="grid-bg"></div>
  <div class="wrap">
    <div class="hero-grid">
      <div class="hero-text">
        <span class="eyebrow">Squarespace specialist \u00b7 Design &amp; development</span>
        <h1 class="display">Squarespace Projects I\u2019ve Built for Real Businesses</h1>
        <p class="lede">Browse a selection of real Squarespace projects from hundreds of websites I\u2019ve designed and built for businesses across different industries, including redesigns, migrations, eCommerce, and custom development.</p>
        <div class="cta-row">
          <a class="cta" href="#portfolio">Browse the work <span class="arr">\u2193</span></a>
          <a class="cta ghost" href="#services">What I build</a>
        </div>
        <div class="builton"><span class="bo-label">Built exclusively on</span><img src="{SQSP_LOGO}?format=300w" alt="Squarespace" loading="lazy"></div>
      </div>
      <div class="hero-visual" aria-hidden="true">
        <div class="hv-col hv-up">{colA}{colA}</div>
        <div class="hv-col hv-down">{colB}{colB}</div>
      </div>
    </div>
    <div class="stats">
      <div class="stat"><div class="n">450+</div><div class="l">Sites built</div></div>
      <div class="stat"><div class="n">230+</div><div class="l">Clients worldwide</div></div>
      <div class="stat"><div class="n">7+ yrs</div><div class="l">Squarespace focus</div></div>
      <div class="stat"><div class="n">Expert</div><div class="l">Marketplace + Circle</div></div>
    </div>
  </div>
</section>

<section class="badges"><div class="wrap">
  <div class="badge-row">{badge_items}</div>
</div></section>

<section class="brands">
  <div class="wrap brands-head">
    <span class="eyebrow">Partners</span>
    <h2 class="display">Some of the brands that trusted me</h2>
    <p>A few of the businesses and personal brands I\u2019ve built Squarespace websites for.</p>
  </div>
  <div class="brands-marquee"><div class="brands-track">{brand_items}{brand_items}</div></div>
</section>

<div class="toolbar" id="portfolio"><div class="wrap">
  <div class="filters">{chips}</div>
</div></div>

<main class="gallery"><div class="wrap">
  <div class="grid" id="grid">{cards}
  </div>
  <div class="empty" id="empty">No projects in this category yet.</div>
</div></main>

<section class="reviews" id="reviews">
  <div class="wrap rev-head">
    <span class="eyebrow">Client reviews</span>
    <h2 class="display">Loved by clients on Upwork</h2>
    <p>Real, unedited feedback from the people I\u2019ve designed and built Squarespace websites for.</p>
  </div>
  <div class="rev-marquee">
    <div class="rev-track rev-l">{row1}{row1}</div>
    <div class="rev-track rev-r">{row2}{row2}</div>
  </div>
</section>

<section class="services" id="services">
  <div class="wrap">
    <div class="svc-head">
      <span class="eyebrow">What I can do for you</span>
      <h2 class="display">Squarespace services for every stage of your website</h2>
      <p>Whatever your website needs, I handle it end to end \u2014 building a brand-new site, improving or moving an existing one, and getting you found on Google. It\u2019s all built on Squarespace, so it stays easy for you to update yourself.</p>
    </div>

    <div class="services-v2-wrap"><div class="bento-grid">

      <section class="v2c span-7 card-purple">
        <div class="split-card">
          <div class="split-left">
            <div class="card-top"><div class="icon"><svg viewBox="0 0 20 20" fill="none" stroke-width="1.8"><rect x="3" y="4" width="14" height="12" rx="2"/><path d="M3 8h14"/><path d="M7 12h6"/></svg></div></div>
            <h2 class="title">Custom Squarespace Web Design</h2>
            <p class="desc">Stop settling for generic templates. Get a high-performing, bespoke Squarespace website designed to rank on Google and convert visitors into loyal customers.</p>
            <div class="project-meta">
              <div class="meta-item"><div class="meta-label">Built On</div><div class="meta-val">Squarespace 7.1</div></div>
              <div class="meta-item"><div class="meta-label">Avg. Timeline</div><div class="meta-val">1 - 2 Weeks</div></div>
            </div>
            <a href="#portfolio" class="action-link">See related builds {arw}</a>
          </div>
          <div class="split-right"><div class="feature-box">
            <h3 class="inner-title">What's Included</h3>
            <div class="checklist">
              <div class="chk">{chk}<div>A signature design that mirrors your brand\u2019s premium value.</div></div>
              <div class="chk">{chk}<div>Engineered for visibility and ranking on Google search results.</div></div>
              <div class="chk">{chk}<div>Lightning-fast performance on every smartphone, tablet and screen.</div></div>
              <div class="chk">{chk}<div>Simple backend management with 1-on-1 training included.</div></div>
              <div class="chk">{chk}<div>Seamless connection of your domain, email and tracking.</div></div>
              <div class="chk">{chk}<div>Post-launch care to ensure your site stays flawless.</div></div>
            </div>
          </div></div>
        </div>
      </section>

      <section class="v2c span-5 card-green">
        <div class="card-top"><div class="icon"><svg viewBox="0 0 20 20" fill="none" stroke-width="1.8"><polyline points="4 16 10 10 14 14 20 6"/><polyline points="14 6 20 6 20 12"/></svg></div></div>
        <h2 class="title">SEO &amp; Performance</h2>
        <p class="desc">Get found by the right clients. I deeply optimise your technical structure, page speed and on-page content so your business ranks on page one.</p>
        <div class="checklist-2col">
          <div class="chk">{chk}<div>Advanced Keyword &amp; Competitor Research</div></div>
          <div class="chk">{chk}<div>Google Search Console &amp; Analytics Setup</div></div>
          <div class="chk">{chk}<div>Deep Meta Tag &amp; Image Alt Optimisation</div></div>
          <div class="chk">{chk}<div>Page Speed &amp; Core Web Vitals Audit</div></div>
          <div class="chk">{chk}<div>XML Sitemap &amp; Robots.txt Config</div></div>
          <div class="chk">{chk}<div>Monthly Performance Reporting</div></div>
        </div>
        <a href="#portfolio" class="action-link">Boost my rankings {arw}</a>
      </section>

      <section class="v2c span-5 card-peach">
        <div class="card-top"><div class="icon"><svg viewBox="0 0 20 20" fill="none" stroke-width="1.8"><path d="M3 6h14v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6z"/><path d="M3 6l2-3h10l2 3"/><path d="M8 10h4"/></svg></div></div>
        <h2 class="title">eCommerce Solutions</h2>
        <p class="desc">Premium Squarespace stores crafted specifically to sell. I optimise product pages, integrate payments smoothly and engineer a seamless checkout experience.</p>
        <div class="tags-row"><span class="tag">Payment Setup</span><span class="tag">Inventory Sync</span><span class="tag">UX Optimised</span></div>
      </section>

      <section class="v2c span-3 card-blue">
        <div class="card-top"><div class="icon"><svg viewBox="0 0 20 20" fill="none" stroke-width="1.8"><path d="M4 4h12v12H4z"/><path d="M7 8h6M7 11h4"/></svg></div></div>
        <h2 class="title">Redesign</h2>
        <p class="desc">Refresh your existing site with a modern look and flawless mobile layout.</p>
        <div class="ba-graphic">
          <div class="ba-col"><div class="ba-label before">Before</div><div class="ba-bar before"></div></div>
          <div class="ba-arrow">\u2192</div>
          <div class="ba-col"><div class="ba-label after">After</div><div class="ba-bar after"></div></div>
        </div>
      </section>

      <section class="v2c span-4 card-yellow">
        <div class="card-top"><div class="icon"><svg viewBox="0 0 20 20" fill="none" stroke-width="1.8"><path d="M4 16V8l6-5 6 5v8"/><path d="M8 16v-5h4v5"/></svg></div></div>
        <h2 class="title">Landing Pages</h2>
        <p class="desc">High-converting standalone pages engineered for ad campaigns or lead generation.</p>
        <div class="tags-row"><span class="tag">Lead Gen</span><span class="tag">Events</span></div>
      </section>

      <section class="v2c span-8 card-green">
        <div class="split-card">
          <div class="split-left">
            <div class="card-top"><div class="icon"><svg viewBox="0 0 20 20" fill="none" stroke-width="1.8"><path d="M10 2v16M2 10h16M4 4l12 12M4 16 16 4"/></svg></div></div>
            <h2 class="title">Maintenance &amp; Support</h2>
            <p class="desc">Your site is a living thing \u2014 it needs care. Monthly plans that keep everything fast, fresh and secure so you can focus on running your business.</p>
            <div class="tags-row"><span class="tag">Monthly retainer</span><span class="tag">Priority response</span><span class="tag">No contracts</span></div>
          </div>
          <div class="split-right"><div class="feature-box">
            <h3 class="inner-title">Plan includes</h3>
            <div class="checklist">
              <div class="chk">{chk}<div>Unlimited small content edits</div></div>
              <div class="chk">{chk}<div>Monthly speed &amp; SEO health check</div></div>
              <div class="chk">{chk}<div>Plugin &amp; platform updates</div></div>
              <div class="chk">{chk}<div>48-hour priority response guarantee</div></div>
            </div>
          </div></div>
        </div>
      </section>

      <section class="v2c span-4 card-gray">
        <div class="card-top"><div class="icon"><svg viewBox="0 0 20 20" fill="none" stroke-width="1.8"><path d="M4 4h6v6H4zM10 10h6v6h-6z"/><path d="M10 4h6M4 10v6"/></svg></div></div>
        <h2 class="title">Platform Migration</h2>
        <p class="desc">Seamless migrations from WordPress, Wix or Shopify into Squarespace \u2014 without losing a drop of your SEO juice.</p>
      </section>

      <section class="v2c span-12 card-blue">
        <div class="split-card">
          <div class="split-left">
            <div class="card-top"><div class="icon"><svg viewBox="0 0 20 20" fill="none" stroke-width="1.8"><path d="m7 6-4 4 4 4M13 6l4 4-4 4"/></svg></div></div>
            <h2 class="title">Your Design \u2192 Squarespace</h2>
            <p class="desc">Already have a mockup, image, PDF or HTML? I rebuild it in Squarespace \u2014 matched pixel-for-pixel, then made fully editable so you can manage it yourself.</p>
            <a href="#portfolio" class="action-link">See conversions {arw}</a>
          </div>
          <div class="split-right"><div class="feature-box">
            <h3 class="inner-title">How it works</h3>
            <div class="v2-flow">
              <div class="v2-step"><span class="v2-k">&lt;/&gt;</span> Your design, mockup or HTML</div>
              <div class="v2-arr">\u2193</div>
              <div class="v2-step"><span class="v2-ck">{chk}</span> Rebuilt in Squarespace</div>
              <div class="v2-arr">\u2193</div>
              <div class="v2-step v2-done"><span class="v2-dot"></span> Live &amp; editable by you</div>
            </div>
          </div></div>
        </div>
      </section>

    </div></div>
    <div class="svc-cta"><a class="cta" href="{UPWORK}" target="_blank" rel="noopener">Contact me on Upwork <span class="arr">\u2197</span></a></div>
  </div>
</section>

<section class="process" id="process"><div class="wrap">
  <div class="process-head">
    <span class="eyebrow">My process</span>
    <h2 class="display">How your Squarespace project moves forward</h2>
    <p>A structured five-stage workflow keeps decisions clear, feedback focused and your project moving confidently towards launch.</p>
  </div>
  <div class="process-card">
    <div class="process-top"><div class="process-current"><span id="process-current">1</span> / 5</div><div class="process-arrows"><button class="process-arrow process-prev" type="button" aria-label="Previous process step" disabled>&larr;</button><button class="process-arrow process-next" type="button" aria-label="Next process step">&rarr;</button></div></div>
    <div class="process-tabs" role="tablist" aria-label="Website project process">
      <button class="process-tab is-active" id="process-tab-1" role="tab" aria-selected="true" aria-controls="process-panel-1" tabindex="0" data-step="1"><span>01</span><b>Project Alignment</b></button>
      <button class="process-tab" id="process-tab-2" role="tab" aria-selected="false" aria-controls="process-panel-2" tabindex="-1" data-step="2"><span>02</span><b>Content &amp; Direction</b></button>
      <button class="process-tab" id="process-tab-3" role="tab" aria-selected="false" aria-controls="process-panel-3" tabindex="-1" data-step="3"><span>03</span><b>Squarespace Build</b></button>
      <button class="process-tab" id="process-tab-4" role="tab" aria-selected="false" aria-controls="process-panel-4" tabindex="-1" data-step="4"><span>04</span><b>Review &amp; Refine</b></button>
      <button class="process-tab" id="process-tab-5" role="tab" aria-selected="false" aria-controls="process-panel-5" tabindex="-1" data-step="5"><span>05</span><b>Launch &amp; Handover</b></button>
    </div>
    <div class="process-panels">
      <div class="process-panel is-active" id="process-panel-1" role="tabpanel" aria-labelledby="process-tab-1">
        <div class="process-left"><div class="process-bg-num" aria-hidden="true">01</div><div class="process-icon" aria-hidden="true">&#9671;</div><span class="process-kicker">Project alignment</span><h3>Turning your brief into a workable roadmap</h3><p>We start by clarifying what the website must achieve, who it needs to serve and which features matter most. I then translate those priorities into a practical plan for the build.</p><div class="process-tags"><span>Business goals</span><span>Audience</span><span>Priorities</span></div></div>
        <div class="process-right"><h4>You receive</h4><ul><li>Defined project scope</li><li>Recommended page list</li><li>Delivery schedule</li><li>Confirmed project cost</li></ul><div class="process-outcome"><span>&#10003;</span><div><small>In short</small><b>A shared plan before design begins</b></div></div></div>
      </div>
      <div class="process-panel" id="process-panel-2" role="tabpanel" aria-labelledby="process-tab-2" hidden>
        <div class="process-left"><div class="process-bg-num" aria-hidden="true">02</div><div class="process-icon" aria-hidden="true">&#9638;</div><span class="process-kicker">Content &amp; direction</span><h3>Preparing everything the website needs</h3><p>Your copy, imagery, branding and examples are organised into one clear system. If anything is missing, I identify it early and help shape a visual direction that fits your market.</p><div class="process-tags"><span>Content review</span><span>Brand assets</span><span>Visual direction</span></div></div>
        <div class="process-right"><h4>You receive</h4><ul><li>Content inventory</li><li>Organised brand assets</li><li>Reference direction</li><li>Missing-content checklist</li></ul><div class="process-outcome"><span>&#10003;</span><div><small>In short</small><b>Prepared assets and an agreed direction</b></div></div></div>
      </div>
      <div class="process-panel" id="process-panel-3" role="tabpanel" aria-labelledby="process-tab-3" hidden>
        <div class="process-left"><div class="process-bg-num" aria-hidden="true">03</div><div class="process-icon" aria-hidden="true">&lt;/&gt;</div><span class="process-kicker">Squarespace build</span><h3>Bringing the approved direction to life</h3><p>I build the pages directly in Squarespace, creating a consistent visual system and responsive layouts. Required integrations, eCommerce features and custom code are added as the site takes shape.</p><div class="process-tags"><span>Responsive design</span><span>Integrations</span><span>Custom code</span></div></div>
        <div class="process-right"><h4>You receive</h4><ul><li>Responsive page layouts</li><li>Reusable design system</li><li>Required integrations</li><li>Live review access</li></ul><div class="process-outcome"><span>&#10003;</span><div><small>In short</small><b>A working Squarespace site ready to review</b></div></div></div>
      </div>
      <div class="process-panel" id="process-panel-4" role="tabpanel" aria-labelledby="process-tab-4" hidden>
        <div class="process-left"><div class="process-bg-num" aria-hidden="true">04</div><div class="process-icon" aria-hidden="true">&#9998;</div><span class="process-kicker">Review &amp; refine</span><h3>Improving the details through focused feedback</h3><p>You review the live build and leave comments in one organised place. I work through the agreed changes, resolve layout issues and complete a final content and device check.</p><div class="process-tags"><span>Simple feedback</span><span>Revisions</span><span>Quality check</span></div></div>
        <div class="process-right"><h4>You receive</h4><ul><li>Commenting workspace</li><li>Agreed revision rounds</li><li>Cross-device refinements</li><li>Final content review</li></ul><div class="process-outcome"><span>&#10003;</span><div><small>In short</small><b>A polished website aligned with your feedback</b></div></div></div>
      </div>
      <div class="process-panel" id="process-panel-5" role="tabpanel" aria-labelledby="process-tab-5" hidden>
        <div class="process-left"><div class="process-bg-num" aria-hidden="true">05</div><div class="process-icon" aria-hidden="true">&#8599;</div><span class="process-kicker">Launch &amp; handover</span><h3>Going live with confidence</h3><p>Once approved, I connect the domain, test key journeys and complete the essential SEO and analytics setup. A personalised walkthrough makes day-to-day website management straightforward after launch.</p><div class="process-tags"><span>Launch checks</span><span>SEO setup</span><span>Training</span></div></div>
        <div class="process-right"><h4>You receive</h4><ul><li>Domain and form checks</li><li>Core SEO configuration</li><li>Training walkthrough</li><li>Six months of support</li></ul><div class="process-outcome"><span>&#10003;</span><div><small>In short</small><b>A live website you can manage confidently</b></div></div></div>
      </div>
    </div>
    <div class="process-pips" aria-hidden="true"><span class="is-active"></span><span></span><span></span><span></span><span></span></div>
  </div>
</div></section>

<section class="about" id="about"><div class="wrap">
  <div class="about-grid">
    <div class="about-photo">
      <img src="{PORTRAIT}?format=900w" alt="Kalana \u2014 Squarespace designer and developer" loading="lazy">
    </div>
    <div class="about-copy">
      <span class="eyebrow">About</span>
      <h2 class="display">Hello \u2014 I\u2019m Kalana, your Squarespace developer.</h2>
      <p>I\u2019m a Squarespace specialist with 7+ years of experience and 450+ completed builds for clients worldwide. I design and develop high-performing, SEO-optimised sites end to end \u2014 custom builds, redesigns, eCommerce stores, platform migrations, and pixel-perfect Figma-to-Squarespace development, plus custom code when the platform needs to go further.</p>
      <p>As an official Squarespace Circle member and Marketplace Expert, I deliver clean, fast, client-focused results \u2014 and every project ships with a walkthrough so you can manage your own site with confidence.</p>
      <div class="creds">
        <span class="cred">Top Rated on Upwork</span>
        <span class="cred">Top Rated on Fiverr</span>
        <span class="cred">Squarespace Marketplace Expert</span>
        <span class="cred">Circle Platinum Member</span>
        <span class="cred">7+ years \u00b7 450+ builds</span>
      </div>
      <a class="about-linkedin" href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="Connect with Kalana Heshan on LinkedIn">{LINKEDIN_ICON}</a>
    </div>
  </div>
</div></section>

<section class="faq" id="faq"><div class="wrap">
  <div class="faq-grid">
    <div class="faq-head">
      <span class="eyebrow">Frequently asked questions</span>
      <h2 class="display">Questions before we start</h2>
      <p>Quick answers about working with me on your Squarespace project.</p>
    </div>
    <div class="faq-list">
      <details open><summary>What types of Squarespace projects do you handle?<span aria-hidden="true"></span></summary><p>I design new Squarespace websites, redesign existing sites, migrate websites from other platforms, build eCommerce and booking features, and develop custom layouts using CSS and code.</p></details>
      <details><summary>Can you redesign my existing website without losing its content?<span aria-hidden="true"></span></summary><p>Yes. I can preserve your important pages, text, images and brand identity while improving the website's design, navigation, mobile experience and overall performance.</p></details>
      <details><summary>Can you migrate my website to Squarespace?<span aria-hidden="true"></span></summary><p>Yes. I regularly migrate websites from WordPress, Wix, Google Sites and other platforms to Squarespace while maintaining the existing content and improving the structure where needed.</p></details>
      <details><summary>Can you build from Figma, HTML or a design mockup?<span aria-hidden="true"></span></summary><p>Yes. I can accurately recreate approved designs, Figma layouts, HTML concepts or reference websites in Squarespace and make them responsive across desktop, tablet and mobile devices.</p></details>
      <details><summary>How long does a Squarespace project take?<span aria-hidden="true"></span></summary><p>A standard website usually takes one to three weeks, depending on the number of pages, features and how quickly content and feedback are provided. Smaller updates and landing pages can often be completed sooner.</p></details>
      <details><summary>Do I need to have all my content ready before we start?<span aria-hidden="true"></span></summary><p>Not necessarily. We can begin with the available content, and I can help organise it into a clear website structure. Final text, images and business information should be supplied before launch.</p></details>
      <details><summary>Will my website work properly on mobile devices?<span aria-hidden="true"></span></summary><p>Yes. Every website is tested and optimised for desktop, tablet and mobile screens. I also review navigation, spacing, image presentation and button usability on smaller devices.</p></details>
      <details><summary>Do you provide support after the website is launched?<span aria-hidden="true"></span></summary><p>Yes. I provide six months of support after launch for questions and minor technical issues related to the completed work. I can also provide ongoing maintenance when required.</p></details>
      <details><summary>How will we manage the project through Upwork?<span aria-hidden="true"></span></summary><p>All communication, milestones, payments and project delivery can remain securely within Upwork. I provide clear progress updates and give you opportunities to review the website throughout the project.</p></details>
    </div>
  </div>
</div></section>

<section class="hire" id="hire"><div class="wrap">
  <div class="hire-card">
    <div class="hire-glow"></div>
    <div class="hire-inner">
      <span class="hire-status"><span class="dot"></span>Available for work \u00b7 Top Rated on Upwork</span>
      <h2 class="display">Have a Squarespace project in mind?</h2>
      <p>If you\u2019re hiring on Upwork, let\u2019s turn your job post into a fast, beautiful, conversion-ready Squarespace site. Send the brief and I\u2019ll reply with a clear plan, timeline and fixed price.</p>
      <div class="hire-cta">
        <a class="cta cta-lg" href="{UPWORK}" target="_blank" rel="noopener">Hire me on Upwork <span class="arr2">\u2197</span></a>
      </div>
    </div>
  </div>
</div></section>
"""
    html_doc += footer("")
    html_doc += '\n<button class="totop" id="totop" aria-label="Back to top"><span>\u2191</span></button>'
    html_doc += '\n<script src="assets/app.js"></script>\n</body></html>'
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_doc)

# ---------------- project page ----------------
def specs(p):
    rows = [("Client", p["client"]), ("Industry", p["industry"]),
            ("Timeline", p["duration"]), ("Built on", "Squarespace")]
    cells = "".join(f'<div class="spec"><div class="k">{E(k)}</div><div class="v">{E(v)}</div></div>' for k, v in rows)
    return f'<div class="specs">{cells}</div>'

def solution_block(p):
    out = '<div class="block"><h2>Solution</h2>'
    out += f'<p>{E(p["solution_p"])}</p>'
    if p.get("solution_list"):
        out += "<ul>"
        for b, t in p["solution_list"]:
            out += f'<li><b>{E(b)}:</b> {E(t)}</li>'
        out += "</ul>"
    out += "</div>"
    return out

def convert_section(p):
    out = '<section class="conv"><div class="wrap">'
    for it in p["convert_items"]:
        files = "".join(f'<span class="f">{E(fn)}</span>' for fn in it["files"])
        files_html = f'<div class="files">{files}</div>' if files else ""
        links = ""
        if it.get("mock"):
            links += f'<a class="btn ghost" href="{it["mock"]}" target="_blank" rel="noopener">Original mockup</a>'
        if it.get("live"):
            links += f'<a class="btn" href="{it["live"]}" target="_blank" rel="noopener">Live Squarespace site</a>'
        mock_img = ""
        if it.get("mock_img"):
            mock_img = f'''<div class="conv-mock">
  <div class="conv-mock-bar"><span class="conv-dots"><i></i><i></i><i></i></span><span>Client homepage mockup</span><span>Scroll to preview</span></div>
  <div class="conv-mock-scroll"><img loading="lazy" src="{img(it["mock_img"],"1200w")}" alt="{E(it["name"])} client mockup"></div>
</div>'''
        out += f"""<div class="conv-item">
  <div class="top"><div><div class="pj">{E(it['pj'])}</div><h3>{E(it['name'])}</h3></div></div>
  <p>{E(it['desc'])}</p>
  {files_html}
{mock_img}
  <div class="links">{links}</div>
</div>"""
    out += "</div></section>"
    return out

def preview_section(p):
    # multiple stacked images (e.g. flair) or single tall scroll shot
    name = E(p["client"])
    if p.get("extra_shots"):
        imgs = f'<img loading="lazy" src="{img(p["shot"],"2200w")}" alt="{name} full site screenshot">'
        for ex in p["extra_shots"]:
            imgs += f'<img loading="lazy" src="{hero_url(ex,"1600w")}" alt="{name} brand asset">'
        return f"""<section class="preview"><div class="wrap">
  <div class="label"><span class="eyebrow">Live preview</span><span class="hint">Click to enlarge</span></div>
  <div class="shot" data-zoom="{img(p['shot'],'2500w')}" data-name="{name} \u2014 live site">
    <div class="bar"><i></i><i></i><i></i><span class="url">{E(p.get('shot_url',''))}</span><span class="z">\u2922 zoom</span></div>
    <div class="scroller">{imgs}</div>
  </div>
</div></section>"""
    return f"""<section class="preview"><div class="wrap">
  <div class="label"><span class="eyebrow">Live preview</span><span class="hint">Scroll inside the frame \u00b7 click to enlarge</span></div>
  <div class="shot" data-zoom="{img(p['shot'],'2500w')}" data-name="{name} \u2014 live site">
    <div class="bar"><i></i><i></i><i></i><span class="url">{E(p.get('shot_url',''))}</span><span class="z">\u2922 zoom</span></div>
    <div class="scroller"><img loading="lazy" src="{img(p['shot'],'2200w')}" alt="{name} full website screenshot"></div>
  </div>
</div></section>"""

def pager(idx):
    prev_a = next_a = ""
    if idx > 0:
        pp = PROJECTS[idx-1]
        prev_a = f'<a class="prev" href="{pp["slug"]}.html"><span class="dir">\u2190 Prev</span><span class="ttl">{E(pp["title"])}</span></a>'
    else:
        prev_a = '<a class="prev disabled"><span class="dir">\u2190 Prev</span><span class="ttl">\u2014</span></a>'
    if idx < len(PROJECTS)-1:
        np = PROJECTS[idx+1]
        next_a = f'<a class="next" href="{np["slug"]}.html"><span class="dir">Next \u2192</span><span class="ttl">{E(np["title"])}</span></a>'
    else:
        next_a = '<a class="next disabled"><span class="dir">Next \u2192</span><span class="ttl">\u2014</span></a>'
    return f'<nav class="pager">{prev_a}{next_a}</nav>'

def lightbox():
    return """<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Full screenshot">
  <div class="lbbar"><span class="nm"></span><button class="x" aria-label="Close">\u2715</button></div>
  <div class="lbscroll"><img alt="Full website screenshot"></div>
</div>"""

def build_project(idx, p):
    doc = head(f'{p["title"]} \u2014 Kalana Square',
               p["sub"], "../")
    doc += topbar()
    doc += f"""
<section class="proj-head"><div class="wrap">
  <div class="crumbs"><a href="../index.html">Work</a><span class="sep">/</span><span>{E(p['cat_label'])}</span><span class="sep">/</span><span>{idx+1:02d}</span></div>
  <h1 class="proj-title display">{E(p['title'])}</h1>
  <p class="proj-sub">{E(p['sub'])}</p>
  {specs(p)}
</div></section>
"""
    if p.get("is_convert"):
        doc += convert_section(p)
    else:
        doc += f"""<section class="proj-body"><div class="wrap"><div class="two-col">
  <div class="block"><h2>Overview</h2><p>{E(p['overview'])}</p></div>
  {solution_block(p)}
</div></div></section>"""
        doc += preview_section(p)

    if p.get("feedback"):
        fb = p["feedback"]
        star = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l2.9 6.26 6.88.6-5.2 4.54 1.56 6.74L12 17.1 5.86 20.7l1.56-6.74-5.2-4.54 6.88-.6z"/></svg>'
        meta = f'<span class="rev-up">Upwork</span>'
        if fb.get("date"):
            meta += f'<span class="rev-dot">\u00b7</span><span>{E(fb["date"])}</span>'
        doc += f"""<section class="proj-fb"><div class="wrap">
  <figure class="fb-card">
    <div class="stars">{star*5}</div>
    <blockquote>{E(fb['text'])}</blockquote>
    <figcaption><div class="rev-name">{E(fb.get('name','Verified client'))}</div><div class="rev-meta">{meta}</div></figcaption>
  </figure>
</div></section>"""

    doc += pager(idx)
    doc += footer("../")
    doc += lightbox()
    doc += '\n<script src="../assets/app.js"></script>\n</body></html>'
    with open(f"projects/{p['slug']}.html", "w", encoding="utf-8") as f:
        f.write(doc)

def main():
    build_index()
    for i, p in enumerate(PROJECTS):
        build_project(i, p)
    print(f"Built index.html + {len(PROJECTS)} project pages.")

if __name__ == "__main__":
    main()
