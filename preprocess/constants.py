# Indian states and union territories
STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", 
    "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", 
    "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
    "Uttarakhand", "West Bengal"
]

UNION_TERRITORIES = [
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu", 
    "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"
]

# Solar vendor organization names
SOLAR_ORGANIZATIONS = [
    "SunTech Solar Solutions", "GreenEnergy Systems", "SolarPeak Innovations", "BrightSun Power",
    "EcoSolar Enterprises", "RadiantSun Energy", "InfiniteLight Solar", "PowerSun Technologies",
    "SunRise Renewable Solutions", "GreenRay Solar Systems", "SkyPower Solar", "SunWave Energy",
    "EcoPower Solar", "SunBeam Energy Solutions", "SolarEdge Systems", "IlluminateSun Technologies",
    "SolarHarvest Energy", "SunVolt Power", "GreenSpark Solar", "SolarCrest Enterprises"
]

DISCOM_NAMES = [
    "Adani Electricity Mumbai Limited",
    "Ajmer Vidyut Vitran Nigam Ltd",
    "Andhra Pradesh Eastern Power Distribution Company Limited",
    "Andhra Pradesh Central Power Distribution Company Limited",
    "Andhra Pradesh Southern Power Distribution Company Limited",
    "Assam Power Distribution Company Limited (APDCL)",
    "Bangalore Electricity Supply Company Limited (BESCOM)",
    "Brihanmumbai Electric Supply and Transport (BEST)",
    "BSES Rajdhani Power Limited, Delhi",
    "BSES Yamuna Power Limited, Delhi",
    "Calcutta Electric Supply Corporation (CESC)",
    "Chamundeshwari Electricity Supply Corporation Limited (CESC Mysore)",
    "Dakshin Gujarat Vij Company Limited (DGVCL), Surat",
    "Dakshin Haryana Bijli Vitran Nigam (DHBVN)",
    "Damodar Valley Corporation (DVC)",
    "Essel Vidyut Vitran Ujjain Pvt. Ltd.",
    "Goa Electricity Department",
    "Gulbarga Electricity Supply Company Limited (GESCOM)",
    "Hubli Electricity Supply Company Limited (HESCOM)",
    "India Power Corporation Limited",
    "Jaipur Vidyut Vitran Nigam Limited (JVVNL)",
    "Jodhpur Vidyut Vitran Nigam Limited (JdVVNL)",
    "Karnataka Power Corporation Limited (KPCL)",
    "Kerala State Electricity Board (KSEB)",
    "Madhya Pradesh Paschim Kshetra Vidyut Vitaran Company Limited",
    "Madhya Pradesh Poorv Kshetra Vidyut Vitaran Company Limited",
    "Madhya Pradesh Madhya Kshetra Vidyut Vitaran Company Limited",
    "Madhya Gujarat Vij Company Limited (MGVCL), Vadodara",
    "Maharashtra State Electricity Distribution Company Limited (MSEDCL)",
    "Mangalore Electricity Supply Company Limited (MESCOM)",
    "Manipur State Power Distribution Company Limited (MSPDCL)",
    "National Thermal Power Corporation (NTPC)",
    "Neyveli Lignite Corporation (NLC)",
    "North Eastern Electricity Supply Company of Odisha Ltd (NESCO)",
    "Noida Power Company Limited (NPCL)",
    "North Bihar Power Distribution Company Limited (NBPDCL)",
    "Paschim Gujarat Vij Company Limited (PGVCL), Rajkot",
    "Power Development Department, Jammu & Kashmir",
    "PowerGrid Corporation of India",
    "Punjab State Power Corporation Limited (PSPCL)",
    "Reliance Infrastructure",
    "South Bihar Power Distribution Company Limited (SBPDCL)",
    "Southern Electricity Supply Company of Odisha (SOUTHCO)",
    "Tamil Nadu Generation and Distribution Corporation Limited (TANGEDCO)",
    "Tata Power",
    "Tata Power Delhi Distribution Limited (TPDDL), Delhi",
    "Northern Power Distribution Company of Telangana Limited (TSNPDCL)",
    "Southern Power Distribution Company of Telangana Limited (TSSPDCL)",
    "Torrent Power Limited",
    "Torrent Power Limited, Agra",
    "Torrent Power Limited, Ahmedabad",
    "Torrent Power Limited, Surat",
    "Tripura State Electricity Corporation Limited (TSECL)",
    "Uttar Gujarat Vij Company Limited (UGVCL), Mehsana",
    "Uttar Haryana Bijli Vitran Nigam Limited (UHBVN)",
    "Uttar Pradesh Power Corporation Limited (UPPCL)",
    "Dakshinanchal Vidyut Vitaran Nigam Limited (DVVNL), Agra Zone",
    "Kanpur Electricity Supply Company (KESCO), Kanpur City",
    "Lucknow Electricity Supply Administration (LESA), Lucknow City",
    "Madhyanchal Vidyut Vitaran Nigam Limited (MVVNL), Lucknow Zone",
    "Pashchimanchal Vidyut Vitaran Nigam Limited (PVVNL), Meerut Zone"
]

# Add DISCOM to State Mapping: 
STATE_DISCOM_MAP = {
    "Maharashtra": ["Adani Electricity Mumbai Limited", "Brihanmumbai Electric Supply and Transport (BEST)", "Maharashtra State Electricity Distribution Company Limited (MSEDCL)", "Tata Power"],
    "Gujarat": ["Dakshin Gujarat Vij Company Limited (DGVCL), Surat", "Madhya Gujarat Vij Company Limited (MGVCL), Vadodara", "Paschim Gujarat Vij Company Limited (PGVCL), Rajkot", "Torrent Power Limited, Ahmedabad", "Uttar Gujarat Vij Company Limited (UGVCL), Mehsana"],
    "Rajasthan": ["Ajmer Vidyut Vitran Nigam Ltd", "Jaipur Vidyut Vitran Nigam Limited (JVVNL)", "Jodhpur Vidyut Vitran Nigam Limited (JdVVNL)"],
    "Andhra Pradesh": ["Andhra Pradesh Eastern Power Distribution Company Limited", "Andhra Pradesh Central Power Distribution Company Limited", "Andhra Pradesh Southern Power Distribution Company Limited"],
    "Tamil Nadu": ["Tamil Nadu Generation and Distribution Corporation Limited (TANGEDCO)"],
    "Karnataka": ["Bangalore Electricity Supply Company Limited (BESCOM)", "Chamundeshwari Electricity Supply Corporation Limited (CESC Mysore)", "Gulbarga Electricity Supply Company Limited (GESCOM)", "Hubli Electricity Supply Company Limited (HESCOM)", "Mangalore Electricity Supply Company Limited (MESCOM)", "Karnataka Power Corporation Limited (KPCL)"],
    "Telangana": ["Northern Power Distribution Company of Telangana Limited (TSNPDCL)", "Southern Power Distribution Company of Telangana Limited (TSSPDCL)"],
    "Uttar Pradesh": ["Uttar Pradesh Power Corporation Limited (UPPCL)", "Dakshinanchal Vidyut Vitaran Nigam Limited (DVVNL), Agra Zone", "Kanpur Electricity Supply Company (KESCO), Kanpur City", "Lucknow Electricity Supply Administration (LESA), Lucknow City", "Madhyanchal Vidyut Vitaran Nigam Limited (MVVNL), Lucknow Zone", "Pashchimanchal Vidyut Vitran Nigam Limited (PVVNL), Meerut Zone", "Torrent Power Limited, Agra"],
    "Delhi": ["BSES Rajdhani Power Limited, Delhi", "BSES Yamuna Power Limited, Delhi", "Tata Power Delhi Distribution Limited (TPDDL), Delhi"],
    "Haryana": ["Dakshin Haryana Bijli Vitran Nigam (DHBVN)", "Uttar Haryana Bijli Vitran Nigam Limited (UHBVN)"],
    "Punjab": ["Punjab State Power Corporation Limited (PSPCL)"],
    "Kerala": ["Kerala State Electricity Board (KSEB)"],
    "Odisha": ["North Eastern Electricity Supply Company of Odisha Ltd (NESCO)", "Southern Electricity Supply Company of Odisha (SOUTHCO)"],
    "Madhya Pradesh": ["Madhya Pradesh Paschim Kshetra Vidyut Vitaran Company Limited", "Madhya Pradesh Poorv Kshetra Vidyut Vitaran Company Limited", "Madhya Pradesh Madhya Kshetra Vidyut Vitaran Company Limited", "Essel Vidyut Vitran Ujjain Pvt. Ltd."],
    "Bihar": ["North Bihar Power Distribution Company Limited (NBPDCL)", "South Bihar Power Distribution Company Limited (SBPDCL)"],
    "Assam": ["Assam Power Distribution Company Limited (APDCL)"],
    "West Bengal": ["Calcutta Electric Supply Corporation (CESC)", "Damodar Valley Corporation (DVC)", "India Power Corporation Limited"],
    "Chhattisgarh": [],
    "Goa": ["Goa Electricity Department"],
    "Himachal Pradesh": [],
    "Jharkhand": [],
    "Manipur": ["Manipur State Power Distribution Company Limited (MSPDCL)"],
    "Meghalaya": [],
    "Mizoram": [],
    "Nagaland": [],
    "Sikkim": [],
    "Tripura": ["Tripura State Electricity Corporation Limited (TSECL)"],
    "Uttarakhand": [],
    "Andaman and Nicobar Islands": [],
    "Chandigarh": [],
    "Dadra and Nagar Haveli and Daman and Diu": [],
    "Jammu and Kashmir": ["Power Development Department, Jammu & Kashmir"],
    "Ladakh": [],
    "Lakshadweep": [],
    "Puducherry": [],
    "Arunachal Pradesh": []
}


# Adding the National discoms if the state discom list is empty
NATIONAL_DISCOMS = ["National Thermal Power Corporation (NTPC)", "PowerGrid Corporation of India"]

# District mapping for each state/UT (simplified, not exhaustive)
STATE_DISTRICTS = {
    "Andhra Pradesh": ["Anantapur", "Chittoor", "East Godavari", "Guntur", "Krishna", "Kurnool", "Nellore", "Prakasam", "Srikakulam", "Visakhapatnam", "Vizianagaram", "West Godavari", "YSR Kadapa"],
    "Arunachal Pradesh": ["Tawang", "West Kameng", "East Kameng", "Papum Pare", "Kurung Kumey", "Kra Daadi", "Lower Subansiri", "Upper Subansiri", "West Siang", "East Siang", "Siang", "Upper Siang", "Lower Siang", "Lower Dibang Valley", "Dibang Valley", "Anjaw", "Lohit", "Namsai", "Changlang", "Tirap", "Longding"],
    "Assam": ["Baksa", "Barpeta", "Biswanath", "Bongaigaon", "Cachar", "Charaideo", "Chirang", "Darrang", "Dhemaji", "Dhubri", "Dibrugarh", "Dima Hasao", "Goalpara", "Golaghat", "Hailakandi", "Hojai", "Jorhat", "Kamrup", "Kamrup Metropolitan", "Karbi Anglong", "Karimganj", "Kokrajhar", "Lakhimpur", "Majuli", "Morigaon", "Nagaon", "Nalbari", "Sivasagar", "Sonitpur", "South Salmara-Mankachar", "Tinsukia", "Udalguri", "West Karbi Anglong"],
    "Bihar": ["Araria", "Arwal", "Aurangabad", "Banka", "Begusarai", "Bhagalpur", "Bhojpur", "Buxar", "Darbhanga", "East Champaran", "Gaya", "Gopalganj", "Jamui", "Jehanabad", "Kaimur", "Katihar", "Khagaria", "Kishanganj", "Lakhisarai", "Madhepura", "Madhubani", "Munger", "Muzaffarpur", "Nalanda", "Nawada", "Patna", "Purnia", "Rohtas", "Saharsa", "Samastipur", "Saran", "Sheikhpura", "Sheohar", "Sitamarhi", "Siwan", "Supaul", "Vaishali", "West Champaran"],
    "Chhattisgarh": ["Balod", "Baloda Bazar", "Balrampur", "Bastar", "Bemetara", "Bijapur", "Bilaspur", "Dantewada", "Dhamtari", "Durg", "Gariaband", "Gaurela-Pendra-Marwahi", "Janjgir-Champa", "Jashpur", "Kabirdham", "Kanker", "Kondagaon", "Korba", "Koriya", "Mahasamund", "Mungeli", "Narayanpur", "Raigarh", "Raipur", "Rajnandgaon", "Sukma", "Surajpur", "Surguja"],
    "Goa": ["North Goa", "South Goa"],
    "Gujarat": ["Ahmedabad", "Amreli", "Anand", "Aravalli", "Banaskantha", "Bharuch", "Bhavnagar", "Botad", "Chhota Udaipur", "Dahod", "Dang", "Devbhoomi Dwarka", "Gandhinagar", "Gir Somnath", "Jamnagar", "Junagadh", "Kachchh", "Kheda", "Mahisagar", "Mehsana", "Morbi", "Narmada", "Navsari", "Panchmahal", "Patan", "Porbandar", "Rajkot", "Sabarkantha", "Surat", "Surendranagar", "Tapi", "Vadodara", "Valsad"],
    "Haryana": ["Ambala", "Bhiwani", "Charkhi Dadri", "Faridabad", "Fatehabad", "Gurugram", "Hisar", "Jhajjar", "Jind", "Kaithal", "Karnal", "Kurukshetra", "Mahendragarh", "Mewat", "Palwal", "Panchkula", "Panipat", "Rewari", "Rohtak", "Sirsa", "Sonipat", "Yamunanagar"],
    "Himachal Pradesh": ["Bilaspur", "Chamba", "Hamirpur", "Kangra", "Kinnaur", "Kullu", "Lahaul and Spiti", "Mandi", "Shimla", "Sirmaur", "Solan", "Una"],
    "Jharkhand": ["Bokaro", "Chatra", "Deoghar", "Dhanbad", "Dumka", "East Singhbhum", "Garhwa", "Giridih", "Godda", "Gumla", "Hazaribagh", "Jamtara", "Khunti", "Koderma", "Latehar", "Lohardaga", "Pakur", "Palamu", "Ramgarh", "Ranchi", "Sahibganj", "Seraikela Kharsawan", "Simdega", "West Singhbhum"],
    "Karnataka": ["Bagalkot", "Ballari", "Belagavi", "Bengaluru Rural", "Bengaluru Urban", "Bidar", "Chamarajanagar", "Chikkaballapur", "Chikkamagaluru", "Chitradurga", "Dakshina Kannada", "Davanagere", "Dharwad", "Gadag", "Hassan", "Haveri", "Kalaburagi", "Kodagu", "Kolar", "Koppal", "Mandya", "Mysuru", "Raichur", "Ramanagara", "Shivamogga", "Tumakuru", "Udupi", "Uttara Kannada", "Vijayapura", "Yadgir"],
    "Kerala": ["Alappuzha", "Ernakulam", "Idukki", "Kannur", "Kasaragod", "Kollam", "Kottayam", "Kozhikode", "Malappuram", "Palakkad", "Pathanamthitta", "Thiruvananthapuram", "Thrissur", "Wayanad"],
    "Madhya Pradesh": ["Agar Malwa", "Alirajpur", "Anuppur", "Ashoknagar", "Balaghat", "Barwani", "Betul", "Bhind", "Bhopal", "Burhanpur", "Chachaura", "Chhindwara", "Damoh", "Datia", "Dewas", "Dhar", "Dindori", "Guna", "Gwalior", "Harda", "Hoshangabad", "Indore", "Jabalpur", "Jhabua", "Katni", "Khandwa", "Khargone", "Mandla", "Mandsaur", "Morena", "Narsinghpur", "Neemuch", "Panna", "Raisen", "Rajgarh", "Ratlam", "Rewa", "Sagar", "Satna", "Sehore", "Seoni", "Shahdol", "Shajapur", "Sheopur", "Shivpuri", "Sidhi", "Singrauli", "Tikamgarh", "Ujjain", "Umaria", "Vidisha"],
    "Maharashtra": ["Ahmednagar", "Akola", "Amravati", "Aurangabad", "Beed", "Bhandara", "Buldhana", "Chandrapur", "Dhule", "Gadchiroli", "Gondia", "Hingoli", "Jalgaon", "Jalna", "Kolhapur", "Latur", "Mumbai City", "Mumbai Suburban", "Nagpur", "Nanded", "Nandurbar", "Nashik", "Osmanabad", "Parbhani", "Pune", "Raigad", "Ratnagiri", "Sangli", "Satara", "Sindhudurg", "Solapur", "Thane", "Wardha", "Washim", "Yavatmal"],
    "Manipur": ["Bishnupur", "Chandel", "Churachandpur", "Imphal East", "Imphal West", "Jiribam", "Kakching", "Kamjong", "Kangpokpi", "Noney", "Pherzawl", "Senapati", "Tamenglong", "Tengnoupal", "Thoubal", "Ukhrul"],
    "Meghalaya": ["East Garo Hills", "East Jaintia Hills", "East Khasi Hills", "North Garo Hills", "Ri-Bhoi", "South Garo Hills", "South West Garo Hills", "South West Khasi Hills", "West Garo Hills", "West Jaintia Hills", "West Khasi Hills"],
    "Mizoram": ["Aizawl", "Champhai", "Hnahthial", "Khawzawl", "Kolasib", "Lawngtlai", "Lunglei", "Mamit", "Saiha", "Serchhip"],
    "Nagaland": ["Chümoukedima", "Dimapur", "Kiphire", "Kohima", "Longleng", "Mokokchung", "Mon", "Niuland", "Peren", "Phek", "Shamator", "Tuensang", "Wokha", "Zunheboto"],
    "Odisha": ["Angul", "Balangir", "Balasore", "Bargarh", "Bhadrak", "Boudh", "Cuttack", "Deogarh", "Dhenkanal", "Gajapati", "Ganjam", "Jagatsinghpur", "Jajpur", "Jharsuguda", "Kalahandi", "Kandhamal", "Kendrapara", "Kendujhar", "Khordha", "Koraput", "Malkangiri", "Mayurbhanj", "Nabarangpur", "Nayagarh", "Nuapada", "Puri", "Rayagada", "Sambalpur", "Subarnapur", "Sundargarh"],
    "Punjab": ["Amritsar", "Barnala", "Bathinda", "Faridkot", "Fatehgarh Sahib", "Fazilka", "Ferozepur", "Gurdaspur", "Hoshiarpur", "Jalandhar", "Kapurthala", "Ludhiana", "Malerkotla", "Mansa", "Moga", "Mohali", "Muktsar", "Nawanshahr", "Pathankot", "Patiala", "Rupnagar", "Sangrur", "Shaheed Bhagat Singh Nagar", "Tarn Taran"],
    "Rajasthan": ["Ajmer", "Alwar", "Banswara", "Baran", "Barmer", "Bharatpur", "Bhilwara", "Bikaner", "Bundi", "Chittorgarh", "Churu", "Dausa", "Dholpur", "Dungarpur", "Ganganagar", "Hanumangarh", "Jaipur", "Jaisalmer", "Jalore", "Jhalawar", "Jhunjhunu", "Jodhpur", "Karauli", "Kota", "Nagaur", "Pali", "Pratapgarh", "Rajsamand", "Sawai Madhopur", "Sikar", "Sirohi", "Sri Ganganagar", "Tonk", "Udaipur"],
    "Sikkim": ["East Sikkim", "North Sikkim", "South Sikkim", "West Sikkim"],
    "Tamil Nadu": ["Ariyalur", "Chennai", "Coimbatore", "Cuddalore", "Dharmapuri", "Dindigul", "Erode", "Kallakurichi", "Kanchipuram", "Kanyakumari", "Karur", "Krishnagiri", "Madurai", "Mayiladuthurai", "Nagapattinam", "Namakkal", "Nilgiris", "Perambalur", "Pudukkottai", "Ramanathapuram", "Ranipet", "Salem", "Sivaganga", "Tenkasi", "Thanjavur", "Theni", "Thiruvallur", "Thiruvannamalai", "Thiruvarur", "Tiruchirappalli", "Tirunelveli", "Tirupattur", "Tiruppur", "Tiruvannamalai", "Vellore", "Viluppuram", "Virudhunagar"],
    "Telangana": ["Adilabad", "Bhadradri Kothagudem", "Hanamkonda", "Hyderabad", "Jagtial", "Jangaon", "Jayashankar Bhupalpally", "Jogulamba Gadwal", "Kamareddy", "Karimnagar", "Khammam", "Komaram Bheem Asifabad", "Mahabubabad", "Mahabubnagar", "Mancherial", "Medak", "Medchal-Malkajgiri", "Mulugu", "Nagarkurnool", "Nalgonda", "Narayanpet", "Nirmal", "Nizamabad", "Peddapalli", "Rajanna Sircilla", "Ranga Reddy", "Sangareddy", "Siddipet", "Suryapet", "Vikarabad", "Wanaparthy", "Warangal Rural", "Warangal Urban", "Yadadri Bhuvanagiri"],
    "Tripura": ["Dhalai", "Gomati", "Khowai", "North Tripura", "Sepahijala", "South Tripura", "Unakoti", "West Tripura"],
    "Uttar Pradesh": ["Agra", "Aligarh", "Allahabad", "Ambedkar Nagar", "Amroha", "Auraiya", "Ayodhya", "Azamgarh", "Baghpat", "Bahraich", "Ballia", "Banda", "Barabanki", "Bareilly", "Basti", "Bhadohi", "Bijnor", "Budaun", "Bulandshahar", "Chandauli", "Chandausi", "Deoria", "Etah", "Etawah", "Faizabad", "Farrukhabad", "Fatehpur", "Firozabad", "Gautam Buddha Nagar", "Ghaziabad", "Ghazipur", "Gonda", "Gorakhpur", "Hapur", "Hardoi", "Hathras", "Jalaun", "Jaunpur", "Jhansi", "Kannauj", "Kanpur Dehat", "Kanpur Nagar", "Kasganj", "Kaushambi", "Kushinagar", "Lalitpur", "Lucknow", "Maharajganj", "Mahoba", "Mainpuri", "Mathura", "Mau", "Meerut", "Mirzapur", "Moradabad", "Muzaffarnagar", "Pilibhit", "Pratapgarh", "Rae Bareli", "Rampur", "Saharanpur", "Sambhal", "Sant Kabir Nagar", "Shahjahanpur", "Shamli", "Shravasti", "Siddharthnagar", "Sitapur", "Sonbhadra", "Sultanpur", "Unnao", "Varanasi"],
    "Uttarakhand": [
        "Almora", "Bageshwar", "Chamoli", "Champawat", "Dehradun", "Haridwar", "Nainital", 
        "Pauri Garhwal", "Pithoragarh", "Rudraprayag", "Tehri Garhwal", "Udham Singh Nagar", 
        "Uttarkashi"
    ],
    "West Bengal": [
        "Alipurduar", "Bankura", "Birbhum", "Burdwan", "Cooch Behar", "Dakshin Dinajpur", 
        "Darjeeling", "Hooghly", "Howrah", "Jalpaiguri", "Jhargram", "Kolkata", "Malda", 
        "Murshidabad", "Nadia", "North 24 Parganas", "Paschim Bardhaman", "Paschim Medinipur", 
        "Purba Bardhaman", "Purba Medinipur", "Purulia", "South 24 Parganas", "Uttar Dinajpur"
    ]
}

UNION_TERRITORY_DISTRICTS = {
    "Andaman and Nicobar Islands": ["Nicobar", "North and Middle Andaman", "South Andaman"],
    "Chandigarh": ["Chandigarh"],
    "Dadra and Nagar Haveli and Daman and Diu": ["Dadra and Nagar Haveli", "Daman", "Diu"],
    "Delhi": ["Central Delhi", "East Delhi", "New Delhi", "North Delhi", "North East Delhi", 
              "North West Delhi", "Shahdara", "South Delhi", "South East Delhi", 
              "South West Delhi", "West Delhi"],
    "Jammu and Kashmir": ["Anantnag", "Bandipora", "Baramulla", "Budgam", "Doda", "Ganderbal", 
                          "Jammu", "Kathua", "Kishtwar", "Kulgam", "Kupwara", "Pulwama", 
                          "Poonch", "Rajouri", "Ramban", "Reasi", "Samba", "Shopian", 
                          "Srinagar", "Udhampur"],
    "Ladakh": ["Kargil", "Leh"],
    "Lakshadweep": ["Amini", "Andrott", "Bithra", "Chetlat", "Kavaratti", "Kiltan"],
    "Puducherry": ["Karaikal", "Mahe", "Pondicherry", "Yanam"]
}