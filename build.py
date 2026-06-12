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

TESTIMONIALS = [
    ("Lucy Hargrave", "May 2026", "Kalana built a complete Squarespace website from our style guide and template. He completed the project quickly and implemented every change with ease. Would highly recommend."),
    ("Ana Valdez Curiel", "Apr 2026", "Extremely attentive and helpful \u2014 he did the design exactly to my liking. I would work with him over and over again for his professionalism, quick responses and knowledge."),
    ("Gordon Allott", "Mar 2026", "Super professional with a very fast turnaround. Kalana is a Squarespace guru \u2014 he pulled the whole website together in no time and filled in the grey areas brilliantly."),
    ("Christopher Stear", "Feb 2026", "Very professional and easy to work with. Outstanding attention to detail, and he delivered every high-quality milestone ahead of schedule. A pleasure from start to finish."),
    ("Jennifer Kim", "Jan 2026", "From start to finish he showed exceptional skill in website design and communication. I\u2019m very pleased with how the whole project turned out and will be back for the next one."),
    ("Sarah Talbo", "Dec 2025", "Kalana built my website from the ground up. He was patient, worked at my pace and really listened to my brand vision. Highly recommended to anyone needing a Squarespace site!"),
]

def img(path, fmt):
    # path is the part after /content/ ; add format sizing, strip any junk
    base = path.split("?")[0]
    return f"{CDN}/{base}?format={fmt}"

# Category labels used by the filter bar (slug -> label)
CATS = [
    ("all", "All work"),
    ("health", "Health & Wellness"),
    ("ecom", "eCommerce"),
    ("photo", "Photography & Video"),
    ("hospitality", "Hospitality"),
    ("business", "Business & Branding"),
    ("tech", "Tech & Apps"),
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
        "sub": "A 48-hour, end-to-end Squarespace overhaul \u2014 store, podcast hub and blog \u2014 built to accelerate a fast-growing health brand.",
        "overview": "I revamped ChemoClub\u2019s Squarespace site by building an online store, podcast page and blog. I handled full SEO setup, designed a promotional pop-up to drive engagement, and launched an email campaign for customer outreach \u2014 all delivered under a tight 48-hour turnaround to support their rapid growth goals.",
        "solution_p": "Delivered a rapid, end-to-end Squarespace overhaul in under 48 hours. I transformed their digital presence with a fully integrated e-commerce store, a dedicated podcast hub and an active blog. To maximise immediate visibility and retention, the launch included full-site SEO optimisation, a lead-generating promotional pop-up and a strategic email outreach campaign.",
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
        "sub": "A full redesign and rebuild on Squarespace, migrated cleanly off WordPress with a sharper layout and structure.",
        "overview": "Redesigned and rebuilt the entire website in Squarespace after migrating it from WordPress \u2014 improving layout, structure and overall user experience.",
        "solution_p": "I fully redesigned and rebuilt this wellness-focused website on Squarespace, migrating it from WordPress while improving its layout, structure and user experience. The new site reflects a clean, professional design tailored to the client\u2019s brand, with mobile responsiveness and intuitive navigation throughout.",
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
        "sub": "A fully responsive Squarespace site for a Florida travel consultancy, built around custom destination modules and lead capture.",
        "overview": "A fully responsive Squarespace site built for a Florida-based travel consultancy. Key features include customised destination modules, an integrated blog and optimised lead-capture forms that streamline the client onboarding process.",
        "solution_p": "Designed a fully responsive, visually engaging Squarespace website tailored for a Florida-based travel consultancy. I developed custom destination modules that showcase travel packages alongside an integrated blog to drive organic traffic. To prioritise conversions, the site features strategically optimised lead-capture forms that streamline the journey from inspiration to inquiry.",
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
        "sub": "A calming, high-end resource hub for survivors navigating medically induced menopause \u2014 structured for clarity and comfort.",
        "overview": "For Pausitive Outlook I transformed a complex resource hub into a streamlined, high-end Squarespace experience. The focus was a calming user journey for survivors navigating medically induced menopause: a custom-structured resource library, integrated newsletter growth tools and a mobile-first responsive layout that keeps critical medical information both accessible and visually comforting.",
        "solution_p": "Transformed a complex medical resource hub into a streamlined Squarespace experience built around an empathetic, calming user journey. I developed a custom-structured resource library that makes critical information easy to find without feeling overwhelming, pairing a visually comforting, mobile-first design with integrated newsletter tools to support ongoing audience growth and community connection.",
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
        "sub": "Brand identity, logo and a full Squarespace site for a human-centred recruitment & coaching service.",
        "overview": "I created the brand identity, logo and full Squarespace website for Flair Recruitment LLC, a human-centred recruitment & coaching service. The project delivers a polished digital presence \u2014 professional aesthetics with clarity, intuitive navigation, responsive layouts and a cohesive visual style guide reflecting the company\u2019s values of connection, opportunity and trust.",
        "solution_p": "Delivered a complete brand identity and digital presence. To reflect their human-centred approach I designed a custom logo and cohesive visual style guide rooted in connection, opportunity and trust, then translated that brand into a full Squarespace website \u2014 prioritising professional aesthetics, intuitive navigation and fully responsive layouts for a polished, frictionless client experience.",
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
        "cat_slugs": ["ecom"],
        "cat_label": "eCommerce",
        "duration": "2 Weeks",
        "industry": "E-commerce",
        "tech": ["Squarespace", "Figma"],
        "sub": "A modern, conversion-focused homepage redesign for a vibrant natural beauty brand.",
        "overview": "I led the redesign of The Curly Pineapples\u2019 Squarespace homepage, creating a more modern, engaging and conversion-focused layout for their beauty product brand. The focus was enhancing visual storytelling, improving user flow and aligning the design with the brand\u2019s vibrant, natural aesthetic.",
        "solution_p": "Delivered a comprehensive Squarespace homepage overhaul focused on modern aesthetics and increased conversions.",
        "solution_list": [
            ("Conversion-driven layout", "Restructured the user flow into a seamless, intuitive path to purchase for their e-commerce customers."),
            ("Visual storytelling", "Highlighted the brand\u2019s vibrant, natural aesthetic through dynamic design elements."),
            ("Modernised experience", "Upgraded the interface to reflect the premium quality of their curly haircare accessories and keep visitors engaged."),
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
        "sub": "A refined, single-page presence for a boutique firm serving high-net-worth clients, collectors and private clientele.",
        "overview": "Abstract Insurance Brokerage LLC is a boutique firm specialising in tailored coverage for high-net-worth individuals, art collectors, car enthusiasts and private clients. They needed a website that reflected the sophistication of their clientele \u2014 refined, trustworthy and distinct from standard insurance brands.",
        "solution_p": "Designed and developed a custom Squarespace website with a luxury aesthetic that communicates credibility and exclusivity. The site features a clean single-page layout with structured sections covering services, coverage highlights and a contact form \u2014 all crafted to resonate with a discerning, high-end audience. Visual direction centred on elegance and restraint, letting the brand speak with authority.",
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
        "sub": "An editorial e-commerce build for a Toronto material curation studio serving designers, developers and hospitality projects.",
        "overview": "Matter & Co is a Toronto-based material curation studio serving designers, developers and hospitality projects across Canada. They needed a sophisticated e-commerce site that could showcase premium hardwood flooring, designer rugs and eco-friendly surfaces \u2014 while positioning them as a high-end B2B and B2C brand.",
        "solution_p": "Built a fully custom Squarespace e-commerce website with a clean, editorial aesthetic that reflects the brand\u2019s premium positioning. The site features a structured product store across multiple categories (Hardwoods, Rugs, Eco Flooring), a project portfolio section, brand showcase and sustainability-focused content \u2014 designed to serve both trade professionals and direct consumers with confidence.",
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
        "sub": "A warm, multi-page site for a trauma-focused therapy practice balancing approachability with clinical credibility.",
        "overview": "Coastline Therapy Group is a trauma-focused therapy practice in Santa Barbara, California, offering in-person and telehealth services statewide. They needed a warm, welcoming website that builds trust with potential clients while clearly communicating their services, team and approach to mental health care.",
        "solution_p": "Designed and developed a calming, professional Squarespace website that balances approachability with clinical credibility. The multi-page structure covers therapist profiles, service listings, insurance & cost information, a client-portal integration, blog and a careers page \u2014 giving both new clients and prospective therapists everything they need in one cohesive, easy-to-navigate experience.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/900d990b-a223-4397-bdd0-74622d3b4819/coastlinetherapygroupsb.png",
        "shot": "69cdfa4b7e96fb29aceec739/a9a36abc-806a-4c77-a773-1064eafcc484/screencapture-coastlinetherapygroupsb-2026-04-25-15_21_34+%281%29.png",
        "shot_url": "coastlinetherapygroup",
    },
    {
        "slug": "gorgeous-gorgona",
        "title": "Gorgeous Gorgona \u2014 Luxury Nail Salon, NYC",
        "client": "Gorgeous Gorgona",
        "cat_slugs": ["health", "business"],
        "cat_label": "Beauty",
        "duration": "1 Week",
        "industry": "Beauty, Wellness",
        "tech": ["Squarespace", "Figma"],
        "sub": "A bold, editorial site for a premium Russian manicure studio in Midtown Manhattan with celebrity clientele.",
        "overview": "Gorgeous Gorgona is a premium Russian manicure studio in Midtown Manhattan, known for medical-grade standards, celebrity clientele and an elevated salon experience. They needed a website that matched the sophistication of the brand \u2014 bold, editorial and unmistakably high-end.",
        "solution_p": "Designed and developed a visually striking Squarespace website with a luxury brand identity at its core. The site features individual artist profiles, a curated trend-collections gallery, detailed service pages, an FAQ section, gift-card sales and a seamless booking integration \u2014 all crafted to reflect the salon\u2019s premium positioning and convert first-time visitors into loyal clients.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/724998f2-cd1a-4bf7-8f9b-de7587b50285/Gorgeous+Gorgona.webp",
        "shot": "69cdfa4b7e96fb29aceec739/4ae334f7-650b-4dcd-8a4d-0ffd5469a40f/screencapture-russiannails-2026-04-25-15_33_48.webp",
        "shot_url": "gorgeousgorgona",
    },
    {
        "slug": "fletcher-films",
        "title": "Fletcher Films \u2014 Wedding Videography",
        "client": "Fletcher Films",
        "cat_slugs": ["photo"],
        "cat_label": "Photography",
        "duration": "2 Weeks",
        "industry": "Photography, Videography",
        "tech": ["Squarespace"],
        "sub": "A cinematic, editorial site for a UK luxury wedding videographer \u2014 built to let the films take centre stage.",
        "overview": "Fletcher Films is a UK-based luxury wedding videography brand with nearly a decade of experience filming across the UK, Europe and beyond. They needed a refined, cinematic website that reflected the emotional storytelling at the heart of their work \u2014 not just showcasing weddings, but capturing the feeling of them.",
        "solution_p": "Designed and developed an elegant Squarespace website with a minimal, editorial aesthetic that lets the films take centre stage. The site features a curated wedding-films gallery, a weddings showcase, an about page and a contact/availability form \u2014 all crafted to evoke emotion, build trust and convert high-end couples into inquiries.",
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
        "sub": "A warm, image-first bilingual portfolio for a Munich photographer and videographer.",
        "overview": "By Lena is a Munich-based photographer and videographer specialising in weddings, family, lifestyle, travel and analog photography. She needed a warm, personal portfolio that felt as natural and authentic as her photography style \u2014 one that would attract clients across Germany and internationally.",
        "solution_p": "Designed and developed a clean, image-first Squarespace portfolio that puts Lena\u2019s photography front and centre. The site features separate gallery sections for each photography niche, a bilingual about section (German & English), client testimonials and a contact form \u2014 all wrapped in a warm, approachable aesthetic that reflects her personal brand.",
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
        "sub": "A high-converting landing page for an AI Bible app with 50K+ users and a 5-star App Store rating.",
        "overview": "+GB (The Good Book) is an AI-powered Bible app on iOS and Android, making scripture more accessible through verse-by-verse explanations, an AI chat assistant, multi-language support and family-friendly reading modes. With 50K+ users and a 5-star App Store rating, they needed a high-converting landing page that clearly communicated the app\u2019s value and drove downloads.",
        "solution_p": "Designed and developed a sleek, app-focused Squarespace landing page with a bold, modern aesthetic built to convert. The page features an animated feature showcase, a step-by-step how-it-works section, social proof with testimonials, app-store download CTAs and a contact section \u2014 all structured to guide visitors from curiosity to download in a single scroll.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/7a656f48-232a-4875-a8f8-b8d9c5a44f90/thegb.webp",
        "shot": "69cdfa4b7e96fb29aceec739/d4d81264-e924-4c9b-a1e8-80dfe7ea406b/screencapture-thegb-co-2026-04-30-00_01_17.webp",
        "shot_url": "thegb.co",
    },
    {
        "slug": "psych-science-hub",
        "title": "Psych Science Hub \u2014 Nonprofit Website",
        "client": "Psych Science Hub (CAAPS)",
        "cat_slugs": ["health"],
        "cat_label": "Nonprofit",
        "duration": "1 Week",
        "industry": "Health & Wellness, Nonprofit",
        "tech": ["Squarespace", "Canva"],
        "sub": "A credible, accessible platform bridging academic psychology and the public, for a coalition of leading organisations.",
        "overview": "Psych Science Hub is the public-facing platform for CAAPS (Coalition for the Advancement and Application of Psychological Science) \u2014 a coalition of leading professional psychology organisations. They needed a credible, accessible website that bridges the gap between academic psychological research and everyday people seeking trustworthy mental-health information.",
        "solution_p": "Designed and developed a clean, authoritative Squarespace website that balances scientific credibility with approachability. The site features an expert directory for media connections, a science content hub organised by mental-health topics, behind-the-scenes researcher profiles, a blog and a donation section \u2014 all structured to position CAAPS as the go-to trusted source for evidence-based mental-health information.",
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
        "sub": "A dark, atmospheric restaurant site where Miami energy meets Palm Beach elegance.",
        "overview": "Pink Steak is a modern luxury steakhouse in West Palm Beach, Florida, offering an upscale experience with A5 Wagyu, caviar, raw-bar selections and a vibrant cocktail program. They needed a bold, atmospheric website that captured the restaurant\u2019s unique personality \u2014 where Miami energy meets Palm Beach elegance.",
        "solution_p": "Designed and developed a visually striking Squarespace restaurant website with a dark, seductive aesthetic that mirrors the dining experience. The site features a full menu showcase with downloadable PDFs, OpenTable reservation integration, a private-events section, gift-card sales and a contact section \u2014 all crafted to entice visitors and convert them into reservations.",
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
        "sub": "A premium, distraction-free digital exhibition for a Melbourne studio with a 20+ year legacy.",
        "overview": "With a 20+ year legacy of capturing unscripted, beautiful wedding stories in Melbourne, XSiGHT needed a digital re-imagining. I designed and developed a high-end Squarespace website to match their signature artistry \u2014 classic, premium and distraction-free \u2014 functioning as a live digital exhibition of multi-tier image galleries and cinematic film showreels.",
        "solution_p": "I engineered a custom, visually immersive Squarespace layout tailored for high-resolution media while prioritising speed and stability. By replacing bulky JavaScript with lightweight CSS for smoother navigation and using advanced flex-wrap styling so portfolio filters stay flawlessly responsive on mobile, I delivered a seamless digital exhibition backed by robust on-page SEO.",
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
        "sub": "Already have a design? I take exactly what you have \u2014 developer HTML files or designer mockups \u2014 and build it pixel-accurate into a Squarespace site you can manage yourself.",
        "is_convert": True,
        "hero": "static1/69cdfa4b7e96fb29aceec739/69d353a27f01e61adb48975e/6a168b045663dc31b00ad026/1780802515185/mockup-to-squarespace-dark-green.webp",
        "convert_items": [
            {
                "pj": "Project 01",
                "name": "Premier Medicare Planning",
                "desc": "Client provided 7 HTML files \u2014 one per page. I rebuilt the full site in Squarespace matching their design exactly, then refined details based on their feedback.",
                "files": ["home.html", "Contact.html", "Medicare-Advantage.html", "Medicare-Supplement-Plans.html", "Part-D-Drug-Plans.html", "Turning-65.html", "Why-Us.html"],
                "mock": "https://kalanaheshanwa.github.io/client-mockups-projects/Premier%20Medicare%20Planning/home.html",
                "live": "https://www.premiermedicareplanning.com/",
            },
            {
                "pj": "Project 02",
                "name": "Muse MSC",
                "desc": "Client provided 7 HTML files covering their full site structure. Rebuilt in Squarespace with all pages, interactions and content intact.",
                "files": ["home.html", "Clinical-Evidence.html", "Contact-Us.html", "Mechanism-of-Action.html", "Publications-Overview.html", "The-Science.html", "Webinar-Registration.html"],
                "mock": "https://kalanaheshanwa.github.io/client-mockups-projects/muse-msc/home.html",
                "live": "https://www.musemsc.com/",
            },
            {
                "pj": "Project 03",
                "name": "Resurface Co.",
                "desc": "Client had only one homepage image \u2014 no other pages designed. I matched the style across the full site, creating every additional page from scratch in Squarespace.",
                "files": [],
                "mock_img": "69cdfa4b7e96fb29aceec739/e06f30f3-fedc-451b-9bf3-d351a575e046/6A217C59-1281-4789-A815-4B62E12EE6F5.png",
                "live": "https://www.resurface.co/",
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
        "sub": "A compassionate, multi-page site for a Memphis practice delivering primary care to seniors in their homes.",
        "overview": "In-Home MD is a Memphis-based independent medical practice delivering personalised primary care directly to seniors and older adults in their homes. Operated by a trusted physician moving to independent practice, they needed a professional, compassionate website to reassure existing patients and attract new ones \u2014 clearly communicating services, credibility and how to get started.",
        "solution_p": "Built a full multi-page Squarespace website with a clean, trustworthy aesthetic tailored to a senior healthcare audience. The site features dedicated pages for current patients (continuity of care), new patients (onboarding flow), a comprehensive services breakdown, a physician about page, testimonials and a HIPAA-conscious contact section \u2014 all structured to build confidence and convert both returning and first-time patients.",
        "hero": "v1/69cdfa4b7e96fb29aceec739/f1e8d201-d478-49bd-af17-9725d6c01564/inhomemd-casestudy-1-cover.jpg",
        "shot": "69cdfa4b7e96fb29aceec739/4f09943e-e289-4e8e-93e9-c24973048ef9/screencapture-inhomemd-2026-06-11-21_48_55.webp",
        "shot_url": "inhomemd",
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
  <nav><a href="../index.html">All work</a><a class="nav-hire" href="{UPWORK}" target="_blank" rel="noopener">Hire on Upwork&nbsp;\u2197</a></nav>
</div></header>"""

def topbar_index():
    return f"""<header class="topbar"><div class="wrap">
  <a class="brand" href="index.html"><span class="mark"></span><b>Kalana&nbsp;Square</b><span>&nbsp;/ Work</span></a>
  <nav><a href="#portfolio">Work</a><a href="#reviews">Reviews</a><a href="#about">About</a><a class="nav-hire" href="{UPWORK}" target="_blank" rel="noopener">Hire on Upwork&nbsp;\u2197</a></nav>
</div></header>"""

def footer(rel=""):
    return f"""<footer><div class="wrap">
  <a class="brand" href="{rel}index.html"><span class="mark"></span><b>Kalana&nbsp;Square</b></a>
  <div class="skills">
    <span class="t">Custom builds</span><span class="t">Redesigns</span><span class="t">eCommerce</span>
    <span class="t">Migrations</span><span class="t">SEO</span><span class="t">Custom code</span><span class="t">HTML&nbsp;\u2192&nbsp;Squarespace</span>
  </div>
  <div class="note">Squarespace Marketplace Expert &middot; Circle Member &middot; 350+ builds &middot; 7+ years</div>
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
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
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
    stars = '<div class="stars">' + star * 5 + '</div>'
    def rev_card(name, date, quote):
        n = len(quote)
        size = "s" if n < 130 else ("m" if n < 175 else "l")
        return (f'<figure class="rev-card rsz-{size}">{stars}'
                f'<blockquote>{E(quote)}</blockquote>'
                f'<figcaption><div class="rev-name">{E(name)}</div>'
                f'<div class="rev-meta"><span class="rev-up">Upwork</span><span class="rev-dot">\u00b7</span><span>{E(date)}</span></div>'
                f'</figcaption></figure>')
    row1 = "".join(rev_card(*t) for t in TESTIMONIALS)
    row2 = "".join(rev_card(*t) for t in reversed(TESTIMONIALS))

    html_doc = head(
        "Work Catalogue \u2014 Kalana Square \u2014 Squarespace Design & Development",
        "Selected Squarespace website design and development work across health, wellness, eCommerce, photography, hospitality and tech. 350+ builds over 7+ years.",
        "",
    )
    html_doc += topbar_index()
    hv = lambda p: f'<div class="hv-card"><img loading="lazy" src="{hero_url(p["hero"],"640w")}" alt=""></div>'
    colA = "".join(hv(p) for p in PROJECTS[0::2])
    colB = "".join(hv(p) for p in PROJECTS[1::2])
    html_doc += f"""
<section class="hero" id="work">
  <div class="glow"></div>
  <div class="grid-bg"></div>
  <div class="wrap">
    <div class="hero-grid">
      <div class="hero-text">
        <span class="eyebrow">Squarespace specialist \u00b7 Design &amp; development</span>
        <h1 class="display">Squarespace websites that look sharp and <span class="u">actually perform.</span></h1>
        <p class="lede">I design and build Squarespace websites from start to finish \u2014 whether you\u2019re starting fresh, refreshing a dated site, or rebuilding a design you already have. Everything below is real client work, made to look great, load fast, and stay easy for you to update yourself.</p>
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
      <div class="stat"><div class="n">350+</div><div class="l">Sites built</div></div>
      <div class="stat"><div class="n">230+</div><div class="l">Clients worldwide</div></div>
      <div class="stat"><div class="n">7+ yrs</div><div class="l">Squarespace focus</div></div>
      <div class="stat"><div class="n">Expert</div><div class="l">Marketplace + Circle</div></div>
    </div>
  </div>
</section>

<section class="services" id="services">
  <div class="wrap">
    <div class="svc-head">
      <span class="eyebrow">What I can do for you</span>
      <p>Whatever your website needs, I handle it end to end \u2014 building a brand-new site, improving or moving an existing one, and getting you found on Google. It\u2019s all built on Squarespace, so it stays easy for you to update yourself.</p>
    </div>

    <div class="bento">
      <a class="bx bx-design" href="#portfolio">
        <div class="bx-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 9v12"/></svg></div>
        <div class="bx-grow"></div>
        <h3>Custom website design</h3>
        <p>A premium, made-from-scratch Squarespace site built around your brand \u2014 fast, responsive and ready to turn visitors into customers. The flagship service most clients come for.</p>
        <div class="bx-chips"><span>Squarespace 7.1</span><span>Mobile-perfect</span><span>Edit it yourself</span></div>
        <span class="bx-arr">\u2192</span>
      </a>

      <a class="bx bx-seo" href="#portfolio">
        <div class="bx-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 17l5-5 4 4 8-8"/><path d="M16 8h5v5"/></svg></div>
        <span class="bx-tag">Most requested</span>
        <h3>Get found on Google</h3>
        <p>Built SEO-first so you rank \u2014 plus standalone audits &amp; optimisation for sites that already exist.</p>
        <div class="bx-chips"><span>Keywords</span><span>Speed</span><span>Search Console</span><span>Schema</span></div>
      </a>

      <a class="bx bx-ecom" href="#portfolio">
        <div class="bx-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18M16 10a4 4 0 0 1-8 0"/></svg></div>
        <h3>Online stores</h3>
        <p>Products, checkout and digital downloads that actually sell.</p>
      </a>

      <a class="bx bx-migrate" href="#portfolio">
        <div class="bx-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8h13M14 5l3 3-3 3"/><path d="M20 16H7m3 3-3-3 3-3"/></svg></div>
        <h3>Move to Squarespace</h3>
        <p>Switch from WordPress, Wix or GoDaddy \u2014 nothing lost.</p>
      </a>

      <a class="bx bx-html" href="#portfolio">
        <div class="bx-html-text">
          <div class="bx-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m8 6-6 6 6 6M16 6l6 6-6 6"/></svg></div>
          <h3>Your design \u2192 Squarespace</h3>
          <p>Have a mockup, image or HTML? I rebuild it in Squarespace, matched exactly \u2014 pixel for pixel.</p>
        </div>
        <div class="bx-slide" aria-hidden="true">
          <div class="sl sl-a"><span class="sl-k">&lt;/&gt;</span> Your design</div>
          <div class="sl-arrow">\u2192</div>
          <div class="sl sl-b"><span class="sl-dot"></span> Live on Squarespace</div>
        </div>
      </a>

      <a class="bx bx-redesign" href="#portfolio">
        <div class="bx-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-2.64-6.36"/><path d="M21 3v5h-5"/></svg></div>
        <h3>Redesign my old site</h3>
        <p>Turn a dated, messy site into something modern and credible.</p>
      </a>

      <a class="bx bx-maintain" href="#portfolio">
        <div class="bx-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/></svg></div>
        <h3>Care &amp; support</h3>
        <p>Ongoing edits, updates and monthly health checks.</p>
      </a>
    </div>
    <div class="svc-cta"><a class="cta" href="#portfolio">See all projects <span class="arr">\u2193</span></a></div>
  </div>
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
    <h2 class="display">Trusted by 230+ clients worldwide</h2>
    <p>Real feedback from clients I\u2019ve designed and built Squarespace websites for.</p>
  </div>
  <div class="rev-marquee">
    <div class="rev-track rev-l">{row1}{row1}</div>
    <div class="rev-track rev-r">{row2}{row2}</div>
  </div>
</section>

<section class="about" id="about"><div class="wrap">
  <div class="about-grid">
    <div class="about-photo">
      <img src="{PORTRAIT}?format=900w" alt="Kalana \u2014 Squarespace designer and developer" loading="lazy">
    </div>
    <div class="about-copy">
      <span class="eyebrow">About</span>
      <h2 class="display">Hello \u2014 I\u2019m Kalana, your Squarespace developer.</h2>
      <p>I\u2019m a Squarespace specialist with 7+ years of experience and 350+ completed builds for clients worldwide. I design and develop high-performing, SEO-optimised sites end to end \u2014 custom builds, redesigns, eCommerce stores, platform migrations, and pixel-perfect Figma-to-Squarespace development, plus custom code when the platform needs to go further.</p>
      <p>As an official Squarespace Circle member and Marketplace Expert, I deliver clean, fast, client-focused results \u2014 and every project ships with a walkthrough so you can manage your own site with confidence.</p>
      <div class="creds">
        <span class="cred">Top Rated on Upwork</span>
        <span class="cred">Top Rated on Fiverr</span>
        <span class="cred">Squarespace Marketplace Expert</span>
        <span class="cred">Circle Platinum Member</span>
        <span class="cred">7+ years \u00b7 350+ builds</span>
      </div>
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
        <a class="cta ghost cta-lg" href="#portfolio">Revisit the work</a>
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
            mock_img = f'<div class="conv-mock"><img loading="lazy" src="{img(it["mock_img"],"1200w")}" alt="{E(it["name"])} client mockup"></div>'
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
