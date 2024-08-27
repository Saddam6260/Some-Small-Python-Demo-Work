bd_division_info = {"Sylhet" : {"upozila": 38, "union": 334, "district": 4},
                    "Barishal" : {"upozila": 39, "union": 333, "district": 6},
                    "Rangpur" : {"upozila": 58, "union": 536, "district": 8},
                    "Rajshahi" : {"upozila": 70, "union": 558, "district": 8},
                    "Chittagong" : {"upozila": 97, "union": 336, "district": 11},
                    "Mymensingh" : {"upozila": 34, "union": 350, "district": 4},
                    "Dhaka" : {"upozila": 93, "union": 1833, "district": 13},
                    "Khulna" : {"upozila": 59, "union": 270, "district": 10}}


bd_upozila = 0
bd_union = 0
bd_district = 0

for key, value in bd_division_info.items():
    bd_upozila += value["upozila"]
    bd_union += value["union"]
    bd_district += value["district"]

print("Total Upozila in Bangladesh :", bd_upozila)
print("Total Union in Bangladesh : ",bd_union)
print("Total District in Bangladesh : ", bd_district)