# This is for sample dataset for consumers.

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from faker import Faker
import string

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
for state, discoms in STATE_DISCOM_MAP.items():
    if not discoms:
        STATE_DISCOM_MAP[state] = NATIONAL_DISCOMS


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

# Combine state and UT districts
DISTRICTS = {}
DISTRICTS.update(STATE_DISTRICTS)
DISTRICTS.update(UNION_TERRITORY_DISTRICTS)

# Function to select a random district for a given state/UT
def get_random_district(state):
    if state in DISTRICTS and DISTRICTS[state]:
        return random.choice(DISTRICTS[state])
    else:
        return None

# Helper functions
def random_date(start_date, end_date):
    """Generate a random date between start_date and end_date"""
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    return start_date + timedelta(days=random_days)

def random_dob():
    """Generate a random date of birth (at least 18 years old on Jan 1, 2024)"""
    today = datetime.strptime('01-01-2024', '%d-%m-%Y')
    max_age = 75
    earliest_birth_date = today - timedelta(days=max_age * 365)  # Approximate

    # Generate a random date between start_date and the earliest valid birth date
    generated_date = random_date(ADULT_DATE - timedelta(days=365*57), earliest_birth_date)

    # Check if the generated date is within the age range (18-75)
    age = today.year - generated_date.year - ((today.month, today.day) < (generated_date.month, generated_date.day))
    if 18 <= age <= 75:
        return generated_date
    else:
        # If the generated date is outside the age range, return a default valid date (e.g., 50 years old)
        return today - timedelta(days=365*50)

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

def generate_dates_sequence():
    """Generate a sequence of dates for the solar application process"""
    # Registration date
    registration_date = random_date(START_DATE, END_DATE)
    
    # Minimum time gaps between steps (in days)
    min_gaps = {
        "approval": 3,
        "vendor_selection": 5,
        "vendor_acceptance": 2,
        "installation": 10,
        "inspection": 5,
        "claim_submission": 3,
        "claim_release": 7
    }
    
    # Maximum time gaps between steps (in days)
    max_gaps = {
        "approval": 15,
        "vendor_selection": 30,
        "vendor_acceptance": 7,
        "installation": 45,
        "inspection": 15,
        "claim_submission": 10,
        "claim_release":120
    }
    
    # Calculate dates with random gaps
    approval_date = registration_date + timedelta(days=random.randint(min_gaps["approval"], max_gaps["approval"]))
    
    # Ensure all dates fit within the year 2024
    if approval_date > END_DATE:
        approval_date = END_DATE
        
    vendor_selection_date = approval_date + timedelta(days=random.randint(min_gaps["vendor_selection"], max_gaps["vendor_selection"]))
    if vendor_selection_date > END_DATE:
        vendor_selection_date = END_DATE
        
    vendor_acceptance_date = vendor_selection_date + timedelta(days=random.randint(min_gaps["vendor_acceptance"], max_gaps["vendor_acceptance"]))
    if vendor_acceptance_date > END_DATE:
        vendor_acceptance_date = END_DATE
        
    installation_date = vendor_acceptance_date + timedelta(days=random.randint(min_gaps["installation"], max_gaps["installation"]))
    if installation_date > END_DATE:
        installation_date = END_DATE
        
    inspection_date = installation_date + timedelta(days=random.randint(min_gaps["inspection"], max_gaps["inspection"]))
    if inspection_date > END_DATE:
        inspection_date = END_DATE
        
    claim_submission_date = inspection_date + timedelta(days=random.randint(min_gaps["claim_submission"], max_gaps["claim_submission"]))
    if claim_submission_date > END_DATE:
        claim_submission_date = END_DATE
        
    claim_release_date = claim_submission_date + timedelta(days=random.randint(min_gaps["claim_release"], max_gaps["claim_release"]))
    if claim_release_date > END_DATE:
        claim_release_date = END_DATE
    
    return {
        "registration_date": registration_date,
        "approval_date": approval_date,
        "vendor_selection_date": vendor_selection_date,
        "vendor_acceptance_date": vendor_acceptance_date,
        "installation_date": installation_date,
        "inspection_date": inspection_date,
        "claim_submission_date": claim_submission_date,
        "claim_release_date": claim_release_date
    }

# Gender Options and Ratio
gender_options = ["Male", "Female", "Other"]
gender_ratio = [55, 41, 4]  # 55:41:4
gender_weights = [x / sum(gender_ratio) for x in gender_ratio]

# Application Status Options and Ratio
status_options = ["Approved", "Pending", "Rejected", "Installed", "Claim Submitted", "Claim Released"]
status_ratio = [20, 25, 7, 35, 13, 10]  # Adjusted ratios
status_weights = [x / sum(status_ratio) for x in status_ratio]

# State Production Share Ratio
production_share = {
    "Rajasthan": 16.99990, "Gujarat": 9.22990, "Karnataka": 8.21990, "Tamil Nadu": 6.70990,
    "Maharashtra": 4.70990, "Telangana": 4.64990, "Andhra Pradesh": 4.51990, "Madhya Pradesh": 2.78990,
    "Uttar Pradesh": 2.50990, "Punjab": 1.15990, "Haryana": 1.02990, "Chhattisgarh": 0.94990,
    "Kerala": 0.75990, "Uttarakhand": 0.56990, "Odisha": 0.44990, "Delhi": 0.21990,
    "Bihar": 0.18990, "West Bengal": 0.17990, "Assam": 0.14990, "Jharkhand": 0.10990,
    "Himachal Pradesh": 0.09990, "Jammu and Kashmir": 0.05990, "Puducherry": 0.04990,
    "Mizoram": 0.03990, "Goa": 0.03990, "Andaman and Nicobar Islands": 0.03990,
    "Chandigarh": 0.05990, "Tripura": 0.02990, "Dadra and Nagar Haveli and Daman and Diu": 0.01990,
    "Manipur": 0.01990, "Arunachal Pradesh": 0.01990, "Sikkim": 0.00990, "Nagaland": 0.00990,
    "Lakshadweep": 0.00990, "Meghalaya": 0.00990
}


# Normalizing Production Share as Weights
state_weights = [production_share[state] / sum(production_share.values()) for state in STATES + UNION_TERRITORIES if state in production_share]
state_list = [state for state in STATES + UNION_TERRITORIES if state in production_share]  # Ensure STATES and UNION_TERRITORIES are combined

# --- Data Generation ---
num_records = 948576
data = []

for _ in range(num_records):
    # Select state based on solar production share
    state = random.choices(state_list, weights=state_weights, k=1)[0]

    # Generate basic information
    consumer_first_name = fake.first_name()
    consumer_last_name = fake.last_name()
    
    # 98% same last name as applicant
    if random.random() < 0.98:
        guardian_last_name = consumer_last_name
    else:
        guardian_last_name = fake.last_name()
    
    guardian_first_name = fake.first_name()
    generated_date = random_date(ADULT_DATE - timedelta(days=365*57), END_DATE)

    district = get_random_district(state)
    gender = random.choices(gender_options, weights=gender_weights, k=1)[0]
    dates = generate_dates_sequence()
    date_of_birth = generated_date
    date_of_birth = random_dob()
    registration_date = dates["registration_date"]
    discom_name = random.choice(STATE_DISCOM_MAP[state])

    # Generate the rest of the data
    record = {
        "consumer_first_name": consumer_first_name,
        "consumer_last_name": consumer_last_name,
        "guardian_first_name": guardian_first_name,
        "guardian_last_name": guardian_last_name,
        "gender": gender,
        "state_ut": state,
        "district": district,
        "date_of_birth": date_of_birth.strftime('%Y-%m-%d'),
        "ca_number": generate_unique_9digit_ca_number(),
        "discom_name": discom_name,
        "email_address": generate_email(consumer_first_name, consumer_last_name),
        "registration_date": registration_date.strftime('%Y-%m-%d'),
        "application_approved_date": dates["approval_date"].strftime('%Y-%m-%d'),
        "application_number": generate_unique_application_number(),
        "vendor_first_name": fake.first_name(),
        "vendor_last_name": fake.last_name(),
        "vendor_organization": random.choice(SOLAR_ORGANIZATIONS),
        "vendor_selection_date": dates["vendor_selection_date"].strftime('%Y-%m-%d'),
        "vendor_acceptance_date": dates["vendor_acceptance_date"].strftime('%Y-%m-%d'),
        "installation_date": dates["installation_date"].strftime('%Y-%m-%d'),
        "inspection_date": dates["inspection_date"].strftime('%Y-%m-%d'),
        "claim_submission_date": dates["claim_submission_date"].strftime('%Y-%m-%d'),
        "claim_release_date": dates["claim_release_date"].strftime('%Y-%m-%d'),
    }
    data.append(record)

# --- DataFrame Creation and Export ---
# Create DataFrame
df = pd.DataFrame(data)

# Export to CSV
df.to_csv("consumer_application_data.csv", index=False)

print("Data generation complete. CSV file created: solar_application_data.csv")
