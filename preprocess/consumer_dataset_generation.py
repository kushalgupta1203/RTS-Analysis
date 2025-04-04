# This is for sample dataset for consumers.

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from faker import Faker
import string
from collections import defaultdict

print(f"Your dataset is under generation phase...")

# Set a seed for reproducibility
np.random.seed(42)
random.seed(42)

# Initialize Faker for generating realistic names, emails, etc.
fake = Faker('en_IN')
Faker.seed(42)

# Constants
START_DATE = datetime.strptime('01-01-2024', '%d-%m-%Y')
END_DATE = datetime.strptime('31-12-2024', '%d-%m-%Y')
ADULT_DATE = datetime.strptime('01-01-2006', '%d-%m-%Y')  # 18 years before 01-01-2024

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

# State Production Share Ratio
production_share = {
    "Gujarat": 16.99990, "Maharashtra": 9.22990, "Uttar Pradesh": 8.21990, "Rajasthan": 6.70990,
    "Karnataka": 4.70990, "Telangana": 4.64990, "Andhra Pradesh": 4.51990, "Madhya Pradesh": 2.78990,
    "Tamil Nadu": 2.50990, "Punjab": 1.15990, "Haryana": 1.02990, "Chhattisgarh": 0.94990,
    "Kerala": 0.75990, "Uttarakhand": 0.56990, "Odisha": 0.44990, "Delhi": 0.21990,
    "Bihar": 0.18990, "West Bengal": 0.17990, "Assam": 0.14990, "Jharkhand": 0.10990,
    "Himachal Pradesh": 0.09990, "Jammu and Kashmir": 0.05990, "Puducherry": 0.04990,
    "Mizoram": 0.03990, "Goa": 0.03990, "Andaman and Nicobar Islands": 0.03990,
    "Chandigarh": 0.05990, "Tripura": 0.02990, "Dadra and Nagar Haveli and Daman and Diu": 0.01990,
    "Manipur": 0.01990, "Arunachal Pradesh": 0.01990, "Sikkim": 0.00990, "Nagaland": 0.00990,
    "Lakshadweep": 0.00990, "Meghalaya": 0.00990
}


ACCEPTANCE_RATIOS = {
    "Andhra Pradesh": 0.80, "Arunachal Pradesh": 0.85, "Assam": 0.72, "Bihar": 0.64,
    "Chhattisgarh": 0.92, "Goa": 0.75, "Gujarat": 0.92, "Haryana": 0.82,
    "Himachal Pradesh": 0.87, "Jharkhand": 0.78, "Karnataka": 0.79, "Kerala": 0.81,
    "Madhya Pradesh": 0.83, "Maharashtra": 0.86, "Manipur": 0.79, "Meghalaya": 0.74,
    "Mizoram": 0.73, "Nagaland": 0.87, "Odisha": 0.84, "Punjab": 0.81,
    "Rajasthan": 0.87, "Sikkim": 0.86, "Tamil Nadu": 0.85, "Telangana": 0.78,
    "Tripura": 0.70, "Uttar Pradesh": 0.82, "Uttarakhand": 0.79, "West Bengal": 0.81,
    "Andaman and Nicobar Islands": 0.62, "Chandigarh": 0.73,
    "Dadra and Nagar Haveli and Daman and Diu": 0.77, "Delhi": 0.74,
    "Jammu and Kashmir": 0.85, "Ladakh": 0.88, "Lakshadweep": 0.66, "Puducherry": 0.69
}


SOLAR_ORGANIZATION_WEIGHTS = {
    "SunTech Solar Solutions": 0.075, "GreenEnergy Systems": 0.050, "SolarPeak Innovations": 0.065, 
    "BrightSun Power": 0.090, "EcoSolar Enterprises": 0.040, "RadiantSun Energy": 0.085, 
    "InfiniteLight Solar": 0.060, "PowerSun Technologies": 0.055, "SunRise Renewable Solutions": 0.070, 
    "GreenRay Solar Systems": 0.045, "SkyPower Solar": 0.095, "SunWave Energy": 0.080, 
    "EcoPower Solar": 0.030, "SunBeam Energy Solutions": 0.035, "SolarEdge Systems": 0.025, 
    "IlluminateSun Technologies": 0.055, "SolarHarvest Energy": 0.065, "SunVolt Power": 0.045, 
    "GreenSpark Solar": 0.085, "SolarCrest Enterprises": 0.050
}


# Dictionary to track the count of each DISCOM's selection
discom_selection_count = defaultdict(lambda: defaultdict(int))

def assign_discoms_gaussian(state):
    if state in STATE_DISCOM_MAP and STATE_DISCOM_MAP[state]:  
        source_discoms = STATE_DISCOM_MAP[state]
        num_discoms = len(source_discoms)

        if num_discoms == 1:
            return source_discoms[0]  # If only one DISCOM, return it

        mean = (num_discoms - 1) / 2  # Center of distribution
        std_dev = max(1, num_discoms / 4)  # Controls variance

        # Assign weights based on Gaussian probability
        weights = [np.exp(-((i - mean) ** 2) / (2 * std_dev ** 2)) for i in range(num_discoms)]
        total_weight = sum(weights)
        weights = [w / total_weight for w in weights]

        # **Modify selection to reduce repetition**
        # Adjust weights based on how many times a DISCOM has already been selected
        adjusted_weights = [
            w / (1 + discom_selection_count[state][source_discoms[i]])  # Penalize already selected DISCOMs
            for i, w in enumerate(weights)
        ]

        # Normalize the adjusted weights
        total_adjusted_weight = sum(adjusted_weights)
        adjusted_weights = [w / total_adjusted_weight for w in adjusted_weights]

        # Select **one** DISCOM with the adjusted probability
        selected_discom = random.choices(source_discoms, weights=adjusted_weights, k=1)[0]

        # Update the selection count
        discom_selection_count[state][selected_discom] += 1  

        return selected_discom

    else:  
        # If state not found, pick from NATIONAL_DISCOMS with (0.27, 0.73) probability
        return random.choices(NATIONAL_DISCOMS, weights=[0.27, 0.73], k=1)[0]




# Combine state and UT districts
DISTRICTS = {}
DISTRICTS.update(STATE_DISTRICTS)
DISTRICTS.update(UNION_TERRITORY_DISTRICTS)

# Function to select a random district for a given state/UT
def get_random_district_gaussian(state):
    if state in DISTRICTS and DISTRICTS[state]:
        districts = DISTRICTS[state]
        num_districts = len(districts)

        # Generate weights using a Gaussian-like curve
        mean = (num_districts - 1) / 2  # Center of distribution
        std_dev = max(1, num_districts / 4)  # Controls variance (adjustable)

        # Assign weights based on normal distribution probability
        weights = [np.exp(-((i - mean) ** 2) / (2 * std_dev ** 2)) for i in range(num_districts)]

        # Normalize weights so they sum to 1
        total_weight = sum(weights)
        weights = [w / total_weight for w in weights]

        # Select a district based on weighted probability
        return random.choices(districts, weights=weights, k=1)[0]
    else:
        return None

# Normalize weights to sum to 1
total_weight = sum(SOLAR_ORGANIZATION_WEIGHTS.values())
SOLAR_ORGANIZATION_WEIGHTS = {k: v / total_weight for k, v in SOLAR_ORGANIZATION_WEIGHTS.items()}

# Initialize selection counter
counter = defaultdict(int)

def get_solar_organization_weighted():
    global counter

    # Select an organization based on predefined weights
    selected_org = random.choices(
        list(SOLAR_ORGANIZATION_WEIGHTS.keys()), 
        weights=list(SOLAR_ORGANIZATION_WEIGHTS.values()), 
        k=1
    )[0]

    # Increase the count for variance tracking
    counter[selected_org] += 1

    return selected_org


# Helper functions
def random_date(start_date, end_date):
    """Generate a random date between start_date and end_date"""
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    return start_date + timedelta(days=random_days)

def random_dob():
    """Generate a random date of birth ensuring ages are uniformly distributed between 18 and 75 years."""
    today = datetime.strptime('01-01-2024', '%d-%m-%Y')
    min_age = 18
    max_age = 75

    # Generate a random age in the range [18, 75]
    random_age = random.randint(min_age, max_age)

    # Compute the birthdate based on the random age
    random_days = random.randint(0, 364)  # Vary birthdate within the chosen year
    birth_date = today - timedelta(days=(random_age * 365 + random_days))

    return birth_date



import random
from datetime import datetime, timedelta
from scipy.stats import truncnorm

def truncated_gaussian(mean, std_dev, lower_bound, upper_bound):
    """Generate a value from a truncated Gaussian distribution."""
    a, b = (lower_bound - mean) / std_dev, (upper_bound - mean) / std_dev
    return int(truncnorm.rvs(a, b, loc=mean, scale=std_dev))

def skewed_gaussian_gap(ranges, normalized_weights):
    """Generate gap using skewed Gaussian distribution based on provided ranges and weights."""
    selected_range = random.choices(ranges, weights=normalized_weights)[0]
    mean = (selected_range[0] + selected_range[1]) / 2
    std_dev = (selected_range[1] - selected_range[0]) / 6
    return truncated_gaussian(mean, std_dev, selected_range[0], selected_range[1])

def gaussian_gap(min_gap, max_gap, stage=None, stage_data=None):
    """Generate gap using skewed Gaussian distribution based on provided ratios."""
    if stage and stage_data:
        ranges = stage_data['ranges']
        normalized_weights = stage_data['normalized_weights']
        return skewed_gaussian_gap(ranges=ranges, normalized_weights=normalized_weights)
    else:
        # Default Gaussian distribution if not defined stage
        mean = (min_gap + max_gap) / 2
        std_dev = (max_gap - min_gap) / 6
        return truncated_gaussian(mean=mean, std_dev=std_dev,
                                  lower_bound=min_gap,
                                  upper_bound=max_gap)

def generate_dates_sequence(START_DATE: datetime, END_DATE: datetime):
    """Generate sequence of dates for the solar application process with monthly distribution."""
    month_weights = {
        1: 0.03, 2: 0.05, 3: 0.06, 4: 0.07, 5: 0.08, 6: 0.09,
        7: 0.15, 8: 0.09, 9: 0.08, 10: 0.09, 11: 0.12, 12: 0.09
    }

    # Select a month based on weights
    month = random.choices(
        population=list(month_weights.keys()),
        weights=list(month_weights.values()),
        k=1
    )[0]

    # Generate a random day within that month
    year = START_DATE.year
    max_day = (
        (29 if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else
         (28 if month == 2 else
          (30 if month in [4, 6, 9, 11] else
           (31)))
    )
    )
    day = random.randint(1, max_day)

    registration_date = datetime(year, month, day)

    min_gaps = {
        "approval": 1, "vendor_selection": 1, "vendor_acceptance": 1,
        "installation": 1, "inspection": 1, "claim_submission": 1,
        "claim_release": 1
    }

    max_gaps = {
        "approval": 180, "vendor_selection": 180, "vendor_acceptance": 180,
        "installation": 180, "inspection": 180, "claim_submission": 180,
        "claim_release": 180
    }

    # Precompute ranges and normalized weights for each stage
    ratios = {
        "approval": [78.44, 17.17, 4.39, 0, 0],
        "vendor_selection": [74.1, 24.2, 1.7, 0, 0],
        "vendor_acceptance": [57.88, 28.94, 13.18, 0, 0],
        "installation": [20.04, 56.85, 13.11, 1.93, 0.07],
        "inspection": [22.46, 47.44, 18.10, 7.66, 0.34],
        "claim_submission": [16.06, 37.66, 30.28, 5.70, 0.30],
        "claim_release": [15.41, 43.86, 22.73, 4.20, 1.80]
    }

    stage_data = {}
    for stage, weights in ratios.items():
        ranges = [(1, 15), (16, 30), (31, 60), (61, 120), (121, max_gaps[stage] + 1)]
        normalized_weights = [w / sum(weights) for w in weights]
        stage_data[stage] = {'ranges': ranges, 'normalized_weights': normalized_weights}

    approval_date = None
    vendor_selection_date = None
    vendor_acceptance_date = None
    installation_date = None
    inspection_date = None
    claim_submission_date = None
    claim_release_date = None

    remaining_days = (END_DATE - registration_date).days
    current_date = registration_date  # Keep track of the current date

    # Approval Date Calculation
    current_max_gap = min(max_gaps["approval"], remaining_days)
    if current_max_gap >= min_gaps["approval"]:
        gap = gaussian_gap(min_gaps["approval"], current_max_gap, stage="approval", stage_data=stage_data["approval"])
        approval_date = current_date + timedelta(days=gap)
        if approval_date <= END_DATE:
            current_date = approval_date
            remaining_days = (END_DATE - current_date).days
        else:
            approval_date = None  # Reset if out of range

    # Vendor Selection Date Calculation
    if approval_date:
        current_max_gap = min(max_gaps["vendor_selection"], remaining_days)
        if current_max_gap >= min_gaps["vendor_selection"]:
            gap = gaussian_gap(min_gaps["vendor_selection"], current_max_gap, stage="vendor_selection", stage_data=stage_data["vendor_selection"])
            vendor_selection_date = current_date + timedelta(days=gap)
            if vendor_selection_date <= END_DATE:
                current_date = vendor_selection_date
                remaining_days = (END_DATE - current_date).days
            else:
                vendor_selection_date = None

    # Vendor Acceptance Date Calculation
    if vendor_selection_date:
        current_max_gap = min(max_gaps["vendor_acceptance"], remaining_days)
        if current_max_gap >= min_gaps["vendor_acceptance"]:
            gap = gaussian_gap(min_gaps["vendor_acceptance"], current_max_gap, stage="vendor_acceptance", stage_data=stage_data["vendor_acceptance"])
            vendor_acceptance_date = current_date + timedelta(days=gap)
            if vendor_acceptance_date <= END_DATE:
                current_date = vendor_acceptance_date
                remaining_days = (END_DATE - current_date).days
            else:
                vendor_acceptance_date = None

    # Installation Date Calculation
    if vendor_acceptance_date:
        current_max_gap = min(max_gaps["installation"], remaining_days)
        if current_max_gap >= min_gaps["installation"]:
            gap = gaussian_gap(min_gaps["installation"], current_max_gap, stage="installation", stage_data=stage_data["installation"])
            installation_date = current_date + timedelta(days=gap)
            if installation_date <= END_DATE:
                current_date = installation_date
                remaining_days = (END_DATE - current_date).days
            else:
                installation_date = None

    # Inspection Date Calculation
    if installation_date:
        current_max_gap = min(max_gaps["inspection"], remaining_days)
        if current_max_gap >= min_gaps["inspection"]:
            gap = gaussian_gap(min_gaps["inspection"], current_max_gap, stage="inspection", stage_data=stage_data["inspection"])
            inspection_date = current_date + timedelta(days=gap)
            if inspection_date <= END_DATE:
                current_date = inspection_date
                remaining_days = (END_DATE - current_date).days
            else:
                inspection_date = None

    # Claim Submission Date Calculation
    if inspection_date:
        current_max_gap = min(max_gaps["claim_submission"], remaining_days)
        if current_max_gap >= min_gaps["claim_submission"]:
            gap = gaussian_gap(min_gaps["claim_submission"], current_max_gap, stage="claim_submission", stage_data=stage_data["claim_submission"])
            claim_submission_date = current_date + timedelta(days=gap)
            if claim_submission_date <= END_DATE:
                current_date = claim_submission_date
                remaining_days = (END_DATE - current_date).days
            else:
                claim_submission_date = None

    # Claim Release Date Calculation
    if claim_submission_date:
        current_max_gap = min(max_gaps["claim_release"], remaining_days)
        if current_max_gap >= min_gaps["claim_release"]:
            gap = gaussian_gap(min_gaps["claim_release"], current_max_gap, stage="claim_release", stage_data=stage_data["claim_release"])
            claim_release_date = current_date + timedelta(days=gap)
            if claim_release_date > END_DATE:
                claim_release_date = None

    result = {
        "registration_date": registration_date,
        "approval_date": approval_date,
        "vendor_selection_date": vendor_selection_date,
        "vendor_acceptance_date": vendor_acceptance_date,
        "installation_date": installation_date,
        "inspection_date": inspection_date,
        "claim_submission_date": claim_submission_date,
        "claim_release_date": claim_release_date,
    }

    return result







START_DATE = datetime.strptime('01-01-2024', '%d-%m-%Y')
END_DATE = datetime.strptime('31-12-2024', '%d-%m-%Y')



application_numbers = set()
ca_numbers = set()

def generate_unique_application_number():
    """Generate a unique 8-digit numeric application number, not starting with 0."""
    while True:
        app_number = ''.join(random.choices(string.digits[1:], k=1)) + ''.join(random.choices(string.digits, k=7))
        if app_number not in application_numbers:
            application_numbers.add(app_number)
            return app_number

def generate_unique_9digit_ca_number():
    """Generate a consumer account number, not starting with 0."""
    while True:
        ca_number = ''.join(random.choices(string.digits[1:], k=1)) + ''.join(random.choices(string.digits, k=8))
        if ca_number not in ca_numbers:
            ca_numbers.add(ca_number)
            return ca_number

def generate_email(first_name, last_name):
    """Generate an email based on first and last name"""
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "rediffmail.com"]
    name_part = f"{first_name.lower()}.{last_name.lower()}".replace(" ", "")
    random_num = random.randint(1, 9999)
    domain = random.choice(domains)
    return f"{name_part}{random_num}@{domain}"

def assign_production_capacity():
    """Assign production capacity based on given distribution"""
    rand = random.uniform(0, 1)  # Random number between 0-1

    if rand <= 168 / 44953:
        return "1 - 2 KW"
    elif rand <= (168 + 2496) / 44953:
        return "2 - 3 KW"
    elif rand <= (168 + 2496 + 31495) / 44953:
        return "3 - 4 KW"
    elif rand <= (168 + 2496 + 31495 + 6598) / 44953:
        return "4 - 5 KW"
    elif rand <= (168 + 2496 + 31495 + 6598 + 3300) / 44953:
        return "5 - 6 KW"
    else:
        return "Above 6 KW"

def assign_rwa_residential(state, district):
    """
    Assigns 'RWA' or 'Residential' based on a skewed Gaussian distribution across states and districts.
    - 17% applicants should be 'RWA'
    - 83% should be 'Residential'
    - Gaussian skew ensures district/state-based variations.
    """
    # Base probability distribution
    base_prob = 0.17  # RWA ratio

    # Skew factor based on state and district (introducing variation)
    state_hash = abs(hash(state)) % 10 / 100  # Convert state hash to a small variation (0 to 0.1)
    district_hash = abs(hash(district)) % 5 / 100  # Convert district hash to a smaller variation (0 to 0.05)

    # Skewed probability for RWA (some states/districts have slightly higher/lower chance)
    adjusted_prob = base_prob + state_hash - district_hash  # Adjust probability using skew factor
    adjusted_prob = max(0.10, min(0.25, adjusted_prob))  # Keep within a reasonable range (10% - 25%)

    # Assign category based on adjusted probability
    return "RWA" if random.random() < adjusted_prob else "Residential"





# Gender Options and Ratio
gender_options = ["Male", "Female", "Other"]
gender_ratio = [55, 44, 1]
gender_weights = [x / sum(gender_ratio) for x in gender_ratio]

# Acceptance Ratio
acceptance_ratio_weights = [ACCEPTANCE_RATIOS[state] / sum(ACCEPTANCE_RATIOS.values()) for state in STATES + UNION_TERRITORIES if state in ACCEPTANCE_RATIOS]
acceptance_ratio_list = [state for state in STATES + UNION_TERRITORIES if state in ACCEPTANCE_RATIOS]

# Normalizing Production Share as Weights
state_weights = [production_share[state] / sum(production_share.values()) for state in STATES + UNION_TERRITORIES if state in production_share]
state_list = [state for state in STATES + UNION_TERRITORIES if state in production_share]  # Ensure STATES and UNION_TERRITORIES are combined

combined_weights = {}
for state in set(state_list + acceptance_ratio_list):
    prod_weight = production_share.get(state, 0) / sum(production_share.values()) if state in production_share else 0
    acc_weight = ACCEPTANCE_RATIOS.get(state, 0.3) / sum(ACCEPTANCE_RATIOS.values()) if state in ACCEPTANCE_RATIOS else 0
    
    # You can adjust how much each factor matters (e.g., 0.7*prod + 0.3*acc)
    combined_weights[state] = 0.7 * prod_weight + 0.3 * acc_weight

combined_state_list = list(combined_weights.keys())
combined_weight_values = [combined_weights[state] for state in combined_state_list]


# --- Data Generation ---
num_records = 1048532
data = []



# --- Data Generation Loop ---
for _ in range(num_records):
    # Select state using combined weights
    state = random.choices(combined_state_list, weights=combined_weight_values, k=1)[0]
    
    # Acceptance Logic
    acceptance_ratio = ACCEPTANCE_RATIOS.get(state, 0.3)
    is_accepted = random.random() < acceptance_ratio
    acceptance_status = "Accepted" if is_accepted else "Rejected"

    # Generate basic information
    consumer_first_name = fake.first_name()
    consumer_last_name = fake.last_name()

    # 98% same last name as applicant
    guardian_last_name = consumer_last_name if random.random() < 0.98 else fake.last_name()
    guardian_first_name = fake.first_name()

    date_of_birth = random_dob()
    district = get_random_district_gaussian(state)
    gender = random.choices(gender_options, weights=gender_weights, k=1)[0]
    dates = generate_dates_sequence(START_DATE=START_DATE, END_DATE=END_DATE)
    registration_date = dates["registration_date"]
    rwa_residential = assign_rwa_residential(state, district)

    # Helper function to format dates safely
    def format_date_safely(date_obj):
        return date_obj.strftime('%Y-%m-%d') if date_obj is not None else "Pending"


    # Generate the rest of the data
    record = {
        "Application Number": generate_unique_application_number(),
        "Consumer First Name": consumer_first_name,
        "Consumer Last Name": consumer_last_name,
        "Guardian First Name": guardian_first_name,
        "Guardian Last Name": guardian_last_name,
        "Gender": gender,
        "State/UT": state,
        "District": district,
        "RWA/Residential": rwa_residential,
        "Date Of Birth": date_of_birth.strftime('%Y-%m-%d'),
        "CA Number": generate_unique_9digit_ca_number(),
        "Discom Name": assign_discoms_gaussian(state),
        "Email Address": generate_email(consumer_first_name, consumer_last_name),
        "Acceptance Status": acceptance_status,
        "Production Capacity (KW)": assign_production_capacity(),
        "Vendor First Name": fake.first_name(),
        "Vendor Last Name": fake.last_name(),
        "Vendor Organization": get_solar_organization_weighted(),
        "Registration Date": registration_date.strftime('%Y-%m-%d'),
        "Application Approved Date": format_date_safely(dates["approval_date"]) if is_accepted else "Declined",
        "Vendor Selection Date": format_date_safely(dates["vendor_selection_date"]) if is_accepted else "Declined",
        "Vendor Acceptance Date": format_date_safely(dates["vendor_acceptance_date"]) if is_accepted else "Declined",
        "Installation Date": format_date_safely(dates["installation_date"]) if is_accepted else "Declined",
        "Inspection Date": format_date_safely(dates["inspection_date"]) if is_accepted else "Declined",
        "Subsidy Redeemed Date": format_date_safely(dates["claim_submission_date"]) if is_accepted else "Declined",
        "Subsidy Released Date": format_date_safely(dates["claim_release_date"]) if is_accepted else "Declined",
    }
    
    data.append(record)


# --- DataFrame Creation and Export ---
df = pd.DataFrame(data)

output_file = r"D:\Projects\RTS Analysis\dataset\consumer_application_data.csv"

# Export to CSV
df.to_csv(output_file, index=False)

print(f"Data generation complete. CSV file created: {output_file}")

