from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv


driver = webdriver.Chrome(executable_path='chromedriver')


def first_csv():
    file = open('main.csv', 'a+', newline ='')
    with file:
        header = ['Main_Title','Listing_ID', 'List_Price', 'Status','Property_Type','Property_Sub_Type','City','County','Parcel_Number']
        writer_main = csv.DictWriter(file, fieldnames = header)
        writer_main.writeheader()
        return writer_main   
def second_csv():
    file = open('sub.csv', 'a+', newline ='')
    with file:
        header = ['Main_Title','Assessment Year','2021','2020','2019']
        writer_sub = csv.DictWriter(file, fieldnames = header)
        writer_sub.writeheader()
        return writer_sub
def first_csv_t():
    filename = 'main.csv'
    with open(filename, 'w',encoding='UTF8',newline='') as csvfile:
        fields = ['Main_Title','Listing_ID', 'List_Price', 'Status','Property_Type','Property_Sub_Type','City','County','Parcel_Number']
        writer_main = csv.writer(csvfile)
        writer_main.writerow(fields)             
        return writer_main
def first_csv_s():
    filename = 'sub.csv'
    with open(filename, 'w',encoding='UTF8',newline='') as csvfile:
        fields = ['Main_Title','Assessment Year','2021','2020','2019']
        writer_sub = csv.writer(csvfile)
        writer_sub.writerow(fields)             
        return writer_sub

def scraping():
    link ='https://matrix.abor.com/Matrix/Public/Portal.aspx?ID=0-1717879991-10'
    driver.get(link)
    time.sleep(5)
    total_listing = driver.find_elements_by_xpath('//div[@id="_ctl0_m_divAsyncPagedDisplays"]/div')
    listtingCount=len(total_listing)
    _genral_info = []
    sub_list = []
    for i in range(1,listtingCount+1):
        driver.find_element_by_xpath("//div[@id='_ctl0_m_divAsyncPagedDisplays']/div["+str(i)+"]//span[@class='formula J_formula']/a|//div[@id='_ctl0_m_divAsyncPagedDisplays']/div["+str(i)+"]//span[@class='formula J_formula']/b/a").click()
        time.sleep(10)
        title ='';address='';Listing_ID='';List_Price='';Status='';Property_Type='';Property_Sub_Type='';City='';County='';Parcel_Number='';Subdivision='';Legal_Description='';Tax_Block='';Tax_Lot='';MLS_Area='';School_District='';Elementary_School='';Middle_Or_Junior_School='';High_School='';SqFt='';Living_Area_Source='';SqFt_dollar='';Acres='';Lot_Size_Square_Feet='';Main_Level_Beds='';Beds='';Full_Baths='';Half_Baths='';Baths='';Dining='';Living='';Year_Built='';Year_Built_Source='';Levels='';Pool_Private_YN='';Pool_Features='';Property_Condition='';Garage='';Parking='';Parking_Features='';Roof='';Direction_Faces='';Builder_Name='';Construction_Materials='';Accessibility_Features='';Horse_YN='';Horse_Amenities='';Waterfront_YN='';Waterfront_Features='';Foundation_Details='';Restrictions='';Security_Features='';Heating='';Cooling='';Utilities='';Water_Source='';Sewer='';Association_YN='';Association_Name='';Association_Fee='';Association_Fee_Frequency='';Association_Fee_Includes='';Estimated_Taxes='';Tax_Year='';Tax_Rate=''
        title = driver.find_element_by_xpath("//*[@id='wrapperTable']/div/div/div[1]/div[1]/div/div[1]/span[@class='formula J_formula']").text
        address = driver.find_element_by_xpath("//*[@id='wrapperTable']/div/div/div[1]/div[1]/div/div[2]/span[@class='formula J_formula']").text
        general_info = driver.find_elements_by_xpath("//*[@id='wrapperTable']/div[2]/div/div/div/div")
        #_genral_info=General_Info(general_info)
        for info in general_info:
            if(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Listing ID")):
                Listing_ID=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("List Price")):
                List_Price=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Status")):
                Status=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Property Type")):
                Property_Type=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Property Sub Type")):
                Property_Sub_Type=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("City")):
                City=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("County")):
                County=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Parcel Number")):
                Parcel_Number=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Subdivision")):
                Subdivision=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Legal Description")):
                Legal_Description=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','') 
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Tax Block")):
                Tax_Block=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Tax Lot")):
                Tax_Lot=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("MLS Area")):
                MLS_Area=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("School District")):
                School_District=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Elementary School")):
                Elementary_School=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Middle Or Junior School")):
                Middle_Or_Junior_School=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("High School")):
                High_School=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("SqFt")):
                SqFt=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Living Area Source")):
                Living_Area_Source=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("$/SqFt")):
                SqFt_dollar=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Acres")):
                Acres=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Lot Size Square Feet")):
                Lot_Size_Square_Feet=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("# Main Level Beds")):
                Main_Level_Beds=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("# Beds")):
                Beds=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("# Full Baths")):
                Full_Baths=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("# Half Baths")):
                Half_Baths=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("# Baths")):
                Baths=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("# Dining")):
                Dining=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("# Living")):
                Living=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Year Built")):
                Year_Built=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Year Built Source")):
                Year_Built_Source=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Levels")):
                Levels=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Pool Private YN")):
                Pool_Private_YN=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Pool Features")):
                Pool_Features=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(info.find_element_by_xpath(".//div[1]/span").text.__contains__("Property Condition")):
                Property_Condition=info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            else:
                pass
        general_info_variable=[title,Listing_ID,List_Price,Status,Property_Type,Property_Sub_Type,City,County,Parcel_Number,Subdivision,Legal_Description,Tax_Block,Tax_Lot,MLS_Area,School_District,Elementary_School,Middle_Or_Junior_School,High_School,SqFt,Living_Area_Source,SqFt_dollar,Acres,Lot_Size_Square_Feet,Main_Level_Beds,Beds,Full_Baths,Half_Baths,Baths,Dining,Living,Year_Built,Year_Built_Source,Levels,Pool_Private_YN,Pool_Features,Property_Condition]
        property_info =driver.find_elements_by_xpath("//*[@id='wrapperTable']/div[5]/div/div/div/div")                                                                                                                                                
        for p_info in property_info:
            if(p_info.find_element_by_xpath(".//div[1]/span").text.__contains__("# Garage")):
                Garage=p_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(p_info.find_element_by_xpath(".//div[1]/span").text.__contains__("# Parking")):
                Parking=p_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(p_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Parking Features")):
                Parking_Features=p_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(p_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Roof")):
                Roof=p_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(p_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Direction Faces")):
                Direction_Faces=p_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(p_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Builder Name")):
                Builder_Name=p_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(p_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Construction Materials")):
                Construction_Materials=p_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(p_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Accessibility Features")):
                Accessibility_Features=p_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(p_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Horse YN")):
                Horse_YN=p_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(p_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Horse Amenities")):
                Horse_Amenities=p_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(p_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Waterfront YN")):
                Waterfront_YN=p_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(p_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Waterfront Features")):
                Waterfront_Features=p_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(p_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Foundation Details")):
                Foundation_Details=p_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(p_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Restrictions")):
                Restrictions=p_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(p_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Security Features")):
                Security_Features=p_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
        property_info_variable =[Garage,Parking,Parking_Features,Roof,Direction_Faces,Builder_Name,Construction_Materials,Accessibility_Features,Horse_YN,Horse_Amenities,Waterfront_YN,Waterfront_Features,Foundation_Details,Restrictions,Security_Features]         
        Interior_info =driver.find_elements_by_xpath("//*[@id='wrapperTable']/div[7]/div/div/div/div")                                                                                                                                                
        for i_info in Interior_info:
            if(i_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Laundry Location")):
                Laundry_Location=i_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(i_info.find_element_by_xpath(".//div[1]/span").text.__contains__("# Fireplaces")):
                Fireplaces=i_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(i_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Appliances")):
                Appliances=i_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(i_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Interior Features")):
                Interior_Features=i_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(i_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Flooring")):
                Flooring=i_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(i_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Window Features")):
                Window_Features=i_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(i_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Guest Accommodaton Desc")):
                Guest_Accommodaton=i_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')       
        Exterior_info =driver.find_elements_by_xpath("//*[@id='wrapperTable']/div[13]/div/div/div/div")                                                                                                                                                
        for e_info in Exterior_info:
            if(e_info.find_element_by_xpath(".//div[1]/span").text.__contains__("View")):
                View=e_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(e_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Fencing")):
                Fencing=e_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(e_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Exterior Features")):
                Exterior_Features=e_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(e_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Patio And Porch Features")):
                Patio_And_Porch=e_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(e_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Community Features")):
                Community_Features=e_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(e_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Lot Features")):
                Lot_Features=e_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(e_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Other Structures")):
                Other_Structures=e_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','') 
        Exterior_info_variable = [Laundry_Location,Fireplaces,Appliances,Interior_Features,Flooring,Window_Features,Guest_Accommodaton,View,Fencing,Exterior_Features,Patio_And_Porch,Community_Features,Lot_Features,Other_Structures]         
        Additional_info =driver.find_elements_by_xpath("//*[@id='wrapperTable']/div[16]/div/div/div/div")                                                                                                                                                
        for a_info in Additional_info:
            if(a_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Listing Agreement Document")):
                Listing_Agreement_Document=a_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(a_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Listing Agreement")):
                Listing_Agreement=a_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(a_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Special Listing Conditions")):
                Special_Listing_Conditions=a_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(a_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Disclosures")):
                Disclosures=a_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(a_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Documents Available")):
                Documents_Available=a_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(a_info.find_element_by_xpath(".//div[1]/span").text.__contains__("FEMA Flood Plain")):
                FEMA_Flood_Plain=a_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
        Additional_info_variable = [Listing_Agreement_Document,Listing_Agreement,Special_Listing_Conditions,Disclosures,Documents_Available,FEMA_Flood_Plain]        
        Utility_info =driver.find_elements_by_xpath("//*[@id='wrapperTable']/div[19]/div/div/div/div")                                                                                                                                                
        for u_info in Utility_info:
            if(u_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Heating")):
                Heating=u_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(u_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Cooling")):
                Cooling=u_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(u_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Utilities")):
                Utilities=u_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(u_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Water Source")):
                Water_Source=u_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(u_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Sewer")):
                Sewer=u_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')         
        Financial_info =driver.find_elements_by_xpath("//*[@id='wrapperTable']/div[25]/div/div/div/div")                                                                                                                                                
        for f_info in Financial_info:
            if(f_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Association YN")):
                Association_YN=f_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(f_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Association Name")):
                Association_Name=f_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(f_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Association Fee")):
                Association_Fee=f_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(f_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Association Fee Frequency")):
                Association_Fee_Frequency=f_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(f_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Association Fee Includes")):
                Association_Fee_Includes=f_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
            elif(f_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Estimated Taxes")):
                Estimated_Taxes=f_info.find_element_by_xpath(".//div[2]/span").text.replace(',','').replace('$','')  
            elif(f_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Tax Year")):
                Tax_Year=f_info.find_element_by_xpath(".//div[2]/span").text.replace(',','').replace('$','') 
            elif(f_info.find_element_by_xpath(".//div[1]/span").text.__contains__("Tax Rate")):
                Tax_Rate=f_info.find_element_by_xpath(".//div[2]/span").text.replace("'","").replace(',','').replace('$','')
        Financial_info_variable = [Heating,Cooling,Utilities,Water_Source,Sewer,Association_YN,Association_Name,Association_Fee,Association_Fee_Frequency,Association_Fee_Includes,Estimated_Taxes,Tax_Year,Tax_Rate]        
        making_row_1=[title,address,Listing_ID,List_Price,Status,Property_Type,Property_Sub_Type,City,County,Parcel_Number,Subdivision,Legal_Description,Tax_Block,Tax_Lot,MLS_Area,School_District,Elementary_School,Middle_Or_Junior_School,High_School,SqFt,Living_Area_Source,SqFt_dollar,Acres,Lot_Size_Square_Feet,Main_Level_Beds,Beds,Full_Baths,Half_Baths,Baths,Dining,Living,Year_Built,Year_Built_Source,Levels,Pool_Private_YN,Pool_Features,Property_Condition,Garage,Parking,Parking_Features,Roof,Direction_Faces,Builder_Name,Construction_Materials,Accessibility_Features,Horse_YN,Horse_Amenities,Waterfront_YN,Waterfront_Features,Foundation_Details,Restrictions,Security_Features,Heating,Cooling,Utilities,Water_Source,Sewer,Association_YN,Association_Name,Association_Fee,Association_Fee_Frequency,Association_Fee_Includes,Estimated_Taxes,Tax_Year,Tax_Rate] 
        _genral_info.append(making_row_1)      
        Assessment_Tax =driver.find_elements_by_xpath("//*[@id='wrapperTable']/div/div/div[2]/div/div[position()>1 and position()<last()-3]")                                                                                                                                             
        for Assessment in Assessment_Tax:
            div_loop = Assessment.find_elements_by_xpath(".//div/span")
            row_data_one ='';row_data_two='';row_data_three='';row_data_four=''
            row_data_one = div_loop[0].text.replace("'","")
            row_data_two = div_loop[1].text.replace(',','').replace('$','')
            row_data_three = div_loop[2].text.replace(',','').replace('$','')
            row_data_four = div_loop[3].text.replace(',','').replace('$','')
            making_row = [title,row_data_one,row_data_two,row_data_three,row_data_four]
            sub_list.append(making_row)
        driver.refresh()    
        time.sleep(1)                                                                          
    filename = 'main.csv'
    with open(filename, 'w',encoding='UTF8',newline='') as csvfile:
        fields =['Main_Title','Address','Listing_ID','List_Price','Status','Property_Type','Property_Sub_Type','City','County','Parcel_Number','Subdivision','Legal_Description','Tax_Block','Tax_Lot','MLS_Area','School_District','Elementary_School','Middle_Or_Junior_School','High_School,SqFt','Living_Area_Source','SqFt_dollar','Acres','Lot_Size_Square_Feet','Main_Level_Beds','Beds','Full_Baths','Half_Baths','Baths','Dining','Living','Year_Built','Year_Built_Source','Levels','Pool_Private_YN','Pool_Features','Property_Condition','Garage','Parking','Parking_Features','Roof','Direction_Faces','Builder_Name','Construction_Materials','Accessibility_Features','Horse_YN','Horse_Amenities','Waterfront_YN','Waterfront_Features','Foundation_Details','Restrictions','Security_Features','Heating','Cooling','Utilities','Water_Source','Sewer','Association_YN','Association_Name','Association_Fee','Association_Fee_Frequency','Association_Fee_Includes','Estimated_Taxes','Tax_Year','Tax_Rate']
        #fields = ['Main_Title','Listing_ID', 'List_Price', 'Status','Property_Type','Property_Sub_Type','City','County','Parcel_Number']
        writer_main = csv.writer(csvfile)
        writer_main.writerow(fields)
        writer_main.writerows(_genral_info)
    filename = 'sub.csv'
    with open(filename, 'w',encoding='UTF8',newline='') as csvfile:
        fields = ['Main_Title','Assessment Year','2021','2020','2019']
        writer_sub = csv.writer(csvfile)
        writer_sub.writerow(fields)
        writer_sub.writerows(sub_list)
scraping()
