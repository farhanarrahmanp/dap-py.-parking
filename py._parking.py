# Program Tarif Parkir Mobil (Keluar)

import os

import datetime

now = datetime.datetime.now()
jk = int(now.strftime('%H'))
mk = int(now.strftime('%M'))
tgl = now.strftime(("%d/%m/%Y"))

fo = open("logparkir.txt","w")
f1 = open("logparkirv2.txt","w")
fo.write('\n\t\t\t\t\t\t\t'+"   DATA PARKIR"+"\n")
fo.write('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t'+tgl+'\n')
fo.write("_"*124+"\n")
fo.write("\n\tPlat nomor\t\tJenis Kendaraan\t\tJam Masuk\tJam Keluar\tLama Parkir\tTarif Parkir\n")
fo.write("_"*124+"\n")
fo.close()
f1.close()

# Input
def update_data():
	
	os.system('cls')

	Li = []
	
	fo = open("logparkir.txt","a+")
	
	print('\t\t\t\t\t\t _______________________________')
	print("\n\t\t\t\t\t\t\tHuruf depan?")
	kodedepannomor = input("\t\t\t\t\t\t\t>>> ")
	fo.write('\n\t'+kodedepannomor+' ')
	Li.append(kodedepannomor)
	
	print('\t\t\t\t\t\t _______________________________')
	print("\n\t\t\t\t\t\t\tNomor?")
	nomor = input("\t\t\t\t\t\t\t>>> ")
	fo.write(nomor+" ")
	Li.append(nomor)

	print('\t\t\t\t\t\t _______________________________')
	print("\n\t\t\t\t\t\t\tHuruf belakang?")
	kodebelakangnomor = input("\t\t\t\t\t\t\t>>> ")
	fo.write(kodebelakangnomor+' ')
	Li.append(kodebelakangnomor)

	print('\t\t\t\t\t\t _______________________________')
	print("\n\t\t\t\t\t\t\tJenis kendaraan?")
	print("\t\t\t\t\t\t  (Mobil = M, Sepeda motor = S)")
	
	jeniskendaraan = input("\t\t\t\t\t\t\t>>> ")
	i =1;
	while (i<=999):
		if jeniskendaraan == 'M' or jeniskendaraan == 'm':
			jeniskendaraan = 'Mobil   '
			i = i+999
		else:
			if jeniskendaraan == 'S' or jeniskendaraan =='s':
				jeniskendaraan = 'Sepeda motor   '
				i = i+999
			else:
				print('\t\t\t\t\t\t _______________________________')
				print('\n\t\t\t\t\t\t  Salah masukkan!\n\t\t\t\t\t\t  Silakan masukkan ulang.')
				print("\n\t\t\t\t\t\t\tJenis kendaraan?")
				print("\t\t\t\t\t\t  (Mobil = M, Sepeda motor = S)")
				jeniskendaraan = input("\t\t\t\t\t\t\t>>> ")
				i = i+1
	
	fo.write('\t\t'+jeniskendaraan)
	Li.append(jeniskendaraan)
	
	print('\t\t\t\t\t\t _______________________________')
	print("\n\t\t\t\t\t\t\tJam masuk?")
	jm = int(input("\t\t\t\t\t\t\t>>> "))
	Li.append(jm)
	print('\t\t\t\t\t\t _______________________________')
	print('\n\t\t\t\t\t\t\tMenit masuk?')
	mm = int(input('\t\t\t\t\t\t\t>>> '))
	Li.append(mm)
		
	Li.append(jk)
	Li.append(mk)
		
	while (jk) < (jm):
		print('\t\t\t\t\t\t _______________________________')
		print('\n\t\t\t\t\t\t  Salah masukkan!\n\t\t\t\t\t\t  Silakan masukkan ulang.')
		print("\n\t\t\t\t\t\t\tJam masuk?")
		jm = int(input("\t\t\t\t\t\t\t>>> "))
		Li[4] = jm
		Li[6] = jk
	if (jk) == (jm):
		while (mk) < (mm):
			print('\t\t\t\t\t\t _______________________________')
			print('\n\t\t\t\t\t\t  Salah masukkan!\n\t\t\t\t\t\t  Silakan masukkan ulang.')
			print("\n\t\t\t\t\t\t\tMenit masuk?")
			mm = int(input("\t\t\t\t\t\t\t>>> "))
			Li[5] = mm
			Li[7] = mk
	
	jmv2 = str(jm)
	mmv2 = str(mm)
	fo.write('\t\t'+jmv2)
	fo.write(':'+mmv2)
	fo.write("\t\t"+now.strftime('%H'))
	fo.write(':'+now.strftime('%M'))

	lama_parkir_jam = (Li[6]) - (Li[4])
	lama_parkir_menit = (Li[7]) - (Li[5])

	if (lama_parkir_menit < 0):
		lama_parkir_jam = lama_parkir_jam - 1
		lama_parkir_menit = 60 + lama_parkir_menit

	biaya_parkir = 3000 + (lama_parkir_jam) * 2000
	
	fo.write('\t\t'+str(lama_parkir_jam)+' J')
	fo.write(' '+str(lama_parkir_menit)+' M')
	fo.write('\tRp'+str(biaya_parkir)+'\n')
	Li.append(biaya_parkir)

	f1 = open("logparkirv2.txt","a+")
	f1.write(str(Li)+', ')
	print('\n\t\t\t\t\t\t'' _______________________________ ')
	print('\t\t\t\t\t\t''|\t\t                |')
	print('\t\t\t\t\t\t''| TARIF PARKIR SEBESAR RP'+str(biaya_parkir),'\t|')
	print('\t\t\t\t\t\t''|_______________________________|')
	ulang = 'n'
	while ulang == 'n' or ulang == 'N':
		print()
		print()
		ulang = input('Tekan Enter untuk kembali ke MENU . . . ')
	os.system('cls')
	print('\n Data Tersimpan!')	

def read_data():
	os.system('cls')
	fo = open("logparkir.txt","r+")
	viw = fo.read()
	print(viw)
	ulang = 'n'
	while ulang == 'n' or ulang == 'N':
		ulang = input('Tekan Enter untuk kembali ke MENU . . . ')
	os.system('cls')


def tampilan_menu():
	print()
	print('\t\t\t   ██████╗ ██╗   ██╗    ██████╗  █████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗')
	print('\t\t\t   ██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝')
	print('\t\t\t   ██████╔╝ ╚████╔╝     ██████╔╝███████║██████╔╝█████╔╝ ██║██╔██╗ ██║██║  ███╗')
	print('\t\t\t   ██╔═══╝   ╚██╔╝      ██╔═══╝ ██╔══██║██╔══██╗██╔═██╗ ██║██║╚██╗██║██║   ██║')
	print('\t\t\t   ██║        ██║██╗    ██║     ██║  ██║██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝')
	print('\t\t\t   ╚═╝        ╚═╝╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝')
	print('\n')
	print('\t╔╦╗╔═╗╔╗╔╦ ╦')
	print('\t║║║║╣ ║║║║ ║')
	print('\t╩ ╩╚═╝╝╚╝╚═╝\t\t\t\t\t\t\t\t\t\t\tBy Kel. 9 (CS-41-03)')
	print('_'*124)
	print('\t\t\t\t\t\t'' ______________________________ ')
	print('\t\t\t\t\t\t''|\t\t\t       |')
	print('\t\t\t\t\t\t''| [1] TAMPILKAN DATA TERSIMPAN |')
	print('\t\t\t\t\t\t''|______________________________|')
	print('\t\t\t\t\t\t'' ______________________________ ')
	print('\t\t\t\t\t\t''|\t\t\t       |')
	print('\t\t\t\t\t\t''| [2] MASUKKAN DATA            |')
	print('\t\t\t\t\t\t''|______________________________|')
	print('\t\t\t\t\t\t'' ______________________________ ')
	print('\t\t\t\t\t\t''|\t\t\t       |')
	print('\t\t\t\t\t\t''| [3] KELUAR DARI PROGRAM      |')
	print('\t\t\t\t\t\t''|______________________________|')
	

	menu = int(input("\n\n\t\t\t\t\t\t\tPILIH MENU >>> "))
	print ("\n")

	if menu == 1:
		read_data()
	elif menu == 2:
		update_data()
	elif menu == 3:
		exit()
	else:
		os.system('cls')
		print ("\n Salah pilih!")


if __name__ == "__main__":

    while(True):
        tampilan_menu()
