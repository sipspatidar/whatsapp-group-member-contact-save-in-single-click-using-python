#Created_By_Sips_Patidar
#Contact sipspatidar@gmail.com
#For More visit http://www.youtube.com/c/SVSTutorials
#its only for Education Purpose Don't Steal others Number And Don't Misuse it I m not reponsible for any damages
import sqlite3
import time

def extract_number(m_id_list):
	numbers = []
	for n in m_id_list:
		seperate = n[0].split('@')
		if(str(seperate[0]).isdigit()):
			numbers.append(seperate[0])
	return numbers

	
def translator(str):
	new = ""
	str = str.replace("\n","")
	for i in str:
		if(i.isalnum() or i.isspace()):
			new = new+i;
	return new
print("Making Connection............")
conn = sqlite3.connect("msgstore.db")
c = conn.cursor()
time.sleep(1)
print("Successfully Connected....")
c.execute("select key_remote_jid,subject from chat_list")
g_list = c.fetchall()
i=0;
for g_id in g_list:
	print("Extracting Contacts....................")
	print("Group Id "+g_id[0])
	c.execute("select jid from group_participants where gjid='"+g_id[0]+"'")
	m_id_list = c.fetchall()
	numbers = extract_number(m_id_list)
	numbers.sort()	
	time.sleep(1)
	print("Creating file..............")
	if(g_id[1]!=""):
		name = translator(str(g_id[1]))
		fo = open(name+".vcf","w")
		print("Writting to file...................")
		fo.write("BEGIN:VCARD\n")
		fo.write("VERSION:3.0\n")
		try:
			fo.write("N:"+translator(str(g_id[1]))+"\n")
			fo.write("FN:"+translator(str(g_id[1]))+"\n")
		except:
			print("Error: can\'t Write Conatct Name \n Write Another name")
			fo.write("N:alternate\n")
			fo.write("FN:alternate\n")
		
		for n in numbers:
			fo.write("TEL;CELL:+"+n)
			fo.write("\n")
		fo.write("END:VCARD");
		fo.close()
	time.sleep(1)
	print("Contact File is Created Successfully")				
	i=i+1
	print("File Created : "+str(i)+"\n")

#Stay_Connected :p :) 	
